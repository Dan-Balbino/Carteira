import os
import google.generativeai as genai
from dotenv import load_dotenv

from Pasta_IA.Config_IA import modelo_IA

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

modelo = modelo_IA

chat_session = modelo.start_chat(enable_automatic_function_calling=True, history=[])

while True:
  try:
    response = chat_session.send_message(input(": "))
    print(response.text)
  except Exception:
    print("Ocorreu um erro.")