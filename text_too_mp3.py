import os
import requests
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
ELEVENLABS_API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
AUDIO_FILE_PATH = "audio/sample.mp3"

with open("text_for_all_cals.txt", "r", encoding="utf-8") as file:
    TEXT = file.read()


# Параметри запиту
headers = {
    "Content-Type": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY
}

data = {
    "text": TEXT,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8
    }
}

# Виконуємо запит до API
response = requests.post(ELEVENLABS_API_URL, json=data, headers=headers)

# Перевіряємо, чи все пройшло успішно
if response.status_code == 200:
    # Зберігаємо отримане аудіо у файл
    with open(AUDIO_FILE_PATH, "wb") as file:
        file.write(response.content)
    print("Аудіофайл успішно збережено як sample.mp3")
else:
    print(f"Помилка: {response.status_code}, {response.text}")

