from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder    


def bright_inline_kb():
    bright_bt = [
        [InlineKeyboardButton(text='0', callback_data='set_0'),
        InlineKeyboardButton(text='50', callback_data='set_50'),
        InlineKeyboardButton(text='100', callback_data='set_100')],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=bright_bt)
    return keyboard