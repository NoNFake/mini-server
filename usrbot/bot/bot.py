from decouple import config

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message



import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


TOKEN: str = config("BOT_TOKEN", default=None)
if TOKEN == '':
    print("Enter ur TOKEN in .env")


logging.info(f"TOKEN: {TOKEN}\n")


chat_id = 897794210
dp = Dispatcher()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
