import requests

from decouple import config

ELEVEN_LABS_KEY = config("ELEVEN_LABS_API_KEY")

# eleven labs
# convert text to speech

def convert_text_to_speech(message):

    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }

    voice_britney = "jsCqWAovK2LkecY7zXl4"