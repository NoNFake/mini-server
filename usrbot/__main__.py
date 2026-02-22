import uvloop
uvloop.install()
import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    
from .usrbot import UsrBot
import logging


log = logging.getLogger(__name__)

log.info(f"{__name__} start...")



    

if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())\
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    
    log.info("Starting bot...")
    UsrBot().run()
    log.info("Bot started")
