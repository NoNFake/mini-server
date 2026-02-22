# __command__ = ".preload"
# __info__ = "`.preload Show memmory of prelaod"



from hydrogram import filters
from ..usrbot import UsrBot
import logging
from sys import getsizeof


log = logging.getLogger(__name__)



stiker_cache = None




# @UsrBot.on_message(filters.command("preload", prefixes=".") & (filters.me | filters.private))
# async def preloader(client, message):
#     try: 
#         await message.reply_text(f)
# @autostart
# async def starter():
