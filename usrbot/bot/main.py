import asyncio
import schedule 
import time 

# from handlers import bot_msg
from .handlers.bot_msg import start_router
from .callback.bot_clb_msg import cbl_router


from .plugins.bat_alarm import check_bat, schedule_check


from .bot import bot, dp, chat_id


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp.include_routers(
        start_router,
        cbl_router
    )

    
    
    await bot.send_message(
        chat_id=chat_id,
        text='server started')
    
    


    # And the run events dispatching
    await dp.start_polling(bot)
    schedule.every(1).minutes.do(schedule_check)


# if __name__ == "__main__":
#     asyncio.run(main())
