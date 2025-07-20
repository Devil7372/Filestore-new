import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))
CHANNELS = list(map(int, os.getenv("CHANNELS", "").split(",")))
USE_SHORTENER = os.getenv("USE_SHORTENER", "False").lower() == "true"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", 8080))
