from gtts import gTTS

def generate_voice(text, filename="voice.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename
