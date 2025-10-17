from ..usrbot import UsrBot, autostart
from pyrogram import filters, enums
from pyrogram.errors import (
    BotInlineDisabled,
    BotResponseTimeout)
from ..sample_config import Config, MessagesTag
import logging
import asyncio

from pathlib import Path


from io import BytesIO 
# import random as rnd

log = logging.getLogger(__name__)


word_trigger = r"(?i)^да$"




test = 8447053567
target = 1022174802




sticker_cache = None
sticker_file_id = "CAACAgIAAxkDAAIQoWjyloabRHkB2CYhpbNu15KP-LeqAAK0jAACptuYS8tDK8a8BfUuHgQ"

@autostart
async def on_start():
    global sticker_cache

    current = Path(__file__).parent
    name_sticker = 'sticker.webp'
    sticker_file = current / "data" / name_sticker 

    with open(sticker_file, "rb") as f: 
        sticker_cache = BytesIO(f.read())
    

    sticker_cache.name = name_sticker
    log.warning("preload sticker")
    log.warning(f"sticker_cache size: {sticker_cache.getbuffer().nbytes} bytes")




@UsrBot.on_message( 
    filters.user(1022174802) & filters.regex(word_trigger)
)


async def ban_words(client, message):
    global sticker_file_id 
    try:
        
        chat_id = message.chat.id

        if sticker_file_id:
            await client.send_sticker(
            chat_id= chat_id,
            sticker=sticker_file_id
        )
        else: 
            sticker_cache.seek(0)
            sent_message = await client.send_sticker(
                chat_id= message.chat.id,
                sticker=sticker_cache
            )

            # Cache the file_id for future use
            sticker_file_id = sent_message.sticker.file_id
            log.info(f"Cached sticker_file_id: {sticker_file_id}")

            

        # chat_id = message.chat.id
        # text_ed = message.text
        # log.info(f"word_trigger: {text_ed}, {sticker_cache}")

        # await client.send_sticker(
        #     chat_id= chat_id,
        #     sticker=sticker_cache
        # )


    except Exception as e:
        log.error(f"Error: {e}")
