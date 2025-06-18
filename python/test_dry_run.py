#!/usr/bin/python3

"""
Dry-run test script for update_versions.py
This script tests the functionality without modifying git or files
"""

import sys
import os

# Add the current directory to Python path to import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from update_versions import ReVancedVersionUpdater
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d: [%(levelname)s] %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

class DryRunUpdater(ReVancedVersionUpdater):
    """Dry run version that doesn't modify files or git"""
    
    def replace_placeholders_in_files(self, youtube_version, last_update):
        """Mock version that just logs what would be replaced"""
        logging.info('DRY RUN: Would replace placeholders in files...')
        logging.info(f'Would replace ${{YT_VERSION}} with: {youtube_version}')
        logging.info(f'Would replace ${{LAST_UPDATE}} with: {last_update}')
        
        # Show dashed version handling
        youtube_version_dashed = youtube_version.replace('.', '-')
        logging.info(f'Would replace APKMirror dashed versions with: {youtube_version_dashed}')
        
        # Count files that would be updated
        import glob
        md_files = glob.glob('../**/*.md', recursive=True)
        logging.info(f'Would check {len(md_files)} markdown files for placeholders')
    
    def update_state_file(self, data):
        """Mock version that doesn't actually update state"""
        logging.info('DRY RUN: Would update state file')
    
    def export_output(self, key: str, value: str):
        """Mock version that just prints outputs"""
        print(f"EXPORT: {key}={value}")

def main():
    """Test the updater in dry-run mode"""
    print("🧪 Running dry-run test of update_versions.py")
    print("=" * 50)
    
    updater = DryRunUpdater()
    
    try:
        # Fetch and parse API data
        patches_data, version_data = updater.fetch_api_data()
        package_versions = updater.parse_patches_data(patches_data)
        
        # Get YouTube version
        youtube_version = updater.get_youtube_version(package_versions)
        
        if not youtube_version:
            print("❌ Could not find YouTube version")
            return
        
        print(f"✅ Found YouTube version: {youtube_version}")
        
        # Test placeholder replacement (dry run)
        from datetime import datetime, timezone
        last_update = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        
        updater.replace_placeholders_in_files(youtube_version, last_update)
        
        # Mock exports
        updater.export_output('modified', 'true')
        updater.export_output('youtube_version', youtube_version)
        updater.export_output('last_update', last_update)
        
        print("\n✅ Dry-run test completed successfully!")
        print(f"📺 YouTube version: {youtube_version}")
        print(f"🕒 Timestamp: {last_update}")
        
    except Exception as e:
        print(f"❌ Dry-run test failed: {e}")
        logging.exception("Error details:")

if __name__ == '__main__':
    main()
