from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.text import plans_price, price, days
from keyboards.inline.callback_data import plans_callback
from utils.db_api.mongo import plans_price_db


async def plansMenu():
    plansMenu = InlineKeyboardMarkup(row_width=1)
    plans = await plans_price()
    cost = await price()
    for num, (value, key) in enumerate(plans.items()):
        plansMenu.insert(InlineKeyboardButton(text=key,
                                              callback_data=plans_callback.new(item_name=value,
                                                                               plan_price=cost[num],
                                                                               days=days[num],
                                                                               )))
    return plansMenu