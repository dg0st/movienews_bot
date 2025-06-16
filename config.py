import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("7350949932:AAE1Vc5AkV3C845gCsduwJjh8iSWY0kBU2w")
CHANNEL_ID = os.getenv("@plasticcult")  # Например: '@yourchannelname'
RSS_URL = os.getenv("https://fight-films.info", "https://news.google.com/rss/search?q=action+movies&hl=en&gl=US&ceid=US:en")
KEYWORDS = ["action", "боевик", "thriller", "экшн"]
