from google import genai
from dotenv import load_dotenv
from text_to_speech import speak
import os

# Carrega as variáveis do arquivo .env
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

# Cria o client da google 
client =  genai.Client(api_key=API_KEY)

# CHATBOT
print('='*50)
print('🤖 Chatbot Gemini')
print("Digite 'sair' para encerrar.")
print('='*50)

historico =  []

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        print("\n🤖: Até logo.")
        speak("Até logo.")
        break
    # Guardar a mensagem do usuário
    historico.append(
        {
           "role": "user",
           "parts": [{"text":pergunta}] 
        }
    )

    # Resposta do GEMINI 
    resposta = client.models.generate_content(
        model = "gemini-3.1-flash-lite",
        contents = historico
    )

    texto = resposta.text
    # Guarda a resposta do GEMINI 
    historico.append(
        {
            "role": "model",
            "parts": [{"text":texto}]
        }
    )

    print(f"\n🤖:{texto}")
    speak(texto)
