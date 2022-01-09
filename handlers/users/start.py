from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import text
from keyboards.default.main_keyboards import main_button
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['telegram_id'] = m.from_user.id
        await m.answer(text=text['start_text'].format(m.from_user.full_name), reply_markup=main_button)
        await m.answer(text=text['plan'], reply_markup=plansMenu)
