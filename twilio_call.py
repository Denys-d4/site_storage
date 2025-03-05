from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Twilio конфігурація
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

your_phone_number = "+380665275296"

# Посилання на аудіофайл 
audio_url = "https://denys-d4.github.io/site_storage/audio/sample.mp3"

# Ініціалізація клієнта Twilio
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Виконання дзвінка
call = client.calls.create(
    to=your_phone_number,
    from_=TWILIO_PHONE_NUMBER,
    twiml=f'<Response><Play>{audio_url}</Play></Response>'
)

print(f"Дзвінок ініційовано! SID: {call.sid}")