from aiogram import types
from aiogram.dispatcher.filters import Command

from data.text import text, default_button
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), Command('info', prefixes='/!'))
@dp.message_handler(IsPrivate(), text=default_button['info'])
async def get_plans(m: types.Message):
    await m.answer(text=text['info'])

