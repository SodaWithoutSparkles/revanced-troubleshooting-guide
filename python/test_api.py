#!/usr/bin/python3

import requests
import json
import os
import logging
import subprocess
import glob
from datetime import datetime
from packaging import version

# Configuration
PATCHES_LIST_API = 'https://api.revanced.app/v4/patches/list'
PATCHES_VERSION_API = 'https://api.revanced.app/v4/patches/version'

# File paths
CACHE_DIR = '.conf/python'
JSON_FILE = os.path.join(CACHE_DIR, 'patches_list.json')
VERSION_FILE = os.path.join(CACHE_DIR, 'patches_version.json')

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d: [%(levelname)s] %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

class ReVancedVersionTester:
    """Test version of the updater without git operations"""
    
    def fetch_api_data(self):
        """Fetch data from ReVanced API v4"""
        logging.info('Fetching patches list from API...')
        
        # Fetch patches list
        response = requests.get(PATCHES_LIST_API)
        response.raise_for_status()
        patches_data = response.json()
        
        # Fetch patches version
        response = requests.get(PATCHES_VERSION_API)
        response.raise_for_status()
        version_data = response.json()
        
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
    
    def run_test(self):
        """Test the API parsing functionality"""
        try:
            # Fetch API data
            patches_data, version_data = self.fetch_api_data()
            
            logging.info(f"Fetched {len(patches_data)} patches")
            logging.info(f"Patches version: {version_data}")
            
            # Parse data
            package_versions = self.parse_patches_data(patches_data)
            
            logging.info(f"Found {len(package_versions)} packages with versions")
            
            # Get YouTube version
            youtube_version = self.get_youtube_version(package_versions)
            
            if youtube_version:
                logging.info(f"YouTube latest supported version: {youtube_version}")
            else:
                logging.error("Could not find YouTube version")
            
            # Show some other popular packages
            popular_packages = [
                'com.google.android.youtube',
                'com.google.android.apps.youtube.music',
                'com.ss.android.ugc.trill',  # TikTok
                'tv.twitch.android.app',
                'com.reddit.frontpage'
            ]
            
            print("\n=== Popular Package Versions ===")
            for pkg in popular_packages:
                if pkg in package_versions:
                    info = package_versions[pkg]
                    print(f"{pkg}: {info['latest_version']} (from {len(info['all_versions'])} versions)")
                else:
                    print(f"{pkg}: Not found")
            
            # Generate timestamp
            last_update = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
            print(f"\nGenerated timestamp: {last_update}")
            
            return True
            
        except Exception as e:
            logging.error(f'Test failed: {e}')
            return False

def main():
    """Main entry point for testing"""
    tester = ReVancedVersionTester()
    success = tester.run_test()
    if success:
        print("\n✅ Test completed successfully!")
    else:
        print("\n❌ Test failed!")

if __name__ == '__main__':
    main()
