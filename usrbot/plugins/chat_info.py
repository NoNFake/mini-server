__command__ = ".chat_info"
__info__ = "`.chat_info chat_id, "


from hydrogram import filters
from ..usrbot import UsrBot
import logging
from pathlib import Path

import random 

log = logging.getLogger(__name__)




@UsrBot.on_message(filters.command("chat_info", prefixes=".") & (filters.me | filters.private))
async def status(client, message):
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)


    try:
        if chat:
            await message.reply_text(f"```chat info\n{chat}```")
    except:
        if chat:
            await message.reply_text(f"```chat info\n{chat.id}```")
    # if coin and coin.strip():
    #     for i in range(5):
    #         await message.reply_text(coin)
            

    # try:
    #     await message.reply_text(f"```{coin}```")
    # except Exception as e:
    #     await message.reply_text(f"Error: {e}")
    



