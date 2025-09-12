from decouple import config

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from usrbot import Config

import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

TOKEN = Config.bot_token
chat_id = 897794210
dp = Dispatcher()
bot = None


if TOKEN != '':
    logging.info(f"TOKEN: {TOKEN}\n")


    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
else:
    print("Enter ur TOKEN in .env")



