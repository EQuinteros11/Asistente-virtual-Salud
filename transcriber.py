import openai

class Transcriber:
 def __init__(self) :
   pass
 def transcribe(self, audio):
    audio.save("audio.mp3")
    audio_file = open("audio.mp3", "rb")
    transcrit = openai.audio.transcriptions.create(
    file = audio_file,
    model="whisper-1",  # Modelo Whisper de OpenAI
    language="es"       # Especificar español como el idioma
    )
    return transcrit.text