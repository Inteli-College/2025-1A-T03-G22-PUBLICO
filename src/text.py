import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SITE_URL = os.getenv("YOUR_SITE_URL")
SITE_NAME = os.getenv("YOUR_SITE_NAME")


response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "<YOUR_SITE_URL>",
    "X-Title": "<YOUR_SITE_NAME>",
  },
  data=json.dumps({
    "model": "openai/gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life? In 10 words, please"
      }
    ]
  })
)

print(response.json())  # Para visualizar a resposta da API
