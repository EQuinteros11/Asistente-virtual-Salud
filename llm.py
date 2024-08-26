import openai
import json

#Clase para utilizar cualquier LLM para procesar un texto
#Y regresar una funcion a llamar con sus parametros
#Uso el modelo 0613, pero puedes usar un poco de
#prompt engineering si quieres usar otro modelo
class LLM():
    def __init__(self):
        pass
    def Funciones(self, text):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= [{"role": "system", "content": "Eres un asistente virtual empático, cuidadoso y profesional, utiliza las tools para ayudar al usuario"},
            {"role": "user", "content": text}],
            functions= [
                {
                    "name": "open_chrome",
                    "description": "Abrir una pestaña de choome en un sitio específico",
                    "parameters":{
                        "type": "object",
                        "properties":{
                            "website":{
                                "type": "string",
                                "description": "El sitio al cual se desea ir"
                            }
                        }
                            
                    }
                },
                 {
                    "name": "know_patient_data",
                    "description": "verificar el expediente del paciente",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "fist_name": {
                                "type": "string",
                                "description": "el primer nombre del paciente",
                            },
                            "second_name": {
                                "type": "string",
                                "description": "el segundo nombre del paciente",
                            },
                            "first_surname": {
                                "type": "string",
                                "description": "el primer apellidos del paciente",
                            },
                             "second_last_name": {
                                "type": "string",
                                "description": "el segundo apellido del paciente",
                            },

                        },
                        "requiered":[]
                    },
                },

            ],
            function_call="auto"
        )
        return response
    
            