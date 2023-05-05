# First Start Guide

## Preface

This is a first-start guide for starters to patch a copy of ReVanced YouTube.

This guide is for non-root users, but it should still work for root users.

Remember: There is **NO** way to *download* ReVanced. To prevent the distribution of copyrighted materials, you need to "make" ReVanced yourself. **ANY place where you can _download_ ReVanced YouTube is either lying or contains malware**.

## Requirements

You need to have the following to follow this guide:

- An Android smartphone with
    - ARMv8 or x86 architecture *
    - Android 8 or later *
    - ≥1GB storage space

- About 15 minutes of time

Don't know what these are? Don't worry, we will check for the ones marked with (*) later in this guide.


## Terminology / short forms

Here are some terminologies that this guide may use:

- launch: click the icon on your phone's desktop and open the app

To save time, this guide will use the following short forms

- YT: YouTube
- RV: ReVanced
- RVM: ReVanced manager
- RYT: YouTube ReVanced
- microG: Vanced microG

## Steps

### Part 0: Checking versions

The latest supported YT version is: 

```
18.16.37 
```

as of 2023-05-05T14:15 UTC. Remember that, as we will use it very soon.

### Part 1: Getting the files ready

1. Download and install the latest stable [ReVanced manager (RVM)](https://github.com/ReVanced/ReVanced-manager/releases/latest)
![download manager](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/000-download_manager.jpg?raw=true)
2. Download and install the latest stable [Vanced microG (microG)](https://github.com/TeamVanced/VancedMicroG/releases/tag/v0.2.24.220220-220220001)
![download microG](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/010-download_microg.jpg?raw=true)
3. Visit [APK mirror for YouTube APK](https://www.apkmirror.com/apk/google-inc/youtube/)
4. Scroll down and find the _latest supported version_
5. Select the FULL APK, **not BUNDLE or SPLIT APK**
![select apk](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/020-choose_YT_apk.jpg?raw=true)
6. Download **but don't install** the YT APK
![download yt](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/030-download_YT_apk.jpg?raw=true)

### Part 2: Checking compatibility

1. launch RVM. Ignore any updates it claimed it knew. You may not have the red shaded part, that's normal.
![launch rvm](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/040-first_launch_manager.jpg?raw=true)
2. Go to the settings tab and scroll down until you find "About"
![check about](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/050-check_about.jpg?raw=true)
3. Check that `Arch` had at least 1 entry that looks like `arm64-v8a`
4. If you only got something that said `armv7` or lower, you cannot patch it on your phone. Please patch it on another device or your PC.
5. If you got `armv8` or higher, you are probably fine
6. Check that your Android version is at least 8
7. If you only got something that said `7` or lower, you cannot patch it on your phone. Please patch it on another device or your PC.
8. If you made it here, you can probably patch on your phone with ReVanced manager

### Part 3: Patching

1. Go to the Patcher tab and click "Select an application"
![select app](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/060-select_application.jpg?raw=true)
2. Select YT from the list as we are trying to make RYT
![select YT](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/070-select_YT.jpg?raw=true)
3. A window should pop up asking you to select from storage. If not, you are using an older manager version. Use at least 0.1.0
![feat not imp](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/080-select_from_storage.jpg?raw=true)
4. Select the APK you just downloaded in part 1 step 6. It should have a recent date and a size of roughly 130MB.
![storage view](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/090-select_YT_apk.jpg?raw=true)
5. The green part should contain the date. I redacted it for privacy.
6. Check that you have the suggested/recommended version of YT
![check ver](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/100-check_version.jpg?raw=true)
7. If no, go back to Part 1 step 3
8. If yes, click "Select patches"
9. In the select patches view, choose "Default" or "Recommended"
![default](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/110-select_default.jpg?raw=true)
10. You can scroll around and disable some patches. BUT don't disable any which you don't know the purpose of.
11. DO NOT ENABLE THE FOLLOWING PATCHES
    - Change package name
    - Enable Android debugging
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
13. When you have finished, click "Done" on the bottom right
![click done](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/120-click_done.jpg?raw=true)
14. Click patch on the bottom right
![click patch](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/130-go_patch.jpg?raw=true)
15. A new patch window should show up. Do **NOT** exit, switch to background, or force-stop ReVanced manager. 
![dont exit](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/140-dont_exit.jpg?raw=true)
16. The process should take less than 5 minutes
17. If you see any warnings, check out [the debug guide](/troubleshoot/00-trouble-shooting.md)
18. After patching is done, export the patched APK
![export and install](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/150-export_install.jpg?raw=true)
19. Install the patched APK
20. If that does not work, install [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) and use that to install instead
21. Keep calm, you don't need to patch again. Just use the exported one in Step 18
