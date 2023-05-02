# 3. ReVanced YouTube

Troubleshooting regarding YouTube ReVanced issues

## 3.1. Unable to open/launch ReVanced youtube / ReVanced crashing

Probably one of the following: 

- split APK is used to patch
    - patch again using the full APK
- non-recommended patches/version
    - patch again with the default/recommended patches/version
- vanced microG not installed
    - install it [here](https://github.com/TeamVanced/VancedMicroG/releases/tag/v0.2.24.220220-220220001)
- You exited ReVanced manager when patching
    - Don't do that. Repatch again.

## 3.2. Video playback issues / buffers / buggy / content not available

Include `client spoof` patch. (_`spoof signature verification` was merged into `client spoof`_)

You can get a guide on that [here](/02-add-patch.md)

If you cannot find them, you probably patched an unsupported YT version.

## 3.3. App not installed / Installation is blocked / `install_failed_verification_failure`

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

## 3.4. Video turns very dark in fullscreen

Try swiping up on the left side of your screen. This feature is called swipe brightness control. Swipe down all the way and it would use auto-brightness. You can also swipe to control volume on the right.

You can disable this under ReVanced YT settings > ReVanced > Interaction > Swipe Controls

## 3.5. No internet connection

Did you change your google password? Anyway, go to system settings > accounts > **vanced microG** > delete/logout account. Don't worry, this will not remove your google account on your device, just remove the one used by microG (hence revanced). 

## 3.6. Shorts button missing?

Disable: ReVanced YT settings > ReVanced > Layout > Hide Shorts, Hide Shorts button

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

Known issue. It would be fixed automatically when you watch the second video. If it still stays on the top, repatch and include the latest patches. Keep in mind that YouTubers can configure subtitle positions so it might be intended for the subtitles to be on the top.

https://github.com/revanced/revanced-patches/issues/2003

## 3.12. Ambient mode / "glow around video" missing

Turn the function off and on again. Seriously, this fixed it.

## 3.13. Some buttons next to like/dislike missing 

Disable: ReVanced YT settings > ReVanced > Layout > Hide action buttons > All toggles listed

## 3.14. Remix/share/thanks/shop/clip buttons missing

Disable: ReVanced YT settings > ReVanced > Layout > Hide action buttons > Hide all other action buttons

## 3.15. Youtube autoplays the next video

1. Disable: ReVanced YT settings > ReVanced > Layout > Hide autoplay button
2. Restart Youtube revanced
3. Play any video, in the video player, turn off autoplay
4. Enable: ReVanced YT settings > ReVanced > Layout > Hide autoplay button
5.  Restart Youtube revanced

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

Casting to TV is different. ReVanced YT does not handle the video stream, it basically tells the TV: go and play that video with this link. So you will need a ad-free youtube TV client. You can get one [here](https://github.com/yuliskov/SmartTubeNext). Note that SmartTubeNext is not developed and not affiliated in any way with the ReVanced team.

## 3.23. Sponsorblock does not work

Sponsorblock is a community project. There might be no marked sponsors yet because

- The video was too new
- Nobody uploaded/marked any segments

Or it might also be that the sponsorblock server is down. Wait a few minutes and try again. You can check the status at [here](https://status.sponsor.ajay.app/).

## 3.24. Dislike button shows nothing

Possible reasons include: 

- Return Youtube Dislike server was down
- API timeout, try again later

## 3.25. Dislike button said hidden

The YouTuber opted-out from the Return Youtube Dislike project

## 3.26. How to auto-skip sponsor segments?

ReVanced setting > SponsorBlock > scroll down > Change segment behabior > select category > skip automatically

## 3.27 Screen goes dark/dim and unable to control/swipe

This is a side effect of removing a YT premium ad. Currently there is no known permanent solution.

You can press the back buttom / use back gesture to close it temporarily. It should not come back too quickly

## 3.28 Low contrast in player / does not lower brightness when controls are visible

Repatch without the `hide player overlay` patch. This requires a repatch, you cannot fix it in settings.
