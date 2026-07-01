import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")