from config import BOT_TOKEN, CHANNEL_ID, RSS_URL
from telegram import Bot
import asyncio
from fetcher import fetch_news
from filter import is_relevant

bot = Bot(token=BOT_TOKEN)

async def main():
    articles = fetch_news()
    for article in articles:
        if is_relevant(article):
            message = f"📰 <b>{article['title']}</b>\n{article['link']}"
            await bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode='HTML')

if __name__ == "__main__":
    asyncio.run(main())
