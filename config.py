from dotenv import load_dotenv
import os

load_dotenv() 

BOT_TOKEN = os.getenv("BOT_TOKEN")
RSS_URL = os.getenv('RSS_URL')
CHANNEL_ID = os.getenv("CHANNEL_ID")
KEYWORDS = ["action", "боевик", "gunfight", "explosion", "chase", "military", "shootout"]

print("BOT_TOKEN:", BOT_TOKEN) 