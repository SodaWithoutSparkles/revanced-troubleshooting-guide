#!/usr/bin/python3

import requests
import json
import os
import logging
import subprocess
import glob
import re
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
LUT_FILE = os.path.join(CACHE_DIR, 'update.lut.json')

# GitHub Actions environment
if os.getenv('GITHUB_ACTIONS') == 'true':
    EXPORT = os.getenv('GITHUB_OUTPUT')
    FORCED = os.getenv('EVENT') == 'workflow_dispatch'
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
    """Handle git operations for branch management"""
    
    @staticmethod
    def run_git_command(command):
        """Execute git command and return output"""
        try:
            # Use shell=True for commands with quoted arguments, otherwise split normally
            if '"' in command or "'" in command:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    check=True,
                    shell=True
                )
            else:
                result = subprocess.run(
                    command.split(),
                    capture_output=True,
                    text=True,
                    check=True
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
    def checkout_branch(branch):
        """Checkout to specified branch"""
        logging.info(f"Checking out to branch: {branch}")
        GitManager.run_git_command(f"git checkout {branch}")
    
    @staticmethod
    def commit_and_push(message, branch=None):
        """Commit changes and push to specified branch"""
        if branch:
            GitManager.checkout_branch(branch)
        
        # Add all changes
        GitManager.run_git_command("git add .")
        
        # Check if there are changes to commit
        try:
            GitManager.run_git_command("git diff --cached --exit-code")
            logging.info("No changes to commit")
            return False
        except subprocess.CalledProcessError:
            # There are changes to commit
            pass
        
        # Commit changes
        GitManager.run_git_command(f'git commit -m "{message}"')
        logging.info(f"Committed changes: {message}")
        
        # Push changes
        GitManager.run_git_command(f"git push origin {GitManager.get_current_branch()}")
        logging.info(f"Pushed to {GitManager.get_current_branch()}")
        return True

    @staticmethod
    def verify_branch_has_placeholders(branch_name):
        """Verify that the current branch contains placeholder variables"""
        try:
            # Count placeholder occurrences
            result = GitManager.run_git_command('grep -r "${YT_VERSION}\\|${LAST_UPDATE}" --include="*.md" .')
            placeholder_count = len(result.split('\n')) if result.strip() else 0
            
            logging.info(f"Found {placeholder_count} placeholder references in {branch_name} branch")
            return placeholder_count > 0
        except subprocess.CalledProcessError:
            # grep returns non-zero when no matches found
            logging.warning(f"No placeholders found in {branch_name} branch")
            return False
    
    @staticmethod
    def verify_branch_has_actual_values(branch_name):
        """Verify that the current branch contains actual values instead of placeholders"""
        try:
            # Look for patterns that indicate actual values
            timestamp_result = GitManager.run_git_command('grep -r "[0-9]\\{4\\}-[0-9]\\{2\\}-[0-9]\\{2\\} [0-9]\\{2\\}:[0-9]\\{2\\}:[0-9]\\{2\\} UTC" --include="*.md" .')
            version_result = GitManager.run_git_command('grep -r "Latest%20Supported%20Version-[0-9]" --include="*.md" .')
            
            has_timestamps = len(timestamp_result.split('\n')) if timestamp_result.strip() else 0
            has_versions = len(version_result.split('\n')) if version_result.strip() else 0
            
            logging.info(f"Found {has_timestamps} timestamp and {has_versions} version references in {branch_name} branch")
            return has_timestamps > 0 or has_versions > 0
        except subprocess.CalledProcessError:
            return False

class ReVancedVersionUpdater:
    """Main class for updating ReVanced versions"""
    
    def __init__(self):
        self.modified = False
        self.youtube_version = None
        self.last_update = None
        
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
    
    def load_lookup_table(self):
        """Load package name to common name lookup table"""
        try:
            with open(LUT_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.warning(f"Lookup table not found: {LUT_FILE}")
            return {}
    
    def check_if_update_needed(self, current_data):
        """Check if update is needed based on state file"""
        try:
            with open(STATE_FILE, 'r') as f:
                last_updated = int(f.readline().strip())
                last_result = f.read().strip()
        except FileNotFoundError:
            logging.info("State file not found, forcing update")
            return True
        
        current_result = json.dumps(current_data, sort_keys=True)
        time_now = int(datetime.now(timezone.utc).timestamp())
        
        # Check if data changed
        if current_result != last_result:
            logging.info('Patches data changed, update needed')
            return True
        
        # Check if more than 1 week has passed
        if (time_now - last_updated) > 604800:
            logging.info('More than 1 week since last update, forcing update')
            return True
        
        return False
    
    def update_state_file(self, data):
        """Update state file with current data"""
        time_now = int(datetime.now(timezone.utc).timestamp())
        data_str = json.dumps(data, sort_keys=True)
        
        os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
        with open(STATE_FILE, 'w') as f:
            f.write(f"{time_now}\n")
            f.write(data_str)
    
    def replace_placeholders_in_files(self, youtube_version, last_update):
        """Replace placeholders in all markdown files"""
        logging.info('Replacing placeholders in files...')
        
        # Find all markdown files
        md_files = glob.glob('**/*.md', recursive=True)
        
        # Convert version to dashed format for APKMirror URLs
        youtube_version_dashed = youtube_version.replace('.', '-')
        
        replacements = {
            '${YT_VERSION}': youtube_version,
            '${LAST_UPDATE}': last_update
        }
        
        files_updated = 0
        for file_path in md_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Handle placeholder replacements
                for placeholder, replacement in replacements.items():
                    content = content.replace(placeholder, replacement)
                
                # Handle APKMirror URL updates - find and replace hardcoded dashed versions
                # Pattern: youtube-XX-XX-XX-release and youtube-XX-XX-XX-android variants
                
                # Find existing dashed versions in APKMirror URLs and replace them
                apkmirror_patterns = [
                    # youtube-19-43-41-release
                    (r'youtube-\d+-\d+-\d+-release', f'youtube-{youtube_version_dashed}-release'),
                    # youtube-19-43-41-android-apk-download
                    (r'youtube-\d+-\d+-\d+-android', f'youtube-{youtube_version_dashed}-android'),
                    # youtube-19-43-41-2-android-apk-download (some have -2- suffix)
                    (r'youtube-\d+-\d+-\d+-\d+-android', f'youtube-{youtube_version_dashed}-2-android')
                ]
                
                for pattern, replacement in apkmirror_patterns:
                    content = re.sub(pattern, replacement, content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_updated += 1
                    logging.debug(f'Updated placeholders in: {file_path}')
                    
            except Exception as e:
                logging.warning(f'Failed to update {file_path}: {e}')
        
        logging.info(f'Updated placeholders in {files_updated} files')
        logging.info(f'YouTube version: {youtube_version} (dashed: {youtube_version_dashed})')
    
    def restore_placeholders_to_docs_base(self):
        """Restore placeholder variables in docs-base branch after committing actual values to main"""
        logging.info('Restoring placeholders in docs-base branch...')
        
        # Find all markdown files
        md_files = glob.glob('**/*.md', recursive=True)
        
        files_restored = 0
        for file_path in md_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Restore placeholders - reverse the replacement process
                # This finds actual values and replaces them back with placeholders
                
                # Restore timestamp placeholders (look for UTC timestamps)
                timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC'
                content = re.sub(timestamp_pattern, '${LAST_UPDATE}', content)
                
                # Restore version placeholders (look for version numbers in specific contexts)
                # Be very specific to avoid false positives
                version_patterns = [
                    # In version badges and similar contexts
                    (r'Latest%20Supported%20Version-\d+\.\d+\.\d+', 'Latest%20Supported%20Version-${YT_VERSION}'),
                    (r'It is \d+\.\d+\.\d+', 'It is ${YT_VERSION}'),
                    # In code blocks and direct version references
                    (r'```\n\d+\.\d+\.\d+\n```', '```\n${YT_VERSION}\n```'),
                    # In APK names and file references
                    (r'youtube-revanced_v\d+\.\d+\.\d+\.apk', 'youtube-revanced_v${YT_VERSION}.apk'),
                    # In version tables (| YouTube | VERSION |)
                    (r'\| YouTube \| \d+\.\d+\.\d+ \|', '| YouTube | ${YT_VERSION} |'),
                    # Version verification text
                    (r'version \d+\.\d+\.\d+', 'version ${YT_VERSION}'),
                    (r'version \*\*\d+\.\d+\.\d+\*\*', 'version **${YT_VERSION}**'),
                ]
                
                for pattern, replacement in version_patterns:
                    content = re.sub(pattern, replacement, content)
                
                # Restore APKMirror URL placeholders - convert back to old hardcoded version
                # This is more complex since we need to detect the current pattern and replace with old one
                apkmirror_restore_patterns = [
                    # Restore release URLs back to 19-43-41 (the original hardcoded version)
                    (r'youtube-\d+-\d+-\d+-release', 'youtube-19-43-41-release'),
                    # Restore android URLs back to 19-43-41
                    (r'youtube-\d+-\d+-\d+-android', 'youtube-19-43-41-android'),
                    # Restore 2-android URLs back to 19-43-41-2
                    (r'youtube-\d+-\d+-\d+-\d+-android', 'youtube-19-43-41-2-android')
                ]
                
                for pattern, replacement in apkmirror_restore_patterns:
                    content = re.sub(pattern, replacement, content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    files_restored += 1
                    logging.debug(f'Restored placeholders in: {file_path}')
                    
            except Exception as e:
                logging.warning(f'Failed to restore placeholders in {file_path}: {e}')
        
        if files_restored > 0:
            logging.info(f'Restored placeholders in {files_restored} files')
            
            # Commit the restored placeholders to docs-base
            try:
                GitManager.run_git_command("git add .")
                GitManager.run_git_command('git commit -m "Restore placeholders in docs-base branch"')
                logging.info('Committed placeholder restoration to docs-base')
            except subprocess.CalledProcessError:
                logging.info('No changes to commit for placeholder restoration')
        else:
            logging.info('No files needed placeholder restoration')

    def run(self):
        """Main execution method"""
        try:
            # Validate git repository
            if not os.path.exists('.git'):
                logging.error("Not in a git repository")
                self.export_output('modified', 'false')
                return
            
            # Ensure we're on the docs-base branch
            current_branch = GitManager.get_current_branch()
            if current_branch != DOCS_BRANCH:
                logging.info(f"Currently on {current_branch}, switching to {DOCS_BRANCH}")
                try:
                    GitManager.checkout_branch(DOCS_BRANCH)
                except subprocess.CalledProcessError:
                    logging.error(f"Failed to checkout {DOCS_BRANCH} branch")
                    self.export_output('modified', 'false')
                    return
            
            # Verify docs-base has placeholders (as it should)
            if not GitManager.verify_branch_has_placeholders(DOCS_BRANCH):
                logging.warning("docs-base branch doesn't contain expected placeholders!")
                # This might indicate a previous run failed to restore placeholders
                # Continue anyway, but log the issue
            
            # Fetch API data
            patches_data, version_data = self.fetch_api_data()
            
            # Parse data
            package_versions = self.parse_patches_data(patches_data)
            
            # Get YouTube version
            youtube_version = self.get_youtube_version(package_versions)
            if not youtube_version or youtube_version == 'ANY':
                logging.error("Could not find valid YouTube version")
                self.export_output('modified', 'false')
                return
            
            logging.info(f"Found YouTube version: {youtube_version}")
            
            # Check if update is needed
            if not (self.check_if_update_needed(package_versions) or FORCED):
                logging.info('No update needed')
                self.export_output('modified', 'false')
                self.export_output('youtube_version', youtube_version)
                return
            
            # Generate timestamp
            last_update = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            
            # Replace placeholders in files
            self.replace_placeholders_in_files(youtube_version, last_update)
            
            # Update state file
            self.update_state_file(package_versions)
            
            # Commit and push to main branch (only if not in test mode)
            if not os.getenv('DRY_RUN'):
                commit_message = f"Update versions: YouTube {youtube_version} ({last_update})"
                changes_made = GitManager.commit_and_push(commit_message, MAIN_BRANCH)
                
                # Return to docs-base branch and restore placeholders
                GitManager.checkout_branch(DOCS_BRANCH)
                
                # Reset docs-base to its original state with placeholders
                self.restore_placeholders_to_docs_base()
                
                # Verify restoration was successful
                if GitManager.verify_branch_has_placeholders(DOCS_BRANCH):
                    logging.info("✓ Successfully restored placeholders in docs-base branch")
                else:
                    logging.error("✗ Failed to restore placeholders in docs-base branch")
                    # This is a serious issue but don't fail the whole process
                    
                # Verify main branch has actual values (quick check)
                try:
                    GitManager.checkout_branch(MAIN_BRANCH)
                    if GitManager.verify_branch_has_actual_values(MAIN_BRANCH):
                        logging.info("✓ main branch contains actual values as expected")
                    else:
                        logging.warning("main branch might not have been updated properly")
                    GitManager.checkout_branch(DOCS_BRANCH)  # Return to docs-base
                except Exception as e:
                    logging.warning(f"Could not verify main branch: {e}")
                    # Ensure we're back on docs-base
                    try:
                        GitManager.checkout_branch(DOCS_BRANCH)
                    except:
                        pass
            else:
                logging.info("DRY_RUN mode: Skipping git operations")
                changes_made = True
            
            # Export outputs
            self.export_output('modified', 'true' if changes_made else 'false')
            self.export_output('youtube_version', youtube_version)
            self.export_output('last_update', last_update)
            
            logging.info(f'Update completed successfully. YouTube version: {youtube_version}')
            
        except Exception as e:
            logging.error(f'Update failed: {e}')
            self.export_output('modified', 'false')
            # Try to return to docs-base branch if we're not on it
            try:
                current_branch = GitManager.get_current_branch()
                if current_branch != DOCS_BRANCH:
                    GitManager.checkout_branch(DOCS_BRANCH)
            except:
                pass
            raise

def main():
    """Main entry point"""
    updater = ReVancedVersionUpdater()
    updater.run()

if __name__ == '__main__':
    main()
