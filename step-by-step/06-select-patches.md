# 6. Select patches

The manager now automatically select patches for first time users. Skip to the next section IF you are patching for the first time.

!!!danger
Changing the default patches may break things. It is NOT recommended for first time users to change the default selection.
!!!

!!!
You may want to check if the `Custom branding` patch is ENABLED. Enable it if you want a different icon and app name than stock YouTube one.
_This became a non-default patch since patch version `2.188.0`._
!!!

!!!
If you WANT to change the default selection, turn on the option at ReVanced Manager settings > Enable changing selection. It is in the "Advanced" section of the settings.
!!!

==- Last time I patched un-successfully / Re-patching / not patching for the first time
1. Click "Select patches" or "Selected patches"
2. In the select patches view, choose "Default"
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
2. In the select patches view, choose "Default"
![default](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/110-select_default.jpg?raw=true)
!!!danger
Do NOT disable the default patches unless you know what you are doing. Especially, do **NOT** disable these two:
- `GmsCore Support`
- `Client Spoof`
!!!
3. You can scroll around and disable some patches. BUT don't disable any which you don't know the purpose of.
4. DO NOT ENABLE THE FOLLOWING PATCHES
    - `Change package name`
    - `Change version code`
    - `Enable Android debugging`
    - `Export all activities`
    - `Hex`
    - `Override certificate pinning`
    - `Predictive back gesture`
    - `Remove screen capture restriction`
    - `Remove screenshot restriction`
    - `Spoof SIM country`
    - `Spoof Wi-Fi connection`
5. You can disable the following patches safely. I have tested them:
    - `Disable auto captions`
    - `Hide player overlay`
    - `Hide seekbar`
    - `Hide timestamp`
    - `Wide search bar`
6. **Enable** the following patches. They are critical.
    - `GmsCore Support` (unless your device is rooted)
        - _if you don't know what root is, you are probably not rooted_
    - `Client Spoof` (must enable)
6. When you have finished, click "Done" on the bottom right
![click done](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/120-click_done.jpg?raw=true)

===
