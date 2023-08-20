# ADB remove guide

## Preface

This guide is to use ADB (Android Debug Bridge) to remove remains or artifacts from the last ReVanced YouTube install

## Requirements

1. A windows computer
2. An Android smartphone with USB debugging enabled
3. An USB cable capable of data transfer

If you don't know how to enable USB debugging, google "\<phone model\> enable usb debugging" (obviously replacing \<phone model\> with your actual phone model)

## Sanity Checks

If you are trying to install ReVanced but failed, make sure that you have checked [section 3.3](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/troubleshoot/03-youtube/03/) first to avoid wasting your time.

## Steps

1. On the computer, download the latest [platform tools](https://developer.android.com/tools/releases/platform-tools)

2. Unzip it. There should be an "adb.exe" inside. Don't double-click it to open though, it won't work. 

3. Right-click on the empty area next to it, select something like "open in powershell" or "open in windows terminal" or "open in cmd".

4. A command window (shell) would pop up. In that window, type `adb devices`. Press enter. You may need to prepend `./` or `.\` in front of it, like `./adb devices`. Remember the one used, and prepend it before all `adb` commands from now on. Something like "List of devices attached" should appear. Something containing "daemon" might also appear, but you can safely ignore them.

5. Connect your phone which USB debugging was already enabled to your computer. Allow USB debugging from the popup on the phone. You may need to unlock the device. If you dont see the popup, it is likely to be the following issues:

    - that is a power only cable, use one with both power and data
    - USB debugging was not enabled
    - something else that I dont know how to solve

6. Then, on the shell, enter `adb devices` again. There should be a new entry.

7. Finally, just type the following, press enter, and ReVanced YT would be uninstalled, and all remains would be removed (if any). 

```bash
adb uninstall app.revanced.android.youtube
```

8. If that did not work, use this instead:

```bash
adb shell pm uninstall app.revanced.android.youtube
```

9. Then you can disconnect the phone, disable USB debugging and disable developer options on your phone. Close the shell by typing `exit` or the X button as usual.

10. Install ReVanced again from ReVanced manager.

11. Delete the zip file and the extracted files download at the first step.
