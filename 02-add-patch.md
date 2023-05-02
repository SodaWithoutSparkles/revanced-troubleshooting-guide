# Add Patches Guide

## Preface

This is a guide for non-root users to add patches to ReVanced YouTube.

Issues like this can be solved: ![content not available](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/screenshots/400-warn-new-ver-yt.jpg?raw=true)

## Requirements

You need to have the following to follow this guide:

- An Android smartphone with
    - android 8 or later
    - 1GB or more storage space
    - Previous ReVanced version
    - Patched ReVanced on the phone before

- About 15 minutes of time

## Terminology / short forms

Here are some terminology that this guide may use:

- launch: click the icon on your phone's desktop and open the app

To save time, this guide will use the following short forms

- YT: YouTube
- RV: ReVanced
- RVM: ReVanced manager
- RYT: ReVanced YouTube
- microG: Vanced microG

## Steps

### Part 0: Checking versions

The latest supported YT version is: 

```
18.15.40 
```

as of 2023-04-30T07:40 UTC. Remember that as we will use it very soon.

### Part 1: Getting the files ready

1. Download and uodate to the latest stable [ReVanced manager (RVM)](https://github.com/ReVanced/ReVanced-manager/releases/latest) if not yet
![download manager](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/000-download_manager.jpg?raw=true)
2. Visit [APK mirror for YouTube APK](https://www.apkmirror.com/apk/google-inc/youtube/)
3. Scroll down and find the _latest supported version_
4. Select the FULL APK, **not BUNDLE or SPLIT APK**
![select apk](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/020-choose_YT_apk.jpg?raw=true)
5. Download **but don't install** the YT APK
![download yt](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/030-download_YT_apk.jpg?raw=true)

### Part 2: Adding the patches

1. Go to Patcher tab and click "Select an application"
![select app](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/060-select_application.jpg?raw=true)
2. Select YT from the list as we are trying to update RYT
![select YT](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/070-select_YT.jpg?raw=true)
3. A window should pop up asking you to select from storage. If no, you are using a older manager version. Use at least 0.1.0
![feat not imp](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/080-select_from_storage.jpg?raw=true)
4. Select the APK you just downloaded in part 1 step 6, **NOT THE PATCHED ReVanced YT**. It should have an recent date and have a size roughly 130MB.
![storage view](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/090-select_YT_apk.jpg?raw=true)
5. The green part should contain the date. I redacted it for privacy.
6. Check that you have the suggested/recommended version of YT
![check ver](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/100-check_version.jpg?raw=true)
7. If no, go back to Part 1 step 2 
8. If yes, click "Select patches"
9. In the select patches view, choose add patches here
![default](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/110-select_default.jpg?raw=true)
10. You can scroll around and disable some patch. BUT don't disable ones not that you don't know what it does.
11. DO NOT ENABLE THE FOLLOWING PATCHES
    - Change package name
    - Enable android debugging
    - Export all activities
    - Predictive back gesture
    - Remove screenshot restriction
    - Spoof wifi connections
12. You can disable the following patches safely. I have tested them:
    - Disable auto captions
    - Hide player overlay
    - Hide seekbar
    - Hide timestamp
    - Wide search bar
14. Make sure you enabled the following patches:
    - Vanced MicroG Support
    - Spoof Signature Verification
    - Client Spoof
![microG](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/300-microg_support.jpg?raw=true)
![spoof sig](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/301-spoof_sig.jpg?raw=true)
![client spoof](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/302-spoof_client.jpg?raw=true)
14. When you have finished, click "Done" on the bottom right
![click done](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/120-click_done.jpg?raw=true)
15. Click patch on bottom right
![click oatch](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/130-go_patch.jpg?raw=true)
16. A new patch window should show up. Do **NOT** exit, switch to background, or force-stop ReVanced manager. 
![dont exit](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/140-dont_exit.jpg?raw=true)
17. The process should take less than 5 minutes
18. If you see any warnings, check out [the debug guide](/troubleshoot/00-trouble-shooting.md)
18. After patching is done, export the patched APK
![export and install](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/150-export_install.jpg?raw=true)
20. Install the patched APK
21. If that does not work, install [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) and use that to install instead
22. Keep calm, you don't need to patch again. Just use the exported one in step 18
