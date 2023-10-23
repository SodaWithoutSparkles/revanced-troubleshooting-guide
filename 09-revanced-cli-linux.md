# ReVanced CLI patch guide

In this guide, we are going to use ReVanced CLI on Linux to patch instead of manager. This guide mainly centers around debian-based distros, but you can adapt them to fit arch-based ones. Also, If you are using Linux, we expect you know how to use Google and the command line interface, such as quoting/escaping parameters and using tab to auto-complete.

## 1. Install Java Development Kit (JDK)

We can use JDK version 11, **17** or 20. Change the number to install different versions.

```bash Install openjdk 17
sudo apt install openjdk-17-jdk
```

## 2. Get ReVanced related files

![Overview](https://raw.githubusercontent.com/SodaWithoutSparkles/revanced-troubleshooting-guide/main/screenshots/501-cli-patch-embed.jpg)

1. Get the following required files
    - [ReVanced Patches](https://github.com/ReVanced/revanced-patches/releases/latest), you need the `.jar` file.
    - [ReVanced CLI](https://github.com/revanced/revanced-cli/releases/latest), you need the `.jar` file.
    - [ReVanced Integrations](https://github.com/revanced/revanced-integrations/releases/latest), you need the `.apk` file.
2. Put all of the files in a directory. Lets call it `revanced` for now.

## 3. Get the APK you wanted to patch

1. If you want YouTube APK, get the YouTube apk link at [step by step guide](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/step-by-step/03-get-files/)
2. If you want other APKs, find the supported version at [versions.md](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/05-versions/)
3. Put the APK you downloaded in the same directory with the 3 files you downloaded just now.
4. Rename the APK to a shorter name, preferably without spaces and special symbols

!!!warning
Make sure you downloaded the full APK, not .apks/.apkm/split apks
!!!

## 4. Sanity checks

1. Go to the `revanced` directory you made just now
2. Open a terminal if you haven't already
3. Run `ls`, you should see the 4 files you downloaded just now
4. Run `java -version`. The version of JDK you installed in Part 1 should appear
5. Don't close the terminal, continue to the next section

## 5. Start patching

Run the following commands, replacing the placeholder filenames with the actual filename.

```bash
java -jar cli.jar patch -b patches.jar -m integrations.apk -o out.apk input.apk
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
java -jar revanced-cli-3.1.0-all.jar patch -b revanced-patches-2.190.0.jar -m revanced-integrations-0.117.1.apk -o out.apk youtube.apk
```

## 6. Installing Patched apk

1. Copy the patched APK file to your phone
2. Install the APK you just transferred
3. Read the [troubleshooting section](/troubleshoot/00-trouble-shooting.md) if you have further issues

!!!
You may need to install [Vanced microG]((https://github.com/TeamVanced/VancedMicroG/releases/tag/v0.2.24.220220-220220001)) if you used the microG support patch, which is the default when patching YouTube related apps.
!!!

## 7. Update ReVanced

1. Delete the old `cli.jar`, `patches.jar`, `integration.jar`, `out.apk`, `input.apk`
2. Repeat from section 2

## 8. Advanced uses

```bash Read the help page for revanced-cli
java -jar cli.jar -h
```

```bash Read the help page for each sub-commands (example: patch sub-command)
java -jar cli.jar patch
```

```bash Specify keystore file and password
java -jar cli.jar patch --keystore='exported.keystore' --password='passwordOfKeystore' -b patches.jar ...
```

```bash List patches available (with descriptions, options, packages and versions compatible)
java -jar cli.jar list-patches -dopv patches.jar
```

```bash Include / Exclude patches
java -jar cli.jar patch -e exclude-1 -e exclude-2 -i include-1 -i include-2 ...
```

```bash Generate Options file
# This will overwrite the existing file
# Use -u instead of -o if you want to update existing file
java -jar cli.jar options -o patches.jar
```

```bash Use Options file
# You need to generate options file first
java -jar cli.jar patch --options=path-to-options-file ...
```

## 9. Options file

Some settings for patches has to be configured via the option file. Don't change them unless you know what you are doing. Don't modify more things than you need to.

!!!
When pasting the path, make sure to use absolute path and escape any `\` to avoid issues. You can escape them by putting another `\` before it.
!!!

!!!
**ALL** value entry should have quotes, except null. Example:
"value": "YouTube ReVanced"
!!!

| Patch | Key | Default value | Type | Example |
| --- | --- | --- | --- | --- |
| Change package name | packageName | null | pkgName | "app.revanced.android.youtubealt" |
| Custom branding | appName | "YouTube ReVanced" | string | "new app name" |
| Custom branding | iconPath | null | path | `"C:\\Users\\test\\Downloads\\res\\"` [^1] |
| Spoof client | client-id | null | string | "abcdef" [^2] [^3] |
| Spotify theme | backgroundColor | "@android:color/black" | string | "@android:color/black" [^4] [^5] |
| Spotify theme | accentColor | "#ff1ed760" | AARRGGBB color code | "#ff1ed761" |
| Spotify theme | accentPressedColor | "#ff169c46" | AARRGGBB color code | "#ff169c47" |
| Theme | darkThemeBackgroundColor | "@android:color/black" | string | "@android:color/holo_blue_dark" [^4] [^5] |
| Theme | lightThemeBackgroundColor | "@android:color/white" | string | "@android:color/holo_purple" [^4] [^5] |

[^1]: Detailed instructions can be found [here](/08-change-icons.md)

[^2]: Don't change this option unless absolutely necessary

[^3]: This option is used when patching many apps, including (but not limited to) reddit, youtube and spotify

[^4]: Color values can be found [here](https://developer.android.com/reference/android/R.color#constants_1), make sure you have a higher API level than when the color was added

[^5]: You can also use colors at `revanced-cache/res/values/colors.xml` [^6], reference them by "@color/color_name"

[^6]: You can also edit that file after revanced deleted the cache to include custom colors
