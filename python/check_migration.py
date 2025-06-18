#!/usr/bin/python3

"""
Migration Readiness Check
Validates that the system is ready to migrate from old to new version updater
"""

import os
import sys
import json
import subprocess
import glob

class MigrationChecker:
    def __init__(self):
        self.checks = []
        self.warnings = []
        self.errors = []

    def log(self, message, level='info'):
        if level == 'error':
            self.errors.append(message)
            print(f"❌ {message}")
        elif level == 'warning':
            self.warnings.append(message)
            print(f"⚠️  {message}")
        else:
            self.checks.append(message)
            print(f"✅ {message}")

    def check_git_repository(self):
        """Check if we're in a git repository"""
        if os.path.exists('.git'):
            self.log("Git repository detected")
            return True
        else:
            self.log("Not in a git repository", 'error')
            return False

    def check_git_branches(self):
        """Check git branch setup"""
        try:
            result = subprocess.run(['git', 'branch', '-r'], capture_output=True, text=True)
            remote_branches = result.stdout
            
            has_main = 'origin/main' in remote_branches
            has_docs_base = 'origin/docs-base' in remote_branches
            
            if has_main:
                self.log("Main branch exists")
            else:
                self.log("Main branch not found", 'warning')
            
            if has_docs_base:
                self.log("docs-base branch exists")
            else:
                self.log("docs-base branch not found - will be created automatically", 'warning')
                
        except subprocess.CalledProcessError:
            self.log("Could not check git branches", 'error')

    def check_python_dependencies(self):
        """Check if Python dependencies are available"""
        try:
            import requests
            self.log("requests library available")
        except ImportError:
            self.log("requests library not installed", 'error')
        
        try:
            import packaging
            self.log("packaging library available")
        except ImportError:
            self.log("packaging library not installed", 'error')

    def check_api_connectivity(self):
        """Test API connectivity"""
        try:
            import requests
            response = requests.get('https://api.revanced.app/v4/patches/version', timeout=10)
            if response.status_code == 200:
                data = response.json()
                version = data.get('version', 'unknown')
                self.log(f"API v4 connectivity OK (patches version: {version})")
            else:
                self.log(f"API returned status {response.status_code}", 'warning')
        except Exception as e:
            self.log(f"API connectivity failed: {e}", 'error')

    def check_configuration_files(self):
        """Check existing configuration files"""
        config_files = [
            '.conf/python/update.lut.json',
            '.conf/python/update.state',
            '.conf/python/update.template'
        ]
        
        for file_path in config_files:
            if os.path.exists(file_path):
                self.log(f"Configuration file exists: {file_path}")
            else:
                if 'update.state' in file_path:
                    self.log(f"State file missing: {file_path} - will be created", 'warning')
                else:
                    self.log(f"Configuration file missing: {file_path}", 'warning')

    def check_placeholder_usage(self):
        """Check for placeholder usage in markdown files"""
        md_files = glob.glob('**/*.md', recursive=True)
        
        yt_version_count = 0
        last_update_count = 0
        
        for file_path in md_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if '${YT_VERSION}' in content:
                        yt_version_count += 1
                    if '${LAST_UPDATE}' in content:
                        last_update_count += 1
            except:
                continue
        
        if yt_version_count > 0:
            self.log(f"Found ${'{YT_VERSION}'} placeholder in {yt_version_count} files")
        else:
            self.log("No ${YT_VERSION} placeholders found", 'warning')
        
        if last_update_count > 0:
            self.log(f"Found ${'{LAST_UPDATE}'} placeholder in {last_update_count} files")
        else:
            self.log("No ${LAST_UPDATE} placeholders found", 'warning')

    def check_old_system(self):
        """Check for old system files"""
        old_files = [
            'checkReVancedVersion.py',
            '.github/workflows/version-and-lastCheck-bump.yml'
        ]
        
        for file_path in old_files:
            if os.path.exists(file_path):
                self.log(f"Old system file found: {file_path}")
            else:
                self.log(f"Old system file not found: {file_path}", 'warning')

    def check_new_system(self):
        """Check for new system files"""
        new_files = [
            'python/update_versions.py',
            'python/requirements.txt',
            'python/run_updater.sh'
        ]
        
        for file_path in new_files:
            if os.path.exists(file_path):
                self.log(f"New system file ready: {file_path}")
            else:
                self.log(f"New system file missing: {file_path}", 'error')

    def run_all_checks(self):
        """Run all migration readiness checks"""
        print("🔍 Migration Readiness Check")
        print("=" * 40)
        
        self.check_git_repository()
        self.check_git_branches()
        self.check_python_dependencies()
        self.check_api_connectivity()
        self.check_configuration_files()
        self.check_placeholder_usage()
        self.check_old_system()
        self.check_new_system()
        
        print("\n" + "=" * 40)
        print("📊 Summary")
        print(f"✅ Checks passed: {len(self.checks)}")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        print(f"❌ Errors: {len(self.errors)}")
        
        if self.errors:
            print("\n🚨 Critical Issues:")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        print("\n" + "=" * 40)
        
        if not self.errors:
            print("🎉 Migration ready! You can proceed with the new system.")
            return True
        else:
            print("🔧 Please fix the errors above before migrating.")
            return False

def main():
    """Main entry point"""
    checker = MigrationChecker()
    ready = checker.run_all_checks()
    
    if ready:
        print("\n📖 Next steps:")
        print("1. Review MIGRATION.md for detailed instructions")
        print("2. Test with: ./python/run_updater.sh --dry-run")
        print("3. Copy new-workflow.yml to .github/workflows/")
        print("4. Disable old workflow")
        
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
