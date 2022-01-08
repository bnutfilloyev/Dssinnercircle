from aiogram import types

from data.text import text
from keyboards.default.main_keyboards import main_button
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp

@dp.message_handler(text='Plans')
async def get_plans(m: types.Message):
    await m.answer(text=text['plan'], reply_markup=plansMenu)

