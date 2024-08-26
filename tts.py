import os
from flask import Flask,render_template,request
from gtts import gTTS
import pygame
import openai
class TTS():
    def __init__(self) -> None:
        pass
    def process(self, text):
            
        tts = gTTS(text, lang='es')
        tts.save("response.mp3")
        # Inicializar el mezclador de sonido
        pygame.mixer.init()

        # Cargar el archivo de sonido
        pygame.mixer.music.load("response.mp3")

        # Reproducir el sonido
        pygame.mixer.music.play()
        # Esperar hasta que termine el sonido