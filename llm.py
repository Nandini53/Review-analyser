import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("DEBUG KEY:", os.getenv("OPENROUTER_API_KEY"))  # debug

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),   # ✅ FIXED
    base_url="https://openrouter.ai/api/v1"
)

def summarize_review(text):
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "Give short sentiment (Positive/Negative/Neutral)."},
                {"role": "user", "content": text}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"