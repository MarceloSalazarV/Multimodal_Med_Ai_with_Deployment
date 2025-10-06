# 🩺 Multimodal-Med-AI → Your AI Doctor Assistant

MediBot 2.0 is an AI-powered doctor assistant that leverages speech recognition, text-to-speech, and multimodal large language models to analyze patient images and voice inputs. The system provides a simulated doctor's response both as text and synthesized speech.

---

## 🔗 Repository Link
[https://github.com/Prerna77Arora/Multimodal_Med_Ai_with_Deployment](https://github.com/Prerna77Arora/Multimodal_Med_Ai_with_Deployment)

## 🌍 Live Demo (Render Deployment)
Experience the app online here:  
👉 [https://multimodal-med-ai.onrender.com](https://multimodal-med-ai.onrender.com)


---

## 🚀 Key Features

- **🎙️ Speech-to-Text**: Converts patient voice input to text using Whisper via Groq API.
- **🖼️ Image Analysis**: Analyzes uploaded patient images for medical concerns using a multimodal LLM (Llama-4 Vision via Groq API).
- **🔊 Text-to-Speech**: Converts AI-generated responses into speech with Google Text-to-Speech (gTTS).
- **🌐 Gradio Web Interface**: User-friendly web interface for uploading images and recording voice.

---

## 📁 Project Structure

```
.env
brain_of_the_doctor.py
voice_of_the_doctor.py
voice_of_the_patient.py
gradio_app.py
requirements.txt
apt.txt
```
---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/Prerna77Arora/Multimodal_Med_Ai_with_Deployment.git
cd Multimodal_Med_Ai_with_Deployment
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with your API keys:

```
GROQ_API_KEY="your_groq_api_key"
ELEVENLABS_API_KEY="your_elevenlabs_api_key"
```

> The `.env` file should not be shared publicly.

### 4. Install System Dependencies

- **ffmpeg** and **portaudio** are required for audio processing.
- **Windows**: Download [ffmpeg](https://ffmpeg.org/download.html) and add it to your PATH.
- **Linux/macOS**: Install via package manager:
```sh
sudo apt install ffmpeg portaudio19-dev
```

### 5. Run the Gradio App

```sh
python gradio_app.py
```

The app will launch at [http://127.0.0.1:7860](http://127.0.0.1:7860).

---

## 🧱 Deploy on Render

1. Push your code to GitHub.  
2. Go to [Render.com](https://render.com) → **New Web Service**.  
3. Connect your GitHub repo:  
   `https://github.com/Prerna77Arora/Multimodal_Med_Ai_with_Deployment`
4. In **Environment Variables**, add:
   - `GROQ_API_KEY`
   - `ELEVENLABS_API_KEY` (optional)
5. In **Build Command**, enter:
   ```
   pip install -r requirements.txt
   ```
6. In **Start Command**, enter:
   ```
   python gradio_app.py
   ```
7. Wait for Render to deploy — once complete, visit your live URL! 🎉

---

## 🧪 How to Use

1. **Open the Gradio Web Interface.**  
2. **Record your voice** using the microphone input.  
3. **Upload a patient image** (e.g., skin photo).  
4. **Submit** to receive:
   - Transcribed speech.
   - Doctor’s medical response.
   - Audio playback of the response.
  
### 🔍 Example Interaction

#### Input

- **Voice**: "I have some redness on my cheek. Can you tell me what it is?"
- **Image**: Upload a clear photo of your face.

#### Output

- **Speech to Text**: "I have some redness on my cheek. Can you tell me what it is?"
- **Doctor's Response**: "With what I see, I think you have mild skin irritation possibly due to an allergic reaction, and keeping the area clean with gentle skincare should help."
- **Doctor's Voice**: (Audio playback of the above response)


---

## 📝 File Descriptions

| File | Description |
|------|--------------|
| `gradio_app.py` | Main Gradio app orchestrating the entire workflow. |
| `brain_of_the_doctor.py` | Image analysis and LLM query logic. |
| `voice_of_the_patient.py` | Speech-to-text logic using Groq API. |
| `voice_of_the_doctor.py` | Text-to-speech logic using gTTS. |
| `.env` | Stores API keys (excluded from version control). |
| `requirements.txt` | Python dependencies. |
| `apt.txt` | System-level dependencies for Render. |

---
## 🎛️ Customization

- **Change the system prompt** in [`gradio_app.py`](gradio_app.py) to adjust the doctor's persona or response style.
- **Switch models** by editing the model names in [`brain_of_the_doctor.py`](brain_of_the_doctor.py) and [`voice_of_the_patient.py`](voice_of_the_patient.py).

## ❗Troubleshooting

- Ensure your API keys are valid and have sufficient quota.
- Make sure `ffmpeg` and `portaudio` are installed and accessible.
- If you encounter microphone or audio device errors, check your system permissions.

## ⚠️ Disclaimer

This project is for **educational purposes only** and does **not provide real medical advice**.  
Always consult a licensed doctor for medical diagnosis or treatment.

---

© 2025 Prerna Arora – All Rights Reserved.
