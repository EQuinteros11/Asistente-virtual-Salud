import os
import openai
from flask import Flask,render_template,request
from dotenv import load_dotenv
import pygame
from transcriber import Transcriber
from llm import LLM
from tts import TTS
from pc_command import PcCommand
import json
from conexion_postgre import Conectar


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("asistente.html")

@app.route("/audio", methods=["POST"])
def audio():
    pygame.mixer.quit() #para iterar en peticiones
    audio = request.files.get("audio")
    text = Transcriber().transcribe(audio)
    print(text)
    responsellm = LLM().Funciones(text)
        # Extraer el nombre de la función
    function_name = responsellm.choices[0].message.function_call.name
        # Extraer los argumentos de la función
    function_arguments = responsellm.choices[0].message.function_call.arguments

    # Mostrar los resultados
    print(f"Nombre de la función: {function_name}")
    print(f"Argumentos: {function_arguments}")

    if function_name is not None:
        if function_name == "open_chrome":
            #llamar a la funcion 
            web = json.loads(function_arguments)
            PcCommand().open_chrome(web['website'])
            final_response = "Listo, ya abrí chrome en el sitio "
            TTS().process(final_response)
            return {"result": "ok", "text": final_response}
        if function_name == "know_patient_data":
            #llamar a la funcion
            web = json.loads(function_arguments)
            final_response = "Tu expediente es " + Conectar.peticion_expediente(web['fist_name'],web['second_name'],web['first_surname'], web['second_last_name'])
            TTS().process(final_response)
            return {"result": "ok", "text": final_response}
    else:
        final_response = "No posseo esa capcidad, analizaremos si es fundamental para garantiza un continuo mejoramiento del servicio, feliz día"
        return {"result": "ok", "content":final_response}
        