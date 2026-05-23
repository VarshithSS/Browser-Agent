import os

from groq import AsyncGroq
from dotenv import load_dotenv

load_dotenv()

client = AsyncGroq(
    api_key=os.getenv("GROQ_API_KEY")
)


async def get_llm_response(prompt: str):

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an AI browser agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content