#!/usr/bin/python3

"""
Test the dashed version replacement logic
"""

import re

def test_dashed_replacement():
    # Test content with various APKMirror URL patterns
    test_content = '''
[![It is ${YT_VERSION}](https://img.shields.io/badge/Latest%20Supported%20Version-${YT_VERSION}-ff0000?style=for-the-badge&logo=youtube)](https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-android-apk-download/)

3. Visit [APK mirror for YouTube APK](https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-2-android-apk-download/)

Another link: https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-android-apk-download/
'''

    youtube_version = "20.12.46"
    youtube_version_dashed = youtube_version.replace('.', '-')
    
    print(f"Original version: {youtube_version}")
    print(f"Dashed version: {youtube_version_dashed}")
    print("\nOriginal content:")
    print(test_content)
    
    # Apply the same logic as the main script
    content = test_content
    
    # Replace placeholders first
    content = content.replace('${YT_VERSION}', youtube_version)
    
    # Handle APKMirror URL updates
    apkmirror_patterns = [
        (r'youtube-\d+-\d+-\d+-release', f'youtube-{youtube_version_dashed}-release'),
        (r'youtube-\d+-\d+-\d+-android', f'youtube-{youtube_version_dashed}-android'),
        (r'youtube-\d+-\d+-\d+-\d+-android', f'youtube-{youtube_version_dashed}-2-android')
    ]
    
    for pattern, replacement in apkmirror_patterns:
        old_content = content
        content = re.sub(pattern, replacement, content)
        if content != old_content:
            print(f"\nReplaced pattern: {pattern}")
            print(f"With: {replacement}")
    
    print("\nFinal content:")
    print(content)

if __name__ == '__main__':
    test_dashed_replacement()
