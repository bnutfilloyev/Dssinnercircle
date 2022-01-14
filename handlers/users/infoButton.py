from aiogram import types

from data.text import text
from filters import IsPrivate
from loader import dp

@dp.message_handler(IsPrivate(), text='ℹ️Info')
async def get_plans(m: types.Message):
    await m.answer(text=text['info'])

