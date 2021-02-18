from google.cloud import speech
import os
import io
import libs.Constants
import wave


__file__ = libs.Constants.FILE_PATH
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = libs.Constants.GOOGLE_APPLICATION_CREDENTIALS


def frame_rate_channel(audio_file_name):
    print(audio_file_name)
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate,channels


def text_from_speech():
    # Creates google client
    client = speech.SpeechClient()

    # audio_path = input("\nPlease enter the path to the audio you wish to test: ") 
    # print("Path entered: ", audio_path) 

    # Full path of the audio file, Replace with your file name
    file_name = os.path.join(os.path.dirname(__file__),"test.wav")

    # Dynamically get the frame rate and channels from audio file
    frame_rate, channels = frame_rate_channel(file_name)

    #Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=channels,
        language_code="en-US",
    )

    # Sends the request to google to transcribe the audio
    response = client.recognize(request={"config": config, "audio": audio})

    # Reads the response
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

text_from_speech()
