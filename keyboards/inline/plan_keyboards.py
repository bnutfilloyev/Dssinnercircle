from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.text import plans_price, price, days
from keyboards.inline.callback_data import plans_callback

plansMenu = InlineKeyboardMarkup(row_width=1)
for num, (value, key) in enumerate(plans_price.items()):
    plansMenu.insert(InlineKeyboardButton(text=key,
                                          callback_data=plans_callback.new(item_name=value,
                                                                           plan_price=price[num],
                                                                           days=days[num],
                                                                           )))
