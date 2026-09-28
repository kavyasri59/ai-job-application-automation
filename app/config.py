import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AI Job Application Automation"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
