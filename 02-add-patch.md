# Add Patches Guide

## Preface

This is a guide for non-root users to add patches to ReVanced YouTube.

Issues like this can be solved: 

![content not available](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/screenshots/400-warn-new-ver-yt.jpg?raw=true)

## 1. Requirements

You need to have the following to follow this guide:

- An Android smartphone with
    - ARMv8 or x86 architecture *
    - Android 8 or later *
    - ≥1GB storage space

- About 15 minutes of time

Don't know what these are? Don't worry, we will check for the ones marked with (*) later in this guide.

## 2. Checking versions

We are going to start patching now, but first we need to check supported version of YouTube.

The latest supported YT version is:

```
19.43.41
```

[![It is 19.43.41](https://img.shields.io/badge/Latest%20Supported%20Version-19.43.41-ff0000?style=for-the-badge&logo=youtube)](https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-2-android-apk-download/)

as of 2025-01-20T07:34 UTC. Remember that, as we will use it very soon.

## 3. Getting the files ready

In this section, you can find the latest supported Revanced Manager, GmsCore and YouTube APK

1. Download and install the latest **stable** [ReVanced manager (RVM)](https://github.com/ReVanced/ReVanced-manager/releases/latest)
!!!
Download the .apk, not the source code. 
The latest stable version may differ from the one shown below.
!!!
==- Image for reference
![download manager](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/000-download_manager.jpg?raw=true)
!!!
Do **NOT** try to find the manager version shown in the image, it might be outdated.
!!!
===
2. Download and install the latest stable [GmsCore](https://github.com/ReVanced/GmsCore/releases/latest)
==- Image for reference
!!!
Download the .apk, not the source code. 
The latest stable version may differ from the one shown below.
!!!
![download GmsCore](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/010-download_GmsCore.jpg?raw=true)
===
3. Visit [APK mirror for YouTube APK](https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-43-41-release/youtube-19-43-41-2-android-apk-download/)
!!!warning Warning
**Do NOT install the downloaded YouTube APK.**
!!!
!!!warning Warning
**The YouTube from Google Play will NOT work.** You CANNOT patch the one from Google Play. Download the one from APK mirror.
!!!
4. Verify that the link actually links to **version 19.43.41**
!!!warning Warning
**Do NOT install the downloaded YouTube APK.**
!!!
5. Verify that it said "DOWNLOAD APK" not "DOWNLOAD APK BUNDLE"
=== Image for reference
![The one marked with a blue :icon-check: is the correct one](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/021-verify-apk-not-bundle.jpg?raw=true)
===
6. Download **but don't install** the YT APK
!!!warning Warning
**Do NOT install the downloaded YouTube APK.**
!!!

## 4. Checking compatibility

1. launch RVM. Ignore any updates it claimed it knew. You may not have the red shaded part, that's normal.
==- Image for reference
![launch rvm](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/040-first_launch_manager.jpg?raw=true)
===
2. Go to the settings tab and scroll down until you find "About"
==- Image for reference
![check about](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/050-check_about.jpg?raw=true)
===
3. Check that `Arch` had at least 1 entry that looks like `arm64-v8a`
4. If you only got something that said `armv7` or lower, you cannot patch it on your phone. Please patch it on another device or your PC.
5. If you got `armv8` or higher, you are probably fine
6. Check that your Android version is at least 8
7. If you only got something that said `7` or lower, you cannot patch it on your phone. Please patch it on another device or your PC.
8. If you made it here, you can probably patch on your phone with ReVanced manager

## 5. Select APK

1. Go to the Patcher tab and click "Select an application"
==- Image for reference
![select app](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/060-select_application.jpg?raw=true)
===
2. Select YT from the list as we are trying to make RYT
==- Image for reference
![select YT](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/070-select_YT.jpg?raw=true)
===
3. A window should pop up asking you to select from storage.
!!!danger If the window did not pop up...
You have a older manager version. Update your manager to at least version v1.0.0.
!!!
==- Image for reference
![feat not imp](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/080-select_from_storage.jpg?raw=true)
===
!!!warning 
If you did not select from storage, patching would fail.
!!!
4. Select the YouTube APK you just downloaded in section 3 step 3. It should have a recent date and a size of roughly 130MB.
==- Image for reference
![storage view](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/090-select_YT_apk.jpg?raw=true)
===
5. The green part should contain the date. I redacted it for privacy.
6. Check that you have the suggested/recommended version of YT
==- Image for reference
![check ver](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/100-check_version.jpg?raw=true)
===
7. If no, go back to [section 3](#3-getting-the-files-ready)
8. If yes, continue to the next section

## 6. Select patches

1. Click "Select patches"
2. In the select patches view, choose "Default" or "Recommended"
==- Image for reference
![default](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/110-select_default.jpg?raw=true)
===
3. You can scroll around and disable some patches. BUT don't disable any which you don't know the purpose of.
4. DO NOT ENABLE THE FOLLOWING PATCHES
    - Change package name
    - Enable Android debugging
    - Export all activities
    - Predictive back gesture
    - Remove screenshot restriction
    - Spoof wifi connections
5. You can disable the following patches safely. I have tested them:
    - Disable auto captions
    - Hide player overlay
    - Hide seekbar
    - Hide timestamp
    - Wide search bar
6. Make sure you enabled the following patches:
    - GmsCore Support
    - Spoof Video Streams
=== Image for reference
![GmsCore](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/300-GmsCore_support.jpg?raw=true)
![Spoof Video Streams](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/302-spoof_client.jpg?raw=true)
===
7. When you have finished, click "Done" on the bottom right
==- Image for reference
![click done](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/120-click_done.jpg?raw=true)
===
8. Continue to next section

## 7. Patching

1. Click patch on the bottom right
==- Image for reference
![click patch](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/130-go_patch.jpg?raw=true)
===
2. A new patch window should show up. Do **NOT** exit, switch to background, or force-stop ReVanced manager.
==- Image for reference
![dont exit](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/140-dont_exit.jpg?raw=true)
===
3. The process should take less than 5 minutes
4. If you see any warnings, check out [the debug guide](/troubleshoot/00-trouble-shooting.md)

## 8. Patching Done!

1. After patching is done, export the patched APK
==- Image for reference
![export and install](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/150-export_install.jpg?raw=true)
===
2. Install the patched APK
3. If that does not work, install [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) and use that to install instead
4. Keep calm, you don't need to patch again. Just use the exported one in Step 1

[![Star this repo if it helps you!](https://img.shields.io/github/stars/SodaWithoutSparkles/revanced-troubleshooting-guide?style=for-the-badge&logo=github)](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide)

