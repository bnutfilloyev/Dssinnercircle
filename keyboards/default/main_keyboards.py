from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.text import default_button

main_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=default_button['plan']),
            KeyboardButton(text=default_button['status'])
        ]
    ]
)
