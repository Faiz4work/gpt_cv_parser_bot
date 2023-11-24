from openai import OpenAI
import pdfplumber
import re
from pprint import pprint
from api_key import api_key

def send_message(message):
    # OpenAI API key
    open_api_key = api_key
    client = OpenAI(
        api_key=open_api_key,
    )

    messages = []

    messages.append({'role': 'user', 'content': message})

    # request gpt 3.5 turbo for chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    chat_message = response.choices[0].message.content

    return chat_message




