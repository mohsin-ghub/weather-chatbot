import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/text-bison-001")
else:
    model = None

def extract_city(user_input):
    if not model:
        return "Gemini API key not configured."

    prompt = f"Extract only the city name from this sentence:\n'{user_input}'\nReply with city name only."

    response = model.generate_content(prompt)
    return response.text.strip()
