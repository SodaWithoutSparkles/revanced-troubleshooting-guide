# 4. Checking compatibility

We are going to check if this device is supported.

1. launch ReVanced Manager.
==- Image for reference
![launch rvm](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/040-first_launch_manager.jpg?raw=true)
===
2. Go to the settings tab and scroll down until you find "About"
==- Image for reference
![check about](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/050-check_about.jpg?raw=true)
===
3. Check that `Arch` had at least 1 entry that looks like `arm64-v8a`
4. If you only got something that said `armv7` or lower, you cannot patch it on your phone. Please patch it on another device or your PC.
5. If you got `armv8`, you are probably fine
6. Check that your Android version is at least 8
7. If you only got something that said `armv7` or lower, you may not be able to patch on your phone. You can patch it on another device or a computer with [ReVanced CLI](/06-revanced-cli.md).
8. If you made it here, you can probably patch on your phone with ReVanced Manager

==- What does `arch` mean? Why is `armv7` not supported?
`arch` is the architecture of your CPU. In layman terms, it is "the language of the CPU", if you don't know that language, you cannot communicate with that CPU. 

The ReVanced team will move to `arsclib` soon™, which supports `armv7`. For now, you can patch on a computer with [ReVanced CLI](/06-revanced-cli.md) instead.
===
