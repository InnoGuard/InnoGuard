# InnoGuard

InnoGuard is a child protection tool that provides protection for children by classifying violence against children through texts and audio, and determining age inappropriate images and links.

[![InnoGuard](./assets/innoguard_title.png)]()

## Table of Contents

- [InnoGuard Tools](#innoguard-tools)
    - [OCR Text Detection and Recognition](#ocr-text-detection-and-recognition)
    - [Safe Browsing](#safe-browsing)
    - [Tisane API](#tisane-api)
    - [Google Vision API](#google-vision-api)
    - [Google Speech API](#google-speech-api)
- [Usage](#usage)
    - [Configuration](#configuration)
    - [OCR Usage](#ocr-usage)
    - [Safe Browsing Usage](#safe-browsing-usage)
    - [Tisane API Usage](#tisane-api-usage)
    - [Google Vision Usage](#google-vision-usage)
    - [Google Speech Usage](#google-speech-usage)
- [Future Work](#future-work)
- [License](#license)
- [Links](#links)

## InnoGuard Tools

### OCR Text Detection and Recognition

Extracts text from images through screenshots.

Example WhatsApp Screenshot   |  OCR Text Extraction
:----------------------------:|:-------------------------:
![Ocr-Screenshot](./assets/ocr_screenshots_before.png)  |  ![Text-Extraction](./assets/ocr_screenshots_after.png)

### Safe Browsing

BrowserHistory Module and SafeBrwosing API are used to determine dangerous, age innapropriate links.

![Safe-browsing](./assets/safe-browsing.gif)

### Tisane API

ClassifIES violence against children [Cyberbulling, Sexual Comments and Harassment, Grooming, Emotional Abuse and Suicidal Tendencies] through texts.

### Google Vision API

Determines child inappropriate images.

![vision-api](./assets/racyimg.gif)

### Google Speech API

Allows audio analysis by turning speech to text.

![speech-api](./assets/speechtotext.gif)


## Usage

### Configuration

Instructions:
- Clone repository.
- Create new Python virtual environment.
- Upon activating the new virtual environment, at root directory, run: 'pip3 install -r requirements.txt'.
- In the scripts folder, the following Python scripts can be executed by the following commands:
    - python3 getImageResults.py
    - python3 getBrowserHistory.py
  Output from these commands will be displayed via the terminal.


Open in colab - https://colab.research.google.com/gist/rajeevratan84/45ca3d6c74175a204ca644ae1605daa4/ocr-on-screenshots

### OCR Usage

### Safe Browsing Usage

### Tisane API Usage

### Google Vision Usage

### Google Speech Usage

## Future Work

Currently, the APIs used to not consider Caribbean Lingo as shown in the gif below.

The team at InnoGuard plans to:

## License

InnoGuard is licensed under the terms of the MIT Open Source license and is available for free.

## Links
* [YouTube Pitch](https://youtu.be/Ncit5I1Bsxo)
