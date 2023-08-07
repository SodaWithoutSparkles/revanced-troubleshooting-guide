# ReVanced CLI patch guide

In this guide, we are going to use ReVanced CLI on Windows to patch instead of manager. This might be useful when you:

- Have `armv7` device
- Want to try latest beta builds
- etc.

## 1. Install Java Development Kit (JDK)

1. Open a powershell terminal by hitting the windows key and typing "powershell"
2. Paste the following command in the terminal to install Azul JDK 11

```winget install "azul zulu jdk 11"```

3. Close the powershell window after it has completed

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

```java -jar cli.jar -a input.apk -b patches.jar -m integration.apk -o out.apk```

| placeholder | meaning | example |
|---|---|---|
| `cli.jar` | revanced-cli jar file | `revanced-cli-2.22.0-all.jar` |
| `input.apk` | the apk you want to patch | `youtube.apk` |
| `patches.jar` | revanced patches bundles | `revanced-patches-2.187.0.jar` |
| `integration.apk` | revanced integrations | `revanced-integrations-0.115.1.apk`|
| `out.apk` | the filename of the patched apk | `patched.apk` |

Example: 

```java -jar revanced-cli-2.22.0-all.jar -a youtube.apk -b revanced-patches-2.187.0.jar -m revanced-integrations-0.115.1.apk -o patched.apk```


## 6. Update ReVanced
1. Delete the old `cli.jar`, `patches.jar`, `integration.jar`, `out.apk`, `input.apk`
2. Repeat from section 2

## 7. Advanced uses
- Read the help page for revanced-cli

```java -jar cli.jar -h```
- Specify keystore file and password

```java -jar cli.jar --keystore='exported.keystore' --password='passwordOfKeystore' -a input.apk ...```

- List patches available

```java -jar cli.jar -b patches.jar -a input.apk -l --with-packages```

- Include / Exclude patches

```java -jar cli.jar -e exclude-1 -e exclude-2 -i include-1 -i include-2 ...```
