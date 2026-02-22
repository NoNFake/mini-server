# __command__ = ".restart"
# __info__ = "Restarts the bot"

from hydrogram import filters
from ..usrbot import UsrBot
import os
import logging
log = logging.getLogger(__name__)




@UsrBot.on_message(filters.command("stop", prefixes="."))
async def stop(_, message):
    log.info("help command received")

    await message.reply_text("Stopping...")
    log.info("Stopping...")

    os.system("bash stop")


