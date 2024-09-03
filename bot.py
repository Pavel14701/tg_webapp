import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command
from aiogram.fsm.storage.redis import RedisStorage
import asyncio
from os import getenv
from dotenv import load_dotenv
import redis.asyncio as redis

load_dotenv()

API_TOKEN = getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)


redis_client = redis.Redis(host=getenv('REDIS_HOST'), port=int(getenv('REDIS_PORT')), db=int('REDIS_DB'))
storage = RedisStorage(redis_client)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)

@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    web_app = WebAppInfo(url="https://your-web-app-url.com")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Open Web App", web_app=web_app))
    await message.answer("Welcome! Click the button below to open the Web App.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())