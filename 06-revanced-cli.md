# ReVanced CLI patch guide

## 1. Initialize/update environment

For Windows users, visit [ReVanced CLI Initialize Guide (Windows)](/CLI-init/01-cli-init-windows.md).

For Linux users, visit [ReVanced CLI Initialize Guide (Linux)](/CLI-init/02-cli-init-linux.md).

## 2. Start patching

Run the following commands, replacing the placeholder filenames with the actual filename.

```bash
java -jar cli.jar \
  patch -b patches.jar \
  -m integrations.apk \
  -o out.apk input.apk
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
java -jar revanced-cli-3.1.0-all.jar \
  patch -b revanced-patches-2.190.0.jar \
  -m revanced-integrations-0.117.1.apk \
  -o out.apk youtube.apk
```

## 3. Installing Patched apk

1. Copy the patched APK file to your phone
2. Install the APK you just transferred
3. Read the [troubleshooting section](/troubleshoot/00-trouble-shooting.md) if you have further issues

!!!
You may need to install [GmsCore](https://github.com/ReVanced/GmsCore/releases/latest) if you used the microG support patch, which is the default when patching YouTube related apps.
!!!

## 4. Update ReVanced

1. Delete the old `cli.jar`, `patches.jar`, `integration.jar`, `out.apk`, `input.apk`
2. Repeat from section 1

## 5. Advanced uses

```bash Read the help page for revanced-cli
java -jar cli.jar -h
```

```bash Read the help page for each sub-commands (example: patch sub-command)
java -jar cli.jar patch
```

```bash Specify keystore file and password
java -jar cli.jar patch \
  --keystore='exported.keystore' --keystore-password='passwordOfKeystore' \
  --alias='alias' --keystore-entry-password='passwordOfKeystoreEntry' \
  -b patches.jar ...
```

```bash List patches available (with [o]ptions, [p]ackages and [v]ersions compatible)
java -jar cli.jar list-patches -opv patches.jar
```

```bash Include / Exclude patches
java -jar cli.jar patch -e 'Exclude patch 1' -e 'Exclude patch 2' -i 'Include patch 1' -i 'Include patch 2' ...
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

## 6. Options file

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
