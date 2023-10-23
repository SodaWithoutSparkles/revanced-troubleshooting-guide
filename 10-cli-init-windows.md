# ReVanced CLI Initialize Guide (Windows)

In this guide, we are going to use ReVanced CLI on Windows to patch instead of manager.

## 1. Install Java Development Kit (JDK)

1. Visit the [download page of Azul JDK](https://www.azul.com/downloads/?package=jdk#zulu)
2. JDK versions 11, **17** and 20 are all compatible. Download the `.msi` installer for the platform you need
3. Your computer is most likely to be 64-bit.
4. Remember to check all the checkboxes, especially the JAVA_HOME one.

!!!
Remember to check the box for for adding JDK to PATH, set JAVA_HOME variable and register JavaSoft!
!!!

==- Image for reference
![Check all options](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/502-jdk_install.png)
===

5. Wait for it to finish installing

## 2. Get ReVanced related files

![Overview](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/501-cli-patch-embed.jpg)

1. Get the following required files
    - [ReVanced Patches](https://github.com/ReVanced/revanced-patches/releases/latest), you need the `.jar` file.
    - [ReVanced CLI](https://github.com/revanced/revanced-cli/releases/latest), you need the `.jar` file.
    - [ReVanced Integrations](https://github.com/revanced/revanced-integrations/releases/latest), you need the `.apk` file.
2. Put all of the files in a folder in `Downloads`. Lets call it `revanced` for now

## 3. Get the APK you wanted to patch

1. If you want YouTube APK, get the YouTube apk link at [step by step guide](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/step-by-step/03-get-files/)
2. If you want other APKs, find the supported version at [versions.md](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/05-versions/)
3. Put the APK you downloaded in the same folder with the 3 files you downloaded just now.
4. Rename the APK to a shorter name, preferably without spaces and special symbols (dots are fine)

!!!warning
Make sure you downloaded the full APK, not .apks/.apkm/split apks
!!!

## 4. Sanity checks

1. Go to the `revanced` folder you made just now
2. Right-click/Shift-right-click the empty space and click "Open Terminal"/"Open Powershell"
3. If you can't find the button, click the file button in the ribbon
4. Type `dir` and hit enter, you should see the 4 files you downloaded just now
5. Type `java -version` and hit enter. The version of JDK you installed in Part 1 should appear.
6. Don't close the terminal window, continue to the next section

==- Image for reference
![Open powershell button in ribbon](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/500-open_pwsh.gif)
===

## 5. Continue

This section has been completed. Go back to the [main cli guide](/06-revanced-cli.md).
