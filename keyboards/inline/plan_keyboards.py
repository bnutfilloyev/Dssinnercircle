from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.text import plans
from keyboards.inline.callback_data import plans_callback


plansMenu = InlineKeyboardMarkup(row_width=1)
for value, key in plans.items():
    plansMenu.insert(InlineKeyboardButton(text=key, callback_data=plans_callback.new(item_name=value)))

