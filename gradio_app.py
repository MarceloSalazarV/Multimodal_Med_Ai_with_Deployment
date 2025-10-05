import os
import time
import gradio as gr
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

# System prompt for AI doctor
system_prompt = """You have to act as a professional doctor, and even though you are not, this is for learning purposes. 

Look at the image carefully. If anything looks medically wrong or concerning, mention it.

If you can make a differential diagnosis, suggest likely causes and simple remedies.

Do not include any numbers or special characters. Your response should be in one long paragraph with a maximum of two sentences.

Always speak like you're talking to a real patient, not as an AI model. Start your answer directly without saying things like 'In the image I see'. 

Instead say things like 'With what I see, I think you have...'. Make sure to still give an answer even if the user did not say anything."""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = ""
    
    # Convert patient audio to text if audio is provided
    if audio_filepath:
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
    
    # Analyze image if provided
    if image_filepath:
        combined_query = system_prompt + " " + speech_to_text_output
        doctor_response = analyze_image_with_query(
            query=combined_query,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    # Generate unique filenames for audio to allow multiple replays
    timestamp = int(time.time())
    mp3_file = f"doctor_response_{timestamp}.mp3"
    wav_file = f"doctor_response_{timestamp}.wav"

    # Generate doctor's voice
    voice_of_doctor_mp3, voice_of_doctor_wav = text_to_speech_with_gtts(
        input_text=doctor_response,
        out_filepath_mp3=mp3_file,
        out_filepath_wav=wav_file
    )

    # Return speech text, doctor's text, and audio path (play/replay available)
    return speech_to_text_output, doctor_response, voice_of_doctor_mp3


# Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Record your voice"),
        gr.Image(type="filepath", label="Upload your skin image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice (Replayable)")
    ],
    title="AI Doctor with Vision and Voice",
    description="Upload a skin image and speak your symptoms. Listen to the doctor's advice using the play/replay button."
)

# Launch on Render using the PORT environment variable
iface.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860)),  # ensures compatibility with Render
    share=True
)
