from ..stats import get_bat
import threading
import time


from ..bot import bot, chat_id
import asyncio


last_notify = 0

async def check_bat():
    # bot.send_message(text=f"ALARM battery: {get_bat}") if int(get_bat) <= 30 else None
    bat = get_bat()
    
    print(bat)
    if bat and bat < 30 and (time.time() - last_notify) > 600:
        try: 
            await bot.send_message(chat_id=chat_id,
                                   text=f"battery: {bat}")
            last_notify = time.time()
        except:
            pass


def schedule_check():
    asyncio.run(check_bat())
