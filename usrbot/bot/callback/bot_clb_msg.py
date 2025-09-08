from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
# from aiogram.utils.chat_action import ChatActionSender

# from keyboards.outline import main_kb
from ..keyboards.inline import bright_inline_kb 
from ..stats import get_bat, get_bright, get_mem, set_bright, get_full

cbl_router = Router()


# Set bright
@cbl_router.callback_query(F.data.startswith('set_'))
async def cmd_set_brght(call: CallbackQuery):

    bright = str(call.data.replace('set_', ''))
    print(bright)

    # async with ChatActionSender()
    await call.message.answer(
        text=set_bright(bright),
        reply_markup=bright_inline_kb()
    )

