from google.cloud import speech
import os
import io
import libs.Constants
import wave
import contextlib


__file__ = libs.Constants.FILE_PATH
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = libs.Constants.GOOGLE_APPLICATION_CREDENTIALS


def frame_rate_channel(audio_file_name):
    print(audio_file_name)
    with wave.open(audio_file_name, "rb") as wave_file:
        frames = wave_file.getnframes()
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        duration = (frames / float(frame_rate))
        return frame_rate, channels, duration


def short_audio(audio_path, channels):
    # Creates google client
    client = speech.SpeechClient()

    # Full path of the audio file, Replace with your file name
    # file_name = os.path.join(os.path.dirname(__file__),"test.wav")

    #Loads the audio file into memory
    with io.open(audio_path, "rb") as audio_file:
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


def long_audio(audio_path, channels):
    """Transcribe the given audio file asynchronously."""

    client = speech.SpeechClient()

    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS (Google Cloud Storage) file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=channels,
        # sample_rate_hertz=16000,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=180)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))


def main():
    audio_path = input("\nPlease enter the path to the audio you wish to test: ") 
    print("Path entered: ", audio_path) 

    # Dynamically get the frame rate and channels from audio file
    frame_rate, channels, duration = frame_rate_channel(audio_path)

    if (duration < 60):
        print("short", duration)
        short_audio(audio_path, channels)
    elif (duration >= 60):
        print("long", duration)
        long_audio(audio_path, channels)
    else:
        print("Invalid Audio File, please check that the file is a .wav file and try again.")


if __name__ == '__main__':
    main()