import os
from dotenv import load_dotenv

load_dotenv()

SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify', 
    'https://www.googleapis.com/auth/calendar'
]

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TIMEZONE = os.getenv("TIMEZONE", "Europe/Madrid")