# ReVanced Trouble​shooting Guide
Troubleshooting guide for Revanced

This is a guide on solving common issues when using ReVanced YT and ReVanced Manager. If you find something missing,  open a new issue and I would add it.

## 1. General

### 1.1. How to install ReVanced YouTube?

No. You don't download an APK and install it. This is to prevent distribution of copyrighted materials. Instead you "make" it yourself. Checkout [this guide by Hokora Yinphine MPP#6969 on discord](https://hokorayinphinempp.github.io/obsidian-git-sync/Revanced/1%20Start%20Here%21/Revanced%20Start/) or [this guide by me](first-start-guide.md) or [this guide](https://www.reddit.com/r/revancedapp/comments/xlcny9/revanced_manager_guide_for_dummies/) for more detailed steps.

### 1.2. Where can I get ReVanced manager?

https://github.com/revanced/revanced-manager/releases/latest

### 1.3. Where can I get Vanced microG?

https://github.com/TeamVanced/VancedMicroG/releases/tag/v0.2.24.220220-220220001

### 1.4. What is the latest YouTube version supported? 

18.45.43 as of 2024-01-20T16:12 UTC. You can check it in ReVanced manager

### 1.5. Is ReVanced related to Vanced?

Nope. 

### 1.6. How can I support Revanced?

If you can, donate to the ReVanced team at either:

- [Liberapay](https://liberapay.com/ReVanced/donate)
- [GitHub Sponsors](https://github.com/sponsors/ReVanced)

If you can't donate, you can also contribute to the development by:

- [Translating Revanced](https://crowdin.com/project/revanced)

### 1.7. I think I saw a bug

You can post your bug on [Reddit](https://www.reddit.com/r/revancedapp) first to confirm if this is indeed a bug and if anyone else has reported it. Or you can go to the [ReVanced discord](https://discord.gg/revanced) to ask there. The ReVanced development team regularly hangs out there. **DO NOT POST YOUR SUPPORT REQUEST IN CHAT.** Post them in \## general > support instead. Remember to add a tag. You can do so on the bottom left.

After that you can go to the relevant Github issues page to file a bug report.

- [ReVanced patches](https://github.com/revanced/revanced-patches/issues/new?template=bug-issue.yml)
- [ReVanced manager](https://github.com/revanced/revanced-manager/issues/new?template=bug-issue.yml)

## 2. ReVanced manager

### 2.1. ReVanced manager does not install

- Not enough storage space, check that you have ≥1GB to be on the safe side

- Bad APK, download again

- Signature mismatch, delete old manager and install (WARNING: this deletes keystore, you may want to export it first)

### 2.2. What is the latest supported / suggested Youtube apk version?

In ReVanced manager > patcher > select application, it tells you the latest supported / suggested YouTube version to patch

### 2.3. Where can I get the YouTube APK?

https://www.apkmirror.com/apk/google-inc/youtube/

Make sure you got the version marked APK and nodpi, **not the one marked BUNDLE**

### 2.4. How to export keystore

This is a new feature from version 0.1.0. Go to ReVanced manager > settings > scroll down to import & export > export keystore

If you have an older version (≤0.0.57), you will need to go to `Android/data/app.revanced.manager.flutter/files` and get the keystore there.

### 2.5. How to import keystore

This is a new feature from version 0.1.0. Go to ReVanced manager > settings > scroll down to import & export > import keystore

If you have an older version (≤0.0.57), you will need to go to `Android/data/app.revanced.manager.flutter/files` and dump your keystore there.

### 2.6. Cannot update ReVanced manager

Delete existing ReVanced manager and install the new one. If you have manager version ≥0.1.0, follow the above steps on exporting the keystore. Then, install the new version and import the old keystore back in.

### 2.7. Cannot select YouTube APK to patch

Delete existing ReVanced manager and install the new one. If you have manager version ≥0.1.0, follow the above steps on exporting the keystore. Then, install the new version and import the old keystore back in.

### 2.8. ReVanced manager still shows update available when I am on latest?

https://github.com/revanced/revanced-manager/issues/805

TL;DR: that is a known harmless bug, ignore it and don't update

### 2.9. Non-root install not possible?

Select `vanced microG support` patch in the patches selection screen. If you cannot find it, use the search function and search for "microg". If you still cannot find it, you are using a non-supported YT version.

### 2.10. Cannot find patch \<insert patch name here\>?

Your selected app version was incompatible. Use the Suggested version.

### 2.11. What patch should I select?

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

### 2.12. Cannot select patch?

Click the "Selected Patches" box

### 2.13. Import patches selection

If you don't know what you should select, or want to use the same set of patches as mine, you can download the patches selection. [!file Patches Selection](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/selected_patches_2023-04-30.json).

Then go to ReVanced manager > settings > scroll down to import & export > Import patches selection. Select the downloaded JSON file just now. You now have the same set of patches mine.

### 2.14. ReVanced manager aborting / exit code 135 / exit code 139 / ARMv7 devices

If you see the text "exit code = 135" or "exit code = 139", then your devices architecture is not supported. 

You are probably using ARMv7. The supported architectures are ARMv8 or above.

Please patch on an another device or on your PC.

### 2.15. ReVanced manager does not select APK

Symptoms: after clicking "select an application" > "YouTube", nothing happened and it goes back to the patcher tab without selecting any apps

You probably are not using the stable version of ReVanced manager. Do the following to get it fixed: 
1. Follow [section 2.4](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/troubleshoot/02-manager/04/) to export the keystore
2. Delete existing ReVanced manager
3. Install the latest **stable** version of ReVanced manager [here](https://github.com/revanced/revanced-manager/releases/latest)
4. Follow [section 2.5](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/troubleshoot/02-manager/05/) to import the keystore

### 2.16 ReVanced manager patch failed / patch not applied

DO NOT SELECT ANY OF THE FOLLOWING PATCHES OR YOU WILL RISK HAVING ISSUES: 

- Change package name
- enable **android** debugging
- export all activities
- Predictive back gesture
- Remove screenshot restriction
- Spoof wifi connections

## 3. ReVanced Youtube

### 3.1. Unable to open/launch ReVanced YouTube

Probably one of the following: 

- split APK is used to patch
    - patch again using the full APK
- non-recommended patches
    - patch again with the default/recommended patches
- You exited ReVanced manager when patching
    - Don't do that. Repatch again.

### 3.2. Video playback issues / buffers / buggy / content not available

Include `client spoof` patch and patch again. (_`spoof signature verification` was merged into `client spoof`_)

If you cannot find them, you probably patched an unsupported YT version.

### 3.3. App not installed / Installation is blocked / `install_failed_verification_failure`

Probably one of the following reason

- Signature mismatch between existing ReVanced install
    - Delete that existing install
- Google play protect blocked it
    - when the play protect window popped up, click "learn more" and "install anyway"
- You exited ReVanced manager when patching
    - Don't do that. Repatch again.
- Split APK used
    - repatch with non-split APK / full apk
- Artifacts left from previous install / the uninstall was not done cleanly
    - This could only happen if you have installed and uninstalled ReVanced previously
    - You will need to use ADB to fully remove the old install.
    - You can find a guide [here](/03-adb-remove.md)

### 3.4. Video turns very dark in fullscreen

Try swiping up on the left side of your screen. This feature is called swipe brightness control. Swipe down all the way and it would use auto-brightness. You can also swipe to control volume on the right.

You can disable this under ReVanced YT settings > ReVanced > Interaction > Swipe Controls

### 3.5. No internet connection

Did you change your google password? Anyway, go to system settings > accounts > **vanced microG** > delete/logout account. Don't worry, this will not remove your google account on your device, just remove the one used by microG (hence ReVanced). 

### 3.6. Shorts button missing?

Disable: ReVanced YT settings > ReVanced > Layout > Hide Shorts, Hide Shorts button

### 3.7. Video UI looks strange when watching playlist

Disable: ReVanced YT settings > ReVanced > Layout > Hide fullscreen panels

### 3.8. Cast button missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide cast button

Note that casting is currently broken. You need to use TV code to pair first

### 3.9. Caption button missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide caption button

### 3.10. End screen cards missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide end screen cards

If that does not work, then it is caused by a side effect of spoofing signatures. For more information, see [revanced-patches github issues #1752](https://github.com/revanced/revanced-patches/issues/1752)

### 3.11. Captions/subtitles in the wrong place

Known issue. It would be fixed automatically when you watch the second video. If it still stays on the top, repatch and include the latest patches. Keep in mind that YouTubers can configure subtitle positions so it might be intended for the subtitles to be on the top.

https://github.com/revanced/revanced-patches/issues/2003

### 3.12. Ambient mode / "glow around video" missing

Turn the function off and on again. Seriously, this fixed it.

### 3.13. Some buttons next to like/dislike missing 

Disable: ReVanced YT settings > ReVanced > Layout > Hide action buttons > All toggles listed

### 3.14. Remix/share/thanks/shop/clip buttons missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide action buttons > Hide all other action buttons

### 3.15. Youtube autoplays the next video

1. Disable: ReVanced YT settings > ReVanced > Layout > Hide autoplay button
2. Restart Youtube ReVanced
3. Play any video, in the video player, turn off autoplay
4. Enable: ReVanced YT settings > ReVanced > Layout > Hide autoplay button
5.  Restart Youtube ReVanced

### 3.16. \<insert name here\> is missing

It is probably in ReVanced YT settings > ReVanced > Layout. Scroll a bit and see if you can find it.

### 3.17. There are two copy buttons?

One is for copy the video URL, another one does the same but adds a timestamp, so people can click on that link and jump to that exact second.

You can disable one or both under ReVanced YT settings > ReVanced > Interactions > Copy video URL settings

### 3.18. `org.schabi.newpipe` is not installed / unable to download video

Install it at https://github.com/TeamNewPipe/NewPipe/releases/latest

Or alternatively you can use Seal instead of newpipe. Go install Seal [here](https://github.com/JunkFood02/Seal/releases/latest), then change ReVanced > ReVanced settings > Interaction > Download settings > Downloader Package name to this:

```
com.junkfood.seal
```

### 3.19. How can I download a video?

Use the download button inside the video player

### 3.20. Buttons overlapping

https://github.com/revanced/revanced-patches/issues/387

### 3.21. Title overlapping with buttons

https://github.com/revanced/revanced-patches/issues/455

### 3.22. Casting to TV have ads

Casting to TV is different. ReVanced YT does not handle the video stream, it basically tells the TV: go and play that video with this link. So you will need a ad-free YouTube TV client. You can get one [here](https://github.com/yuliskov/SmartTubeNext). Note that SmartTubeNext is not developed and not affiliated in any way with the ReVanced team.

### 3.23. SponsorBlock does not work

SponsorBlock is a community project. There might be no marked sponsors yet because

- The video was too new
- Nobody uploaded/marked any segments

Or it might also be that the SponsorBlock server is down. Wait a few minutes and try again. You can check the status at [here](https://status.sponsor.ajay.app/).

### 3.24. Dislike button shows nothing

Possible reasons include: 

- Return Youtube Dislike server was down
- API timeout, try again later

### 3.25. Dislike button said hidden

The YouTuber opted-out from the Return Youtube Dislike project

### 3.26. How to auto-skip sponsor segments?

ReVanced setting > SponsorBlock > scroll down > Change segment behabior > select category > skip automatically
