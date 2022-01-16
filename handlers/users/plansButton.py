from aiogram import types

from data.text import text
from filters import IsPrivate
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp

@dp.message_handler(IsPrivate(), commands='planos')
@dp.message_handler(IsPrivate(), text='Plans')
async def get_plans(m: types.Message):
    await m.answer(text=text['plan'], reply_markup=plansMenu)

