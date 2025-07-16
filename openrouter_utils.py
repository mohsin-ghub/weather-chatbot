import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config.get("OPENROUTER_API")

def extract_city(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who extracts city names from user input."},
            {"role": "user", "content": f"Extract the city name from this sentence:\n'{user_input}'\nReply only with the city name."}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"City not found. Error: {e}"
    else:
        return f"Error: {response.status_code} - {response.text}"
