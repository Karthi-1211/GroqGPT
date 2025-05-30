import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell a joke",
        }
    ],
    model="gemma2-9b-it",
)

print(chat_completion.choices[0].message.content)