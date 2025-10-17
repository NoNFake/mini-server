from ..usrbot import UsrBot
from pyrogram import filters, enums
from pyrogram.errors import (
    BotInlineDisabled,
    BotResponseTimeout)
from ..sample_config import Config, MessagesTag
import logging
import asyncio

from pathlib import Path


# import random as rnd

log = logging.getLogger(__name__)


word_trigger = r"(?i)^да$"

current = Path(__file__).parent


@UsrBot.on_message( 
    filters.user(1022174802
) & filters.regex(word_trigger)
)


async def ban_words(client, message):
    try:

        name_sticker = 'sticker.webp'
        sticker_file = current / "data" / name_sticker 
        chat_id = message.chat.id
        text_ed = message.text
        log.info(f"word_trigger: {text_ed}, {current}")

        await client.send_sticker(
            chat_id= chat_id,
            sticker=sticker_file
        )
    except Exception as e:
        log.error(f"Error: {e}")
