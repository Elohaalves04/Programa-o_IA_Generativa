from gtts import gTTS
import pygame
import os

def speak(texto):
    tts = gTTS(text=texto, lang='pt-br')
    arquivo = "voz.mp3"

    try:
        os.remove(arquivo)
    except OSError:
        pass

    tts.save(arquivo)


    pygame.mixer.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.music.unload()

