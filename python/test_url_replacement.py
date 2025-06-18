#!/usr/bin/python3

"""
Test APKMirror URL replacement with actual examples from the repository
"""

import re
import subprocess

def test_actual_urls():
    """Test with actual URLs found in the repository"""
    print("🔍 Testing APKMirror URL replacement with real examples\n")
    
    # Get actual current content from one of the files
    try:
        result = subprocess.run(['grep', '-n', 'youtube-19-43-41', '00-first-start.md'], 
                              capture_output=True, text=True)
        if result.stdout:
            print("📁 Found hardcoded versions in 00-first-start.md:")
            print(result.stdout)
        else:
            print("📁 No hardcoded 19-43-41 versions found (may already be updated)")
    except:
        print("📁 Could not check file content")
    
    # Test patterns we expect to find
    test_urls = [
        "https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-android-apk-download/",
        "https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-2-android-apk-download/",
        "youtube-19-43-41-release",
        "youtube-19-43-41-android"
    ]
    
    youtube_version = "20.12.46"
    youtube_version_dashed = youtube_version.replace('.', '-')
    
    print(f"\n🎯 Converting from old version patterns to: {youtube_version_dashed}\n")
    
    # Apply the same patterns as the main script
    apkmirror_patterns = [
        (r'youtube-\d+-\d+-\d+-release', f'youtube-{youtube_version_dashed}-release'),
        (r'youtube-\d+-\d+-\d+-android', f'youtube-{youtube_version_dashed}-android'),
        (r'youtube-\d+-\d+-\d+-\d+-android', f'youtube-{youtube_version_dashed}-2-android')
    ]
    
    for i, test_url in enumerate(test_urls, 1):
        print(f"Test {i}: {test_url}")
        
        updated_url = test_url
        for pattern, replacement in apkmirror_patterns:
            updated_url = re.sub(pattern, replacement, updated_url)
        
        if updated_url != test_url:
            print(f"   ✅ → {updated_url}")
        else:
            print(f"   ⚪ No change (pattern not matched)")
        print()

def test_version_conversion():
    """Test version format conversion"""
    print("🔄 Testing version format conversion:\n")
    
    test_versions = ["19.43.41", "20.12.46", "18.45.43", "21.01.23"]
    
    for version in test_versions:
        dashed = version.replace('.', '-')
        print(f"{version} → {dashed}")

if __name__ == '__main__':
    test_version_conversion()
    print()
    test_actual_urls()
