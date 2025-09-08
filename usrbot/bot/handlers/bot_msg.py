from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from ..keyboards.outline import main_kb
from ..keyboards.inline import bright_inline_kb 
from ..stats import get_bat, get_bright, get_mem, get_full

start_router = Router()



# bat_alarm
# @start_router.message()
# async def bat_alarm(message: Message):
#     await message.answer(
#         text=f"!ALARM! Battery: {get_bat()}"
#     )


# Keyboard
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    # print(message.from_user.id)
    await message.answer(
        text="Hi",
        reply_markup=main_kb()
    )




# Get Battery
@start_router.message(F.text == 'get battery')
async def cmd_bat(message: Message):
    await message.answer(
        text=get_bat()
    )


# Get Bright
@start_router.message(F.text == 'get bright')
async def cmd_bat(message: Message):
    await message.answer(
        text=get_bright()
    )


# Get mem
@start_router.message(F.text == 'get mem')
async def cmd_bat(message: Message):
    await message.answer(
        text=get_mem()
    )


# Set bright
@start_router.message(F.text == 'set bright')
async def cmd_bat(message: Message):
    await message.answer(
        
        text="Enter a number of light (0 - min | 100 - max)",
        reply_markup=bright_inline_kb()
    )


# Full stat
@start_router.message(F.text == 'full stat')
async def cmd_bat(message: Message):
    await message.answer(
        text=get_full()
    )




