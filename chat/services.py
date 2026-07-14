from groq import Groq
from django.conf import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def ask_groq(messages):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    return response.choices[0].message.content