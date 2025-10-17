__command__ = ".coin"
__info__ = "`.coin For best choice Yes/No"


from pyrogram import filters
from ..usrbot import UsrBot
import logging
from pathlib import Path

import random as rnd
import time
import asyncio

log = logging.getLogger(__name__)






@UsrBot.on_message(filters.command("coin", prefixes=".") & (filters.me | filters.private))
async def status(client, message):
    coin = rnd.choice(['Yes', 'No'])
    chat_id = message.chat.id
    

    hash_syb = "@#$%&*"
    str = ""

    def hash_gen(x: int = 2):
        hash_str = ""
        for i in range(x):
            hash_str += rnd.choice(hash_syb)

        return hash_str


    for i in hash_gen():
        for j in hash_syb:

            # print(f"{str +j}")

            await client.edit_message_text(
                chat_id=chat_id,
                message_id=message.id,
                text=f"{str +j}"
            )

            if j == i or j == "":
                str += j
            # time.sleep(0.1)
            await asyncio.sleep(0.1)
    
    coin = rnd.choice(["yes", "no"])
    await client.edit_message_text(
                chat_id=chat_id,
                message_id=message.id,
                text=coin
            )
    # if coin and coin.strip():
    #     for i in range(5):
    #         await message.reply_text(coin)
            

    # try:
    #     await message.reply_text(f"```{coin}```")
    # except Exception as e:
    #     await message.reply_text(f"Error: {e}")
    



