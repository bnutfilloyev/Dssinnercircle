from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.text import payment_method

payment_button = InlineKeyboardMarkup(row_width=1)
for value, key in payment_method.items():
    payment_button.insert(InlineKeyboardButton(text=key, callback_data=value))
