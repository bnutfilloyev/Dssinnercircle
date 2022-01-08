from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import text
from keyboards.default.main_keyboards import main_button
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(m: types.Message):
    await m.answer(f"Hey, <b>{m.from_user.full_name}!</b>", reply_markup=main_button)
    await m.answer(text=text['plan'], reply_markup=plansMenu)

