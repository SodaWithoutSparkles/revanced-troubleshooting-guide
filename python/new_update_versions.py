#!/usr/bin/python3

import requests
import json
import os
import logging
import subprocess
import glob
import re
import shutil
from datetime import datetime, timezone
from packaging import version

# Configuration
PATCHES_LIST_API = 'https://api.revanced.app/v4/patches/list'
PATCHES_VERSION_API = 'https://api.revanced.app/v4/patches/version'

DOCS_BRANCH = 'docs-base'
MAIN_BRANCH = 'main'

# File paths
CACHE_DIR = '.conf/python'
JSON_FILE = os.path.join(CACHE_DIR, 'patches_list.json')
VERSION_FILE = os.path.join(CACHE_DIR, 'patches_version.json')
STATE_FILE = os.path.join(CACHE_DIR, 'update.state')

# GitHub Actions environment
if os.getenv('GITHUB_ACTIONS') == 'true':
    EXPORT = os.getenv('GITHUB_OUTPUT')
else:
    EXPORT = None

FORCED = os.getenv('FORCE') is not None

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d: [%(levelname)s] %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

class GitManager:
    """Simplified git operations manager"""
    
    @staticmethod
    def run_git_command(command):
        """Execute git command and return output"""
        try:
            result = subprocess.run(
                command.split() if isinstance(command, str) and '"' not in command else command,
                capture_output=True,
                text=True,
                check=True,
                shell=isinstance(command, str) and '"' in command
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logging.error(f"Git command failed: {command}")
            logging.error(f"Error: {e.stderr}")
            raise
    
    @staticmethod
    def get_current_branch():
        """Get current git branch"""
        return GitManager.run_git_command("git rev-parse --abbrev-ref HEAD")
    
    @staticmethod
    def switch_to_branch(branch):
        """Switch to specified branch"""
        logging.info(f"Switching to branch: {branch}")
        try:
            # Fetch latest changes
            GitManager.run_git_command("git fetch origin")
            
            # Switch to branch (create if doesn't exist)
            try:
                GitManager.run_git_command(f"git checkout {branch}")
            except subprocess.CalledProcessError:
                # Branch doesn't exist locally, try to create from remote
                try:
                    GitManager.run_git_command(f"git checkout -b {branch} origin/{branch}")
                except subprocess.CalledProcessError:
                    # Remote doesn't exist either, create new branch
                    GitManager.run_git_command(f"git checkout -b {branch}")
                    
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to switch to branch {branch}: {e}")
            raise
    
    @staticmethod
    def has_staged_changes():
        """Check if there are staged changes"""
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--exit-code"],
                capture_output=True,
                text=True,
                check=False  # Don't raise exception on non-zero exit
            )
            # Exit code 0 means no differences (no staged changes)
            # Exit code 1 means there are differences (staged changes exist)
            return result.returncode != 0
        except subprocess.CalledProcessError:
            # Fallback: assume there are changes if command fails
            return True
    
    @staticmethod
    def force_push_files(files, branch, commit_message):
        """Force push specific files to a branch"""
        logging.info(f"Force pushing {len(files)} files to {branch}")
        
        try:
            # Stage specific files
            for file_path in files:
                GitManager.run_git_command(f"git add {file_path}")
            
            # Check if there are changes to commit
            if not GitManager.has_staged_changes():
                logging.info("No changes to commit")
                return False
            
            # Commit changes
            GitManager.run_git_command(f'git commit -m "{commit_message}"')
            logging.info(f"Committed changes: {commit_message}")
            
            # Force push to branch
            GitManager.run_git_command(f"git push origin HEAD:{branch} --force")
            logging.info(f"Force pushed to {branch}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to force push files: {e}")
            raise

class ReVancedVersionUpdater:
    """Main class for updating ReVanced versions"""
    
    def __init__(self):
        self.backup_file_paths = []
        
    def export_output(self, key: str, value: str):
        """Export key-value pair to GitHub Actions output"""
        if EXPORT:
            with open(EXPORT, 'a') as f:
                f.write(f'{key}={value}\n')
    
    def fetch_api_data(self):
        """Fetch data from ReVanced API v4"""
        logging.info('Fetching patches list from API...')
        
        # Create cache directory if it doesn't exist
        os.makedirs(CACHE_DIR, exist_ok=True)
        
        # Fetch patches list
        response = requests.get(PATCHES_LIST_API)
        response.raise_for_status()
        patches_data = response.json()
        
        with open(JSON_FILE, 'w') as f:
            json.dump(patches_data, f, indent=2)
        
        # Fetch patches version
        response = requests.get(PATCHES_VERSION_API)
        response.raise_for_status()
        version_data = response.json()
        
        with open(VERSION_FILE, 'w') as f:
            json.dump(version_data, f, indent=2)
        
        return patches_data, version_data
    
    def parse_patches_data(self, patches_data):
        """Parse patches data to extract compatible versions"""
        logging.info('Parsing patches data...')
        
        package_versions = {}
        
        for patch in patches_data:
            if not patch.get('compatiblePackages'):
                continue
                
            for package_name, versions in patch['compatiblePackages'].items():
                if versions is None:
                    # Universal compatibility
                    continue
                    
                if package_name not in package_versions:
                    package_versions[package_name] = set()
                
                package_versions[package_name].update(versions)
        
        # Convert sets to sorted lists and find latest version for each package
        result = {}
        for package_name, versions in package_versions.items():
            version_list = sorted(list(versions), key=self.version_sort_key, reverse=True)
            result[package_name] = {
                'latest_version': version_list[0] if version_list else 'ANY',
                'all_versions': version_list
            }
        
        return result
    
    def version_sort_key(self, ver):
        """Custom sorting key for versions"""
        if ver == 'ANY':
            return version.parse('0.0.0')  # ANY should be ranked lowest
        try:
            return version.parse(ver)
        except:
            # Fallback to string comparison
            return version.parse('0.0.0')
    
    def get_youtube_version(self, package_versions):
        """Extract YouTube version from parsed data"""
        youtube_package = 'com.google.android.youtube'
        if youtube_package in package_versions:
            return package_versions[youtube_package]['latest_version']
        return None
    
    def check_if_update_needed(self, current_data):
        """Check if update is needed based on state file or time"""
        try:
            with open(STATE_FILE, 'r') as f:
                last_updated = int(f.readline().strip())
                last_result = f.read().strip()
        except FileNotFoundError:
            logging.info("State file not found, forcing update")
            return True, "state_file_missing"
        
        current_result = json.dumps(current_data, sort_keys=True)
        time_now = int(datetime.now(timezone.utc).timestamp())
        
        # Check if data changed
        if current_result != last_result:
            logging.debug(f"Data difference:\nOld: {last_result}\nNew: {current_result}")
            logging.info('Patches data changed, update needed')
            return True, "patches_updated"
        
        # Check if more than 1 month has passed (30 days * 24 hours * 3600 seconds)
        if (time_now - last_updated) > 2592000:
            logging.info('More than 1 month since last update, forcing update')
            return True, "time_threshold_exceeded"
        
        logging.info('Read state file, No update needed')
        return False, "no_update_needed"
    
    def update_state_file(self, data):
        """Update state file with current data"""
        time_now = int(datetime.now(timezone.utc).timestamp())
        data_str = json.dumps(data, sort_keys=True)
        
        os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
        with open(STATE_FILE, 'w') as f:
            f.write(f"{time_now}\n")
            f.write(data_str)
    
    def find_markdown_files_with_placeholders(self):
        """Find all markdown files containing placeholders"""
        logging.info('Finding markdown files with placeholders...')
        
        md_files = glob.glob('**/*.md', recursive=True)
        files_with_placeholders = []
        
        for file_path in md_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '${YT_VERSION}' in content or '${LAST_UPDATE}' in content or '${YT_VERSION_DASHED}' in content:
                    files_with_placeholders.append(file_path)
                    
            except Exception as e:
                logging.warning(f'Failed to read {file_path}: {e}')
        
        logging.info(f'Found {len(files_with_placeholders)} files with placeholders')
        return files_with_placeholders
    
    def backup_files(self, file_paths):
        """Create .bak copies of files"""
        logging.info(f'Creating backups for {len(file_paths)} files...')
        
        self.backup_file_paths = []
        for file_path in file_paths:
            backup_path = file_path + '.bak'
            try:
                shutil.copy2(file_path, backup_path)
                self.backup_file_paths.append(backup_path)
                logging.debug(f'Backed up {file_path} to {backup_path}')
            except Exception as e:
                logging.warning(f'Failed to backup {file_path}: {e}')
        
        logging.info(f'Created {len(self.backup_file_paths)} backup files')
    
    def restore_backups(self):
        """Restore files from .bak copies and clean up"""
        logging.info(f'Restoring {len(self.backup_file_paths)} files from backups...')
        
        restored = 0
        for backup_path in self.backup_file_paths:
            original_path = backup_path[:-4]  # Remove .bak extension
            try:
                shutil.move(backup_path, original_path)
                restored += 1
                logging.debug(f'Restored {original_path} from backup')
            except Exception as e:
                logging.warning(f'Failed to restore {original_path}: {e}')
        
        logging.info(f'Restored {restored} files from backups')
        self.backup_file_paths = []
    
    def replace_placeholders_in_files(self, file_paths, youtube_version, last_update):
        """Replace placeholders in specified files"""
        logging.info(f'Replacing placeholders in {len(file_paths)} files...')
        
        # Convert version to dashed format for APKMirror URLs
        youtube_version_dashed = youtube_version.replace('.', '-')
        
        replacements = {
            '${YT_VERSION}': youtube_version,
            '${YT_VERSION_DASHED}': youtube_version_dashed,
            '${LAST_UPDATE}': last_update
        }
        
        files_updated = 0
        total_replacements = 0
        
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                file_replacements = 0
                
                # Handle placeholder replacements
                for placeholder, replacement in replacements.items():
                    count = content.count(placeholder)
                    content = content.replace(placeholder, replacement)
                    file_replacements += count
                    total_replacements += count
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_updated += 1
                    logging.debug(f'Updated {file_replacements} placeholders in: {file_path}')
                    
            except Exception as e:
                logging.warning(f'Failed to update {file_path}: {e}')
        
        logging.info(f'Updated {total_replacements} placeholders in {files_updated} files')
        return files_updated, total_replacements
    
    def cleanup_on_error(self):
        """Clean up backup files in case of error"""
        if self.backup_file_paths:
            logging.info('Cleaning up backup files due to error...')
            for backup_path in self.backup_file_paths:
                try:
                    if os.path.exists(backup_path):
                        os.remove(backup_path)
                        logging.debug(f'Removed backup file: {backup_path}')
                except Exception as e:
                    logging.warning(f'Failed to remove backup {backup_path}: {e}')
            self.backup_file_paths = []
    
    def run(self):
        """Main execution method"""
        try:
            # Validate git repository
            if not os.path.exists('.git'):
                logging.error("Not in a git repository")
                self.export_output('modified', 'false')
                return
            
            # Step 1: Switch to docs-base branch
            GitManager.switch_to_branch(DOCS_BRANCH)
            
            # Fetch API data
            patches_data, version_data = self.fetch_api_data()
            patches_version = version_data.get('version', 'unknown') if isinstance(version_data, dict) else 'unknown'
            logging.info(f"patches v{patches_version} fetched from API")
            self.export_output('patches_version', patches_version)
            
            # Parse data
            package_versions = self.parse_patches_data(patches_data)
            
            # Get YouTube version
            youtube_version = self.get_youtube_version(package_versions)
            if not youtube_version or youtube_version == 'ANY':
                logging.error("Could not find valid YouTube version")
                self.export_output('modified', 'false')
                return
            
            logging.info(f"Found YouTube version: {youtube_version}")
            
            # Step 2: Check if update is needed
            _is_update_needed, update_reason = self.check_if_update_needed(patches_data)
            if not (_is_update_needed or FORCED):
                logging.info('No update needed')
                self.export_output('modified', 'false')
                self.export_output('youtube_version', youtube_version)
                self.export_output('update_reason', update_reason)
                return
            
            # Determine final update reason
            final_update_reason = "forced_update" if FORCED else update_reason
            logging.debug(f"Reason: {_is_update_needed=}, {FORCED=}, final_reason={final_update_reason}")
            # Generate timestamp
            last_update = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            
            # Step 3: Find markdown files with placeholders and backup them
            markdown_files = self.find_markdown_files_with_placeholders()
            if not markdown_files:
                logging.warning("No markdown files with placeholders found")
                self.export_output('modified', 'false')
                return
            
            self.backup_files(markdown_files)
            
            # Step 4: Update state file and commit to docs-base
            self.update_state_file(patches_data)
            
            if not os.getenv('DRY_RUN'):
                # Commit state file to docs-base for persistence
                state_commit_message = f"Update state: YouTube {youtube_version} ({last_update})"
                GitManager.force_push_files([STATE_FILE], DOCS_BRANCH, state_commit_message)
                logging.info(f"Updated state file on {DOCS_BRANCH}")
                
                # Step 5: Replace placeholders and push to main (markdown files only)
                files_updated, total_replacements = self.replace_placeholders_in_files(markdown_files, youtube_version, last_update)
                
                # Only commit markdown files to main branch (state file stays on docs-base)
                commit_message = f"Update versions: YouTube {youtube_version} ({last_update})"
                changes_made = GitManager.force_push_files(markdown_files, MAIN_BRANCH, commit_message)
                
                if changes_made:
                    logging.info(f"Successfully pushed updated files to {MAIN_BRANCH}")
                else:
                    logging.info("No changes were made to push")
                
                # Step 6: Restore backups
                self.restore_backups()
                
            else:
                logging.info("DRY_RUN mode: Skipping file updates and git operations")
                changes_made = True
                files_updated = len(markdown_files)
                total_replacements = 0
                # Still restore backups in dry run mode
                self.restore_backups()
            
            # Export outputs
            self.export_output('modified', 'true' if changes_made else 'false')
            self.export_output('youtube_version', youtube_version)
            self.export_output('last_update', last_update)
            self.export_output('update_reason', final_update_reason)
            self.export_output('files_updated', str(files_updated))
            self.export_output('total_replacements', str(total_replacements))
            
            # Create user-friendly reason message
            reason_messages = {
                "state_file_missing": "State file not found (first run)",
                "patches_updated": "ReVanced patches data updated",
                "time_threshold_exceeded": "More than 30 days since last update",
                "forced_update": "Manual workflow dispatch"
            }
            reason_message = reason_messages.get(final_update_reason, final_update_reason)
            
            logging.info(f'Update completed successfully. YouTube version: {youtube_version}')
            logging.info(f'Files updated: {files_updated}, Total replacements: {total_replacements}')
            logging.info(f'Update reason: {reason_message}')
            
        except Exception as e:
            logging.error(f'Update failed: {e}')
            self.export_output('modified', 'false')
            
            # Clean up on error
            try:
                self.restore_backups()
            except:
                self.cleanup_on_error()
            
            # Try to return to docs-base branch
            try:
                current_branch = GitManager.get_current_branch()
                if current_branch != DOCS_BRANCH:
                    GitManager.switch_to_branch(DOCS_BRANCH)
            except:
                pass
            
            raise

def main():
    """Main entry point"""
    updater = ReVancedVersionUpdater()
    updater.run()

if __name__ == '__main__':
    main()
