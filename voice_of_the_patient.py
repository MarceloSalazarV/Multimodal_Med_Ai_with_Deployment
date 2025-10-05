# voice_of_the_patient.py

import os
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"

# def record_audio(file_path, timeout=20, phrase_time_limit=None):
#     """
#     Disabled for cloud deployment. Gradio handles microphone input in the browser.
#     """
#     pass

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )
    return transcription.text
