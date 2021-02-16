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

InnoGuards Overall Architecture is shown below.
[![InnoGuard-Architecture](./assets/Architecture_Diagram.jpg)]()

### OCR Text Detection and Recognition

Extracts text from images through screenshots.

Example WhatsApp Screenshot   |  OCR Text Extraction
:----------------------------:|:-------------------------:
![Ocr-Screenshot](./assets/ocr_screenshots_before.png)  |  ![Text-Extraction](./assets/ocr_screenshots_after.png)

### Safe Browsing

BrowserHistory Module and SafeBrowsing API are used to extract one’s browsing history from a user's local computer into a csv or pandas array for analysis of age inappropriate links.

The links are stored within a Mongo Database and are determined as **malicious** or not.

![Safe-browsing](./assets/safe-browsing.gif)

### Tisane API

Classifies violence against children [Cyberbulling, Sexual Comments and Harassment, Grooming, Emotional Abuse and Suicidal Tendencies] through texts.

### Google Vision API

Determines child inappropriate images.

![vision-api](./assets/racyimg.gif)

### Google Speech API

Allows audio analysis by turning speech to text.

The recorded audio is turned into text and then analysed through Tisane API for violence against children as shown below.

![speech-api](./assets/speechtotext.gif)


## Usage

### Configuration

Instructions:

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
git clone https://github.com/InnoGuard/InnoGuard.git

# Go into the repository
cd InnoGuard

# Create new Python virtual environment.

# Upon activating the new virtual environment, at root directory, run
pip3 install -r requirements.txt

# Create a Constants.py file under the path scripts/libs/ with the content:
GC_API_KEY = 'your_google_api_key_here'
MONGODB = "your_mongodb_address"

# Used for Google Vision API
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   'LIKELY', 'VERY_LIKELY')


TISANE_API_KEY_1 = 'public_api_key'
TISANE_API_KEY_2 = 'secret_api_key'

FILE_PATH = "path to images and audio for testing"

# In the scripts folder, the following Python scripts can be executed by the following commands:
python3 getImageResults.py
python3 getBrowserHistory.py

# Output from these commands will be displayed via the terminal.

```

### OCR Usage

Open in colab - https://colab.research.google.com/gist/rajeevratan84/45ca3d6c74175a204ca644ae1605daa4/ocr-on-screenshots

### Safe Browsing Usage

### Tisane API Usage

### Google Vision Usage

### Google Speech Usage

## Future Work

The team at InnoGuard plans to implement:

- **Notification and Reporting System**: Upon identification, InnoGuard shall create a report of all instances mentioned above and send this report to the child’s parents or guardian via email or the police if the danger is high, with varying levels (colours) of danger and importance. 

- **Caribbean Lingo Dataset**: Currently, the APIs used to not consider Caribbean Lingo as shown in the gif below where it detects the Caribbean Phrase "Buss ah wine" as a person.

Thus, the new model would be emphasized and trained against Caribbean Speech Datasets to detect harmful Caribbean Lingo online.

- **Chatbot Assistant**:  InnoGuard shall provide real-time emotional support via a chatbot to give tips and consolation.

## License

InnoGuard is licensed under the terms of the MIT Open Source license and is available for free.

## Links
* [YouTube Pitch](https://youtu.be/Ncit5I1Bsxo)
