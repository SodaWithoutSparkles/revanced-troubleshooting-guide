# ReVanced CLI patch guide

In this guide, we are going to use ReVanced CLI on Windows to patch instead of manager. This might be useful when you:

- Have `armv7` device
- Want to try latest beta builds
- etc.

## 1. Install Java Development Kit (JDK)

1. Open a powershell terminal by hitting the windows key and typing "powershell"
2. Paste the following command in the terminal to install Azul JDK 11

```bash
winget install "azul zulu jdk 11"
```

!!!
Remember to check the box for for adding JDK to PATH, set JAVA_HOME variable and register JavaSoft!
!!!

3. Close the powershell window after it has completed

==- Alternative way to install Azul JDK 11
1. Visit the [download page of Azul JDK](https://www.azul.com/downloads/?version=java-11-lts&package=jdk#zulu)
2. Don't click on the big download button. It is for JDK 17 instead of the JDK 11 that we need.
3. Scroll down a bit and find the version for Windows, and click download
4. Your computer is most likely to be 64-bit.
===

## 2. Get ReVanced related files

![Overview](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/501-cli-patch-embed.jpg)

1. Get the following required files
    - [ReVanced patches](https://github.com/ReVanced/revanced-patches/releases/latest), you need the `.jar` file.
    - [ReVanced CLI](https://github.com/revanced/revanced-cli/releases/latest), you need the `.jar` file.
    - [ReVanced integrations](https://github.com/revanced/revanced-integrations/releases/latest), you need the `.apk` file.
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
2. Right-click the empty space and click "Open Terminal"/"Open Powershell"
3. If you can't find the button, click the file button in the ribbon
4. Type `dir` and hit enter, you should see the 4 files you downloaded just now
5. Type `java -version` and hit enter, you should see it is at major version 11
6. Don't close the terminal window, continue to the next section

==- Image for reference
![Open powershell button in ribbon](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/500-open_pwsh.gif)
===

## 5. Start patching
Type the following command in the terminal window, replacing the placeholder filenames with the actual filename. 

!!!
You can use the `tab` key to auto-complete
!!!
!!!
You may need to use single quotes (`'`) around the filenames to avoid issues, like `'youtube v1.2.3.apk'`
!!! 

```bash
java -jar cli.jar -a input.apk -b patches.jar -m integration.apk -o out.apk
```

| placeholder | meaning | example |
|---|---|---|
| `cli.jar` | revanced-cli jar file | `revanced-cli-2.22.0-all.jar` |
| `input.apk` | the apk you want to patch | `youtube.apk` |
| `patches.jar` | revanced patches bundles | `revanced-patches-2.187.0.jar` |
| `integration.apk` | revanced integrations | `revanced-integrations-0.115.1.apk`|
| `out.apk` | the filename of the patched apk | `patched.apk` |

Example: 

```bash
java -jar revanced-cli-2.22.0-all.jar -a youtube.apk -b revanced-patches-2.187.0.jar -m revanced-integrations-0.115.1.apk -o patched.apk
```

## 6. Installing Patched apk

1. Copy the patched APK file to your phone
!!!
The easiest way would be to use a USB **data** cable and copy it over. Make sure to unlock your device and enable MTP mode.
!!!
2. Install the APK you just transfered
3. Read the [troubleshooting section](/troubleshoot/00-trouble-shooting.md) if you have further issues

!!!
You may need to install [Vanced microG]((https://github.com/TeamVanced/VancedMicroG/releases/tag/v0.2.24.220220-220220001)) if you used the microG support patch, which is the default when patching YouTube related apks.
!!!

## 7. Update ReVanced

1. Delete the old `cli.jar`, `patches.jar`, `integration.jar`, `out.apk`, `input.apk`
2. Repeat from section 2

## 8. Advanced uses


```bash Read the help page for revanced-cli
java -jar cli.jar -h
```

```bash Specify keystore file and password
java -jar cli.jar --keystore='exported.keystore' --password='passwordOfKeystore' -a input.apk ...
```


```bash List patches available
java -jar cli.jar -b patches.jar -a input.apk -l --with-packages
```


```bash Include / Exclude patches
java -jar cli.jar -e exclude-1 -e exclude-2 -i include-1 -i include-2 ...
```
