from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import text
from keyboards.default.main_keyboards import main_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hey, <b>{message.from_user.full_name}!</b>", reply_markup=main_button)
    await message.answer(text=text['plan'], )
