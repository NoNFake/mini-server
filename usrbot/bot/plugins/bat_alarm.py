from ..stats import get_bat
import threading
import time


import asyncio


last_notify = 0

async def check_bat():


    try:

        from ..bot import bot, chat_id

        bat = get_bat()
        
        print(bat)
        if bat and bat < 30 and (time.time() - last_notify) > 600:
            try: 
                await bot.send_message(chat_id=chat_id,
                                    text=f"battery: {bat}")
                last_notify = time.time()
            except:
                pass
    except:
        pass


def schedule_check():
    asyncio.run(check_bat())
