# voice_of_the_doctor.py

from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_with_gtts(input_text, out_filepath_mp3, out_filepath_wav):
    # Generate MP3
    audioobj = gTTS(text=input_text, lang="en", slow=False)
    audioobj.save(out_filepath_mp3)

    # Convert to WAV
    sound = AudioSegment.from_mp3(out_filepath_mp3)
    sound.export(out_filepath_wav, format="wav")

    return out_filepath_mp3, out_filepath_wav
