# ReVanced CLI Initialize Guide (Linux)

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

## 5. Continue

This section has been completed. Go back to the [main cli guide](/06-revanced-cli.md).
