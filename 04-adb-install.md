# ADB install guide

## Preface

This guide is to use ADB (Android Debug Bridge) to install ReVanced (or any other apk). This has a higher chance of working, and provides more debug information if it does not work.

## Requirements

1. A windows computer
2. An Android smartphone with USB debugging enabled
3. An USB cable capable of data transfer

If you don't know how to enable USB debugging, google "\<phone model\> enable usb debugging" (obviously replacing \<phone model\> with your actual phone model)

## Steps

### `adb setup`

1. On the computer, download the latest [platform tools](https://developer.android.com/tools/releases/platform-tools)

2. Unzip it. There should be an "adb.exe" inside. Don't double-click it to open though, it won't work. 

3. Right-click on the empty area next to it, select something like "open in powershell" or "open in windows terminal" or "open in cmd".

4. A command window (shell) would pop up. In that window, type `adb devices`. Press enter. You may need to prepend `./` or `.\` in front of it, like `./adb devices`. Remember the one used, and prepend it before all `adb` commands from now on. Something like "List of devices attached" should appear. Something containing "daemon" might also appear, but you can safely ignore them.

5. Connect your phone which USB debugging enabled to your computer with a USB cable. 

6. Allow USB debugging from the popup on the phone
    - You may need to unlock the device. 
    - If you dont see the popup, it might be caused by:
        - the USB cable is a power only cable, use one with both power and data
        - USB debugging was not enabled
        - something else that I don't know how to solve

7. Then, on the shell, enter `adb devices` again. There should be a new entry.

8. Copy the apk to your phone's Download folder

9. On the shell, enter `adb shell`

10. You are now using the shell in your device

11. Enter `whoami`. It should output `shell`. Note: you need to hit the \<Enter\> key.

### Install via ADB

1. Enter `cd /storage/emulated/0/Download`.

2. Enter `ls *.apk`. This would list all apks in Download

3. Find the name of the apk you want to install from the list

4. Enter `pm install name_of_apk.apk`. Example: `pm install youtube-revanced_v19.04.37.apk`

5. If it said Success or showed nothing, check your phone to see if it actually insalled
    - If yes, you have installed ReVanced. Go to Cleanup section
    - If no, ask for help

6. If it said something like `Error: Unable to open file`
    - It should've shown you a suggestion, Example: Consider using a file under `/data/local/tmp`
    - Remember that path, we are going to use that later

7. We are going to copy the APK to that path

8. Enter `cp name_of_apk.apk /data/local/tmp/`, obviously replacing `name_of_apk.apk` with the actual name

9. Now hit the arrow_up key on your keyboard (↑) until you see the command you entered in step 4 (`pm install ...`. Don't hit enter yet.

10. Use arrow keys (← →) to move the cursor.

11. Add `/data/local/tmp/` before the APK name such that it looked like this:
    - `pm install /data/local/tmp/youtube-revanced_v19.04.37.apk`

12. Hit enter

13. If it showed an error ("Exception occurred while executing"):
    - Check the reason given
    - "not enough space" then remove some things until you got the space
    - Google the reason given, for example: "adb pm install not enough space"
    - Or alternatively, ask for help

14. If it said Success or showed nothing, check your phone to see if it actually insalled
    - If yes, you have installed ReVanced. Go to pre-cleanup section
    - If no, ask for help

## Pre-cleanup

1. This section is only needed of you have done step 18
2. Enter `rm /data/local/tmp/*.apk`
3. pre-cleanup done. Now go to cleanup section

## Cleanup

1. Then you can disconnect the phone, disable USB debugging and disable developer options on your phone. Close the shell by typing `exit` or the X button as usual.

2. Delete the zip file and the extracted files download at the first step.
