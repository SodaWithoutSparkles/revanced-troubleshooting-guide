---
redirect: /step-by-step/05-select-apk.md
visibility: hidden
---

# 4. Checking compatibility

We are going to check if your device is supported.

1. Launch ReVanced Manager. Ignore any updates it claimed it knew.
==- Image for reference
![launch rvm](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/040-first_launch_manager.jpg?raw=true)
===
2. Go to the settings tab and scroll down until you find "About"
==- Image for reference
![check about](https://github.com/SodaWithoutSparkles/ReVanced-troubleshooting-guide/blob/main/screenshots/050-check_about.jpg?raw=true)
===
3. Check that `Arch` says `arm64-v8a`
4. If it does not say `arm64-v8a` you cannot patch YouTube on your device. Please patch it on another device or your PC.

==- What does `arch` mean? Why is `arm64-v8a` required?
`arch` is the architecture of your CPU. In layman terms, it is "the language of the CPU". If you don't know that language, you cannot communicate with that CPU. If your device does not support `arm64-v8a` you can patch on a computer with the [`revanced-cli`](/06-revanced-cli.md), [`Taku's auto-cli`](https://github.com/taku-nm/auto-cli) or [`revanced-builder`](https://github.com/reisxd/revanced-builder).
===
