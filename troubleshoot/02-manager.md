# 2. ReVanced manager

Troubleshooting regarding ReVanced manager issues

## 2.1. ReVanced manager does not install

- Not enough storage space, check that you have ≥1GB to be on the safe side

- Bad APK, download again

## 2.2. What is the latest supported / suggested Youtube apk version?

In ReVanced manager > patcher > select application, it tells you the latest supported / suggested YouTube version to patch

## 2.3. Where can I get the YouTube APK?

https://www.apkmirror.com/apk/google-inc/youtube/

Make sure you got the version marked APK and nodpi, **not the one marked BUNDLE**

## 2.4. How to export keystore

This is a new feature from version 0.1.0. Go to ReVanced manager > settings > scroll down to import & export > export keystore

If you have an older version (≤0.0.57), you will need to go to `Android/data/app.revanced.manager.flutter/files` and get the keystore there.

## 2.5. How to import keystore

This is a new feature from version 0.1.0. Go to ReVanced manager > settings > scroll down to import & export > import keystore

If you have an older version (≤0.0.57), you will need to go to `Android/data/app.revanced.manager.flutter/files` and dump your keystore there.

## 2.6. Cannot update ReVanced manager

If you have manager version ≥0.1.0, follow the above steps on exporting the keystore. Then, install the new version and import the old keystore back in.

Delete existing ReVanced manager and install the new one.

## 2.7. Cannot select YouTube APK to patch

If you have manager version ≥0.1.0, follow the above steps on exporting the keystore. Then, install the new version and import the old keystore back in.

Delete existing ReVanced manager and install the new one.

## 2.8. ReVanced manager still shows update available when I am on latest?

*Deleted as outdated*

==- Orginal answer
https://github.com/revanced/revanced-manager/issues/805

TL;DR: that is a known harmless bug, ignore it and don't update
===

## 2.9. Non-root install not possible?

Select `GmsCore support` patch in the patches selection menu. 

If you cannot find it, use the search function and search for "microg". If it is greyed out, it means that you have used an incompatible version.

![non-root install not possible](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/02-manager/09.jpg?raw=true)

## 2.10. Cannot find/select patch \<insert patch name here\>?

Your selected app version was incompatible. Use the Suggested version.

## 2.11. What patch should I select?

Select the default/recommended ones. When you are in the select patches window, you can click the "default" or "recommended" button on the top. You can review the defaults, but don't exclude patches that you don't know what it means. It is probably needed. Don't worry about functions that you may not like, you can disable them in-app later.

DO NOT SELECT ANY OF THE FOLLOWING PATCHES OR YOU WILL RISK HAVING ISSUES: 

- Change package name
- enable **android** debugging
- export all activities
- Predictive back gesture
- Remove screenshot restriction
- Spoof wifi connections

If you don't know where to start but just want to remove some patches, you can safely remove these. I did not select the following patches: 

- Disable auto captions
- Hide player overlay
- Hide seekbar
- Hide timestamp
- Wide search bar

## 2.12. Cannot select patch?

Click the "Selected Patches" box

## 2.13. Import patches selection

Go to ReVanced manager > settings > scroll down to import & export > Import patches selection. Select the downloaded JSON file just now. You now have the same set of patches mine.

## 2.14. ReVanced manager aborting / exit code 135 / exit code 139 / ARMv7 devices

If you see the text "exit code = 135" or "exit code = 139", then your devices architecture is not supported. 

You are probably using ARMv7. The supported architectures are ARMv8 or above.

Please patch on an another device or on your PC.

## 2.15. ReVanced manager does not select APK

Symptoms: after clicking select an application > YouTube, nothing happened and it goes back to the patcher tab without selecting any apps

You probably are not using the stable version of ReVanced manager. Do the following to get it fixed: 
1. Follow [section 2.4](/troubleshoot/02-manager/04/) to export the keystore
2. Delete existing ReVanced manager, and the ReVanced manager APK file you downloaded before.
3. Install the latest **stable** version of ReVanced manager [here](https://github.com/revanced/revanced-manager/releases/latest). Do not use the one you downloaded before.
4. Follow [section 2.5](/troubleshoot/02-manager/05/) to import the keystore

## 2.16 ReVanced manager patch failed / patch not applied

- Non-recommended / non-default patches used
    - Reset to default patches
- Split-apk used
    - Follow the [guide](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/step-by-step/00-preface/) again
    - It will guide you on how to differentiate between split and non-split
- Non-official patch sources
    - Read more about that [here](/troubleshoot/18.md)
- "Work profile"
    - ReVanced might not patch if there is a separate profile
    - Solution: Try another phone
    - Thanks bjhiltbrand#4379 for testing
- "Right-to-left" device language used
    - Manager sometimes get confused when a right-to-left language is used
    - Go to phone settings and change the language to English and try again
- ReVanced manager was confused
    - manager > settings > _scroll down_ > delete temporary files
    - If this did not work, try using the [generic debug methods](/troubleshoot/04-generic/) on ReVanced manager
    - If it still did not work, re-install ReVanced manager:
        1. Follow [section 2.4](/troubleshoot/02-manager/04/) to export the keystore
        2. Delete existing ReVanced manager, and the ReVanced manager APK file you downloaded before.
        3. Install the latest **stable** version of ReVanced manager [here](https://github.com/revanced/revanced-manager/releases/latest). Do not use the one you downloaded before.
        4. Follow [section 2.5](/troubleshoot/02-manager/05/) to import the keystore
    - If that still did not work, follow the above steps again but DON'T import the keystore

![patch failed to apply](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/02-manager/16.jpg?raw=true)

## 2.17 Patched apk does not install

Refer to [section 3.3](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/troubleshoot/03-youtube/03/)

## 2.18 Regarding ReVanced Extended patches / InvocationTargetExceptions

Using ReVanced Extended patches is the most likely cause for InvocationTargetException.

ReVanced Extended patches which are **nonofficial, unsupported, and discontinued**, you should stop using them.

You can reset to official patch sources by: 

1. Going to manager settings > sources
2. Click the reset icon at top right of the window
3. Click ok 

If that doesn't work solve the issue: 

1. **Clear all of manager's data first**
2. Uninstall manager
3. Download the latest version [here](https://github.com/ReVanced/revanced-manager/releases/latest)

