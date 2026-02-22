
import logging
import signal
log = logging.getLogger(__name__)

from usrbot import Config
from usrbot.bot.main import main # async


from hydrogram import Client, filters, __version__ as pyro_version
from hydrogram.enums import ParseMode

import functools
# import schedule # https://schedule.readthedocs.io/en/stable/
# import time
import asyncio






config = Config()
log.info(f"Im runnioing from : {__name__} ... Done") 

# print(config.session_string)



# @lambda _: _() 
# def greet():
#     print(f"Greet from {__name__}")

sessio_string: str = config.session_string
if not sessio_string:
    raise ValueError("No string session provided")

log.info("Session string is set")

class UsrBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        print(f"Init from {name}: v{pyro_version} ... Done")

        super().__init__(
            # ":memory:",
            name,
            session_string=sessio_string,

            # parse_mode=ParseMode.MARKDOWN,

            plugins=dict(root=f"{name}/plugins"),
            sleep_threshold=10,
            max_concurrent_transmissions=5
        )

    
    async def start(self):


        loop = asyncio.get_running_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(
                sig,
                lambda: asyncio.create_task(
                    self.shutdown(sig)
                )
            )


        await super().start()
        # schedule.every(1).minutes.do(await self.restart())

        for func in _autostart_func:
            try:
                await func()
            except Exception as e:
                log.error(f"Autostart func {func.__name__} error: {e}")


        await main() if config.bot_token != '' else log.warning("BOT_TOKEN don't set! Starting without BOT")



        print("Start from {self.__class__.__name__} ... Done")
        usr_bot_me = await self.get_me()


        print("\n\n")
        print(" ############## START ##############")
        print(f"Pyrogram version: {pyro_version}")
        print(f"Bot started. User username: {usr_bot_me.username}")


 
    async def stop(self):
        await super().stop()
        print(f"Stop from {self.__class__.__name__} ... Done")
        print(" ############## STOP ##############")
        print("Bot stopped. Bye.")



    @classmethod
    async def restart(self):
        print(f"Restart from {self.__class__.__name__} ... Done")
        
        await super().stop()
        await asyncio.sleep(2)

        await self.start()





    async def shutdown(self, signal=None):
        log.info(f"Received exit signal {signal.name if signal else 'unknown'}....")
        await self.stop()

        tasks = [
            t for t in asyncio.all_tasks() if t is not asyncio.current_task()
        ]

        [task.cancel() for task in tasks]

        await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        asyncio.get_event_loop().stop()

def test():
    print("Test from {__name__} ... Done")

_autostart_func = []
def autostart(func):
    @functools.wraps(func)

    def wrapper(*args, **kwargs):
        log.critical(f"start func {func.__name__}")
        return func(*args, **kwargs)
    
    _autostart_func.append(wrapper)
    return wrapper

