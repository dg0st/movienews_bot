import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Например: '@yourchannelname'
RSS_URL = os.getenv("RSS_URL", "https://news.google.com/rss/search?q=action+movies&hl=en&gl=US&ceid=US:en")
KEYWORDS = ["action", "боевик", "thriller", "экшн"]
