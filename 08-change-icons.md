# ReVanced CLI Custom Icon Guide

## Prepare the icon

Your icon should satisfy the following requirements:

- Size between 128x128 and 1024x1024 pixels
- Is a square
- Has transparency
- Format is PNG

If any of the above requirements are not met, use tools like [Photopea](https://photopea.com/) (Runs in-browser), Gimp (Free, Open-Sourced), or Photoshop (Paid) to modify the image. How to use such tools are out of scope of the guide, google search the keywords for help. Example: "Photopea remove background", "Gimp export as png".

## Generate the file structure

1. Go to [this site](https://icon.kitchen/)
2. Select your Image tab under Icon (or use the generic Clipart)
3. Set the background color to whatever color you like (Example: white)
4. Set the shape and effects
5. Hit the download button on the right top corner. It will download `ic_launcher.zip`.
6. Extract just the res folder from `ic_launcher.zip`

==- Image for reference
![Icon kitchen](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/601-icon-kitchen.png)
===

## Rename the files (For YouTube Only)

!!! Hint
You need to ENABLE file extensions for this to work
!!!

1. Go into the `res` folder
2. In **EACH** of the `mipmap-*` folders that have images in them, do the following
    - rename `ic_launcher_adaptive_fore.png` to 
      - `adaptiveproduct_youtube_foreground_color_108.png`
    - rename `ic_launcher_adaptive_back.png` to 
      - `adaptiveproduct_youtube_background_color_108.png`
    - copy `ic_launcher.png` and rename the copy to `ic_launcher_round.png`

## Rename the files (Generally)

!!! Hint
You need to ENABLE file extensions for this to work. [Instructions for Windows](https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01)
!!!

1. Copy the APK you want to patch, rename it such that it ends with `.zip` not `.apk`
2. Unzip the `.zip`
3. Go to the `res` folder of the unzipped file
4. Compare the file structure of the res folder from `ic_launcher.zip` and the `res` folder of the unzipped file. (For clarity, lets call them X and Y respectively)
5. Files in the X folder should have the same names as files in the Y folder
6. Files in Y but not in X can be ignored

## Modify the Options file

!!! Hint
Examples can be found [here](/06-revanced-cli.md#9-options-file)
!!!

1. Generate the options file if it doesn't exist
2. Edit the `iconPath` key to include the path to the res folder

## Patch

Follow the standard procedure to patch with the options file

## Credits

This guide is modified from @leadedmegabyte's change icons guide
