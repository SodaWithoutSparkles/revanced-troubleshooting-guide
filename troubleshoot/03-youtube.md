# 3. ReVanced YouTube

Troubleshooting regarding YouTube ReVanced issues

## 3.1. Unable to open/launch ReVanced YouTube / ReVanced crashing

Probably one of the following: 

- split APK is used to patch
    - Patch again using the full APK
- non-recommended patches/version
    - Patch again with the default/recommended patches/version
    - [Refer to section 2.11 (What patch should I select?)](/troubleshoot/02-manager/11/)
- GmsCore not installed
    - Install it [here](https://github.com/ReVanced/GmsCore/releases/latest)
- You exited ReVanced manager when patching
    - Don't do that. Repatch again.
- There were errors during patching
    - Look at the patching log for `failed`
    - It should be at the first word of the line
    - if so, look at the [patch not applied guide](/troubleshoot/02-manager/16/)

## 3.2. Video playback issues / buffers / buggy / content not available

Patch again with the `client spoof` patch. (_`spoof signature verification` was merged into `client spoof`_)

![infinite loading](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/02.png?raw=true)

The process is the same as updating ReVanced, which you can find a guide [here](/07-update-revanced.md)

If you cannot find them, you probably patched an unsupported YT version or used non-default patch sources

keyword: 
- video stops at spectific time
- video stops at 1 minute
## 3.3. App not installed / Installation is blocked / `install_failed_verification_failure`

Probably one of the following reason

- Signature mismatch between existing ReVanced install
  - Delete that existing install
- Google play protect blocked it
  - when the play protect window popped up, click "learn more" and "install anyway"
- You forgot the GmsCore patch
  - Add the `GmsCore support` patch and try again
- You clicked the wrong apk
  - Double-check that you selected the patched instead of the raw source apk
- There were errors during patching
  - Look at the patching log for `failed`
  - It should be at the first word of the line
  - if so, look at the [patch not applied guide](/troubleshoot/02-manager/16/)
- You exited ReVanced manager when patching
  - Don't do that. Repatch again.
- Split APK used
  - repatch with non-split APK / full apk
- Installed in "secure folder"
  - Check if "secure folder" is enabled
  - If so, see if the ReVanced is installed in the "secure folder"
  - If so, delete the install there and try again
- Some unknown reasons
  - We need more information to know what went wrong
  - Install SAI ([Play store](https://play.google.com/store/apps/details?id=com.aefyr.sai), [apkmirror](https://www.apkmirror.com/apk/polychromaticfox/split-apks-installer-sai/)) on your phone
  - After patching again, click the three-dots menu and export the APK
  - Go into SAI and select the APK you just exported
    - Look at the install failure message and search it on Google
- Artifacts left from previous install / the uninstall was not done cleanly
  - This could only happen if you have installed and uninstalled ReVanced previously
  - You will need to use ADB to fully remove the old install.
  - You can find a guide [here](/03-adb-remove.md)

![App not installed](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/03.jpg?raw=true)

## 3.4. Video turns very dark in fullscreen

Try swiping up on the left side of your screen. This feature is called swipe brightness control. Swipe down all the way and it would use auto-brightness. You can also swipe to control volume on the right.

You can disable this under ReVanced YT settings > ReVanced > Interaction > Swipe Controls

## 3.5. No internet connection

Did you change your google password? Anyway, go to system settings > accounts > Google (blue icon with lowercase g) > delete/logout account. Don't worry, this will not remove your google account on your device, just remove the one used by GmsCore (hence ReVanced). 

## 3.6. Shorts button missing?

Disable: ReVanced YT settings > ReVanced > Layout > Navigation buttons > Hide Shorts button

## 3.7. Video UI looks strange when watching playlist

Disable: ReVanced YT settings > ReVanced > Layout > Hide fullscreen panels

## 3.8. Cast button missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide cast button

Note that casting is currently broken. You need to use TV code to pair first

## 3.9. Caption button missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide caption button

## 3.10. End screen cards missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide end screen cards

If that does not work, then it is caused by a side effect of spoofing signatures. For more information, see [revanced-patches github issues #1752](https://github.com/revanced/revanced-patches/issues/1752)

## 3.11. Captions/subtitles in the wrong place

It was fixed in patches version 2.172.0. Repatch your YouTube ReVanced with latest default patches. Keep in mind that YouTubers can configure subtitle positions so it might be intended for the subtitles to be on the top.

https://github.com/revanced/revanced-patches/issues/2003

## 3.12. Ambient mode / "glow around video" missing

Turn the function off and on again. Seriously, this fixed it.

Or you have battery saving mode turned ON, and YouTube disables ambient mode. Blame YouTube ¯\\_(ツ)\_/¯

![Ambient mode settings](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/12.jpg?raw=true)

## 3.13. Some buttons next to like/dislike missing 

Disable: ReVanced YT settings > ReVanced > Layout > Hide action buttons > All toggles listed

## 3.14. Remix/share/thanks/shop/clip buttons missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide action buttons > Hide all other action buttons

## 3.15. Youtube autoplays the next video

1. Disable: ReVanced YT settings > ReVanced > Layout > Hide autoplay button
2. Restart Youtube ReVanced
3. Play any video, in the video player, turn off autoplay
4. Enable: ReVanced YT settings > ReVanced > Layout > Hide autoplay button
5.  Restart Youtube ReVanced

## 3.16. \<insert name here\> is missing

It is probably in ReVanced YT settings > ReVanced > Layout. Scroll a bit and see if you can find it.

## 3.17. There are two copy buttons?

One is for copy the video URL, another one does the same but adds a timestamp, so people can click on that link and jump to that exact second.

You can disable one or both under ReVanced YT settings > ReVanced > Interactions > Copy video URL settings

## 3.18. `org.schabi.newpipe` is not installed / unable to download video

Install it at https://github.com/TeamNewPipe/NewPipe/releases/latest

Or alternatively you can use Seal instead of newpipe. Go install Seal [here](https://github.com/JunkFood02/Seal/releases/latest), then change ReVanced > ReVanced settings > Interaction > Download settings > Downloader Package name to this:

```
com.junkfood.seal
```

## 3.19. How can I download a video?

Use the download button inside the video player

## 3.20. Buttons overlapping

https://github.com/revanced/revanced-patches/issues/387

## 3.21. Title overlapping with buttons

https://github.com/revanced/revanced-patches/issues/455

## 3.22. Casting to TV have ads

Casting to TV is different. ReVanced YT does not handle the video stream, it basically tells the TV: go and play that video with this link. So you will need a ad-free YouTube TV client. You can get one [here](https://github.com/yuliskov/SmartTubeNext). Note that SmartTubeNext is not developed and not affiliated in any way with the ReVanced team.

## 3.23. SponsorBlock does not work

SponsorBlock is a community project. There might be no marked sponsors yet because

- The video was too new
- Nobody uploaded/marked any segments

Or it might also be that the SponsorBlock server is down. Wait a few minutes and try again. You can check the status at [here](https://status.sponsor.ajay.app/).

Or, if it does not skip automatically, checkout [3.32](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/troubleshoot/03-youtube/32/)

## 3.24. Dislike button shows nothing

Possible reasons include: 

- Return Youtube Dislike server was down
- API timeout, try again later

## 3.25. Dislike button said hidden

The YouTuber opted-out from the Return Youtube Dislike project

## 3.26. How to auto-skip sponsor segments?

ReVanced setting > SponsorBlock > scroll down > Change segment behabior > select category > skip automatically

## 3.27 Screen goes dark/dim and unable to control/swipe

This is a side effect of removing a YT premium ad. Updating patches to version 2.172.0 **AND** including the `hide get premium` patch should fix it.

Or You could press the back button / use back gesture to close it temporarily. It should not come back too quickly.

## 3.28 Low contrast in player / does not lower brightness when controls are visible

Repatch without the `hide player overlay` patch. This requires a repatch, you cannot fix it in settings.

## 3.29 SponsorBlock temporarily not available

API Timed out. SB server did not respond in time. Either it is down or it is super busy right now. You can check the status of SB server [here](https://status.sponsor.ajay.app/).

![toast warning](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/29.jpg?raw=true)

## 3.30 Player controls won't disappear

Go to YouTube settings > Accessibility and disable Accessibility player.

![Accessibility player](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/30.jpg?raw=true)

## 3.31 Where is the hide-shorts-button patch?

Merged with `navigation buttons` patch

## 3.32 How can I auto-skip sponsors with SponsorBlock?

Revanced Youtube > settings > SponsorBlock > scroll down > select category > skip automatically

![different behaviours](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/32.jpg?raw=true)

## 3.33 Cannot see comments/details when fullscreen

Disable: Avatar > settings > ReVanced settings > layout > Hide fullscreen panels

## 3.34 Shorts still shows in feed

Enable: ReVanced Settings > Layout > _scroll to bottom_ > Shorts Components > Hide Shorts in feed

Then restart the app.

If you can't find the option, make sure you used default patches when patching YouTube.

## 3.35. Why did the logo/name change?

The YouTube ReVanced logo and the name is changed by the `custom branding` patch. Since patch version `2.188.0` this is a non-default patch.

If you want the new logo, manually add the patch. Exclude it otherwise.

## 3.36 Why is the audio track selection missing?

Enable it at: revanced settings > layout > player flyout menu items > audio track

Credit: leadedmegabyte on discord

## 3.37 Video not available

Re-patch ReVanced Youtube and use `GmsCore` instead of `vanced microG` at `GmsCore support` patch.

![Error example](https://github.com/SodaWithoutSparkles/revanced-troubleshooting-guide/blob/main/troubleshoot/03-youtube/37.jpg?raw=true)

