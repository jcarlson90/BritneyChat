import openai
from decouple import config

# import custom functions
from functions.database import get_recent_messages

#retrieve environment variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")


# open AI - whisper 
# convert audio to text
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript("text")
        return message_text
    except Exception as e:
        print(e)
        return
    
# Open Ai -ChatGpt
# Get Response to our message
def get_chat_response(message_input):

    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
        model="gtp-3.5-turbo"
        )
        message_text = rresponse["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return