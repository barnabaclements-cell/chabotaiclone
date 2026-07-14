import traceback

from groq import Groq
from django.conf import settings

print("=" * 50)
print("GROQ KEY EXISTS:", bool(settings.GROQ_API_KEY))
print("=" * 50)

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def ask_groq(messages):

    try:

        print("Sending to Groq...")
        print(messages)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        print("Groq Success")

        return response.choices[0].message.content

    except Exception as e:

        print("=" * 80)
        print("GROQ ERROR")
        print(e)
        traceback.print_exc()
        print("=" * 80)

        raise