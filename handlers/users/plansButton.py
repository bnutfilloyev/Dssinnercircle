
from aiogram import types
from aiogram.dispatcher.filters import Command

from data.text import text
from filters import IsPrivate
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp
import middlewares

@dp.message_handler(IsPrivate(), Command('planos', prefixes='/!'))
@dp.message_handler(IsPrivate(), text='Planos')
async def get_plans(m: types.Message):
    await m.answer(text=text['plan'], reply_markup=await plansMenu())

