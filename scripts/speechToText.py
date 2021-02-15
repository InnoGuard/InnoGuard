from google.cloud import speech
import os
import io
import libs.Constants


# Creates google client
client = speech.SpeechClient()

__file__ = libs.Constants.FILE_PATH

# Full path of the audio file, Replace with your file name
file_name = os.path.join(os.path.dirname(__file__),"test.wav")

#Loads the audio file into memory
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    audio_channel_count=2,
    language_code="en-US",
)

# Sends the request to google to transcribe the audio
response = client.recognize(request={"config": config, "audio": audio})

# Reads the response
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))