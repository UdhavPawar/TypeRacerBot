<!-- Header -->
<h1 align="center"><a href="https://github.com/UdhavPawar/TypeRacerBot">Type Racer Bot</a></h1>
<!-- Description -->
<h3 align="center">Win every <a href="https://play.typeracer.com/" target="_blank">typing</a> race with 200+ words per minute</h3>

<!-- Labels -->
<p align="center">
  <img src="https://img.shields.io/badge/package-bot-blue.svg?style=flat">
  <img src="https://img.shields.io/badge/code-python3-orange.svg?style=flat">
  <img src="https://img.shields.io/badge/build-passing-green.svg?style=flat">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat">
</p>

<!-- Jumpers -->
<p align="center">
  <a href="#how-it-works">How it works</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#contributing">Contribute</a>
</p>

## How it works
```
1. Using pynput.mouse we get co-ordinates (pixels) of selected screen using mouse
2. Next an in-place (not saved locally) screenshot is captured of those pixels using pyscreenshot.grab
3. This screenshot acts as input for pytesseract.image_to_string function which converts image to string
4. We polish the output string and text is now ready to be typed
5. Finally we simulate typing of this string using pynput.keyboard which will iterate over every character in string and type it out
```
> checkout my [portfolio](https://udhavpawar.com/) to learn more about this project

## Installation
![git clone repo](./svgs/installation.svg)

## How To Use


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change/fix.

## License
[MIT](https://github.com/UdhavPawar/TypeRacerBot/blob/master/LICENSE)
