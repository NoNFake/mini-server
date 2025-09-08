from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_kb():

    main_bt = [ 

        [KeyboardButton(text="get battery"),
        KeyboardButton(text="get bright")],
        [KeyboardButton(text="get mem"),
        KeyboardButton(text="set bright")],
        [KeyboardButton(text="full stat")]

    ]


    keyboard = ReplyKeyboardMarkup(keyboard=main_bt, resize_keyboard=True)
    return keyboard


