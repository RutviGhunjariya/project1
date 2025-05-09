from gtts import gTTS

def generate_speech(text, output_path):
    tts = gTTS(text)
    tts.save(output_path)
