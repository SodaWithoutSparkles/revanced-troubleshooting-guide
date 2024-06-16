# ReVanced Setup Guide

This is a first-start guide for starters to patch a copy of ReVanced YouTube.

This guide is for non-root users. For root users, visit the [other resources section](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/#other-resources) for hokora's guide.

![Preview](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/step-by-step/00.jpg)

In this guide, we will:

- Check requirements and latest supported versions
- Get the tools we need to "make" revanced yourself
- Guide you step-by-step on how to select the right "features"
- Provide solution on what to do when it does not work

!!! Remember
There is **NO** way to _download_ ReVanced. To prevent the distribution of copyrighted materials, you need to "make" ReVanced yourself. 
**ANY place where you can _download_ YouTube ReVanced is either lying or contains malware.**
!!!

All ok? click the next page button.

==- Related Keywords
- How to download revanced
- download revanced
- revanced download
- get revanced
- install revanced
===

## 1. Requirements

You need to have the following to follow this guide:

- An Android smartphone with
    - ARMv8 or x86 architecture *
    - Android 8 or later *
    - ≥1GB storage space

- About 15 minutes of time (depends on your device)
    - speedrun current record: 4:15
    - flagship: estimated 5 ~ 10 min
    - mid-tier: estimated 10 ~ 15 min
    - low-tier: estimated 15 ~ 35 min

Don't know what these are? Don't worry, we will check for the ones marked with (*) later in this guide.

## 2. Checking versions

We are going to start patching now, but first we need to check supported version of YouTube.

The latest supported YT version is:

```
19.16.39
```

[![It is 19.16.39](https://img.shields.io/badge/Latest%20Supported%20Version-19.16.39-ff0000?style=for-the-badge&logo=youtube)](https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-16-39-release/youtube-19-16-39-android-apk-download/)

as of 2024-06-16T18:36 UTC. Remember that, as we will use it very soon.

==- How to check manually
1. Go to the official [ReVanced patches website](https://revanced.app/patches?pkg=com.google.android.youtube)
2. Select `com.google.android.youtube` if not already selected
3. Find the 🎯 icon for the latest supported version of each patch
4. The version you should use is the one that has the lowest version number to ensure maximum compatibility
===

## 3. Getting the files ready

In this section, you can find the latest supported Revanced Manager, GmsCore and YouTube APK.

1. Download and install the latest **stable** [ReVanced manager (RVM)](https://github.com/ReVanced/ReVanced-manager/releases/latest) to your phone
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
2. Download and install the latest stable [GmsCore](https://github.com/ReVanced/GmsCore/releases/latest) to your phone
==- Image for reference
!!!
Download the .apk, not the source code. 
The latest stable version may differ from the one shown below.
!!!
![download GmsCore](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/010-download_GmsCore.jpg?raw=true)
===
3. Visit [APK mirror for YouTube APK](https://www.apkmirror.com/apk/google-inc/youtube/youtube-19-16-39-release/youtube-19-16-39-android-apk-download/)
!!!warning
**Do NOT install the downloaded YouTube APK.**
!!!
!!!warning
**The YouTube from Google Play will NOT work.** You CANNOT patch the one from Google Play. Download the one from APK mirror.
!!!
4. Verify that the link actually links to **version 19.16.39**
5. Verify that it said "DOWNLOAD APK" not "DOWNLOAD APK BUNDLE"
=== Image for reference
![The one marked with a blue :icon-check: is the correct one](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/021-verify-apk-not-bundle.jpg?raw=true)
===
6. Download **but don't install** the YT APK

## 4. Checking compatibility

We are going to check if this device is supported.

1. launch RVM. Ignore any updates it claimed it knew.
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

==- What does `arch` mean? Why is `armv7` not supported?
`arch` is the architecture of your CPU. In layman terms, it is "the language of the CPU", if you don't know that language, you cannot communicate with that CPU. 

The ReVanced team will move to `arsclib` soon™, which supports `armv7`. For now, you can patch on a computer with `revanced-cli` or `revanced-builder` instead.
===

## 5. Select APK

1. In ReVanced manager, go to the Patcher tab and click "Select an application"
==- Image for reference
![select app](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/060-select_application.jpg?raw=true)
===
2. Click the "Storage" button at the bottom right
==- Image for reference
![select YT](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/081-select_from_storage.jpg?raw=true)
===
!!!warning 
If you did not select from storage, patching would fail.
!!!
3. Select the YouTube APK you just downloaded in [Part 3](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/step-by-step/03-get-files/). It should have a recent date and a size of roughly 130MB.
==- Image for reference
![storage view](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/090-select_YT_apk.jpg?raw=true)
===
4. The green part should contain the date. I redacted it for privacy.
5. Check that you have the suggested/recommended version of YT
==- Image for reference
![check ver](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/100-check_version.jpg?raw=true)
===
6. If no, go back to [Part 3](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/step-by-step/03-get-files/)
7. If yes, continue to the next page

## 6. Select patches

The manager now automatically select patches for first time users. Go to the next section IF you are patching for the first time.

!!!danger
Changing the default patches may break things. It is NOT recommended for first time users to change the default selection.
!!!

==- Last time I patched un-successfully / Re-patching / not patching for the first time
1. Click "Select patches" or "Selected patches"
2. In the select patches view, choose "Default" or "Recommended"
![default](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/110-select_default.jpg?raw=true)
!!!danger
Do NOT disable the default patches unless you are instructed to do so. Especially, do **NOT** disable these two:
- `GmsCore Support`
- `Client Spoof`
!!!
!!!warning
Modifying (add/remove) the default patches may cause unintended consequences. 
Do **NOT** try to change them unless you know what you are doing.
!!!
3. Click "Done" on the bottom right, do **NOT** change the default patches unless instructed.
===

==- I want to change the default selection
!!!warning
Modifying the default patches (add/remove) may cause unintended consequences. Do **NOT** try to change them unless you are absolutely sure what you are doing.
!!!
1. Click "Select patches"
2. In the select patches view, choose "Default" or "Recommended"
![default](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/110-select_default.jpg?raw=true)
!!!danger
Do NOT disable the default patches unless you know what you are doing. Especially, do **NOT** disable these two:
- `GmsCore Support`
- `Client Spoof`
!!!
3. You can scroll around and disable some patches. BUT don't disable any which you don't know the purpose of.
4. DO NOT ENABLE THE FOLLOWING PATCHES
    - `Change package name`
    - `Enable Android debugging`
    - `Export all activities`
    - `Predictive back gesture`
    - `Remove screenshot restriction`
    - `Spoof wifi connections`
5. You can disable the following patches safely. I have tested them:
    - `Disable auto captions`
    - `Hide player overlay`
    - `Hide seekbar`
    - `Hide timestamp`
    - `Wide search bar`
6. DO **enable** the following patches. They are critical.
    - `GmsCore Support` (unless your phone is rooted)
        - _if you don't know what root is, you are probably not rooted_
    - `Client Spoof` (must enable)
6. When you have finished, click "Done" on the bottom right
![click done](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/120-click_done.jpg?raw=true)

===

## 7. Patching

1. Click patch on the bottom right
==- Image for reference
![click patch](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/130-go_patch.jpg?raw=true)
===
2. A new patch window should show up. Do **NOT** exit, switch to background, or force-stop ReVanced manager.
==- Image for reference
![dont exit](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/140-dont_exit.jpg?raw=true)
===
3. The process should take about 5 ~ 10 minutes
!!!
The speed of patching depends on phone performance. Some reported that it took 35 minutes with a very old phone.
!!!
4. If you see any warnings, check out [the debug guide](/troubleshoot/00-trouble-shooting.md)

## 8. Patching Done!

1. After patching is done, export the patched APK for backup.
==- Image for reference
![export and install](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/150-export_install.jpg?raw=true)
===
2. Install the patched APK
!!!
Install it in the patching complete screen. You don't need to install the exported one.
!!!
3. If that does not work, install [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) and use that to install instead
4. Keep calm, you don't need to patch again. Just use the exported one in Step 1

[![Star this repo if it helps you!](https://img.shields.io/github/stars/SodaWithoutSparkles/revanced-troubleshooting-guide?style=for-the-badge&logo=github)](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide)

