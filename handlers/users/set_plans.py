import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.text import text
from filters import AdminFilter
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp
from aiogram.dispatcher.filters.state import State, StatesGroup

from utils.db_api.mongo import plans_price_db


class Form(StatesGroup):
    get_text = State()


@dp.message_handler(commands='set_price')
async def set_price(msg: types.Message):
    await msg.answer(text['change_plan_price'])
    await Form.get_text.set()

@dp.message_handler(state=Form.get_text)
async def get_price(msg: types.Message, state: FSMContext):
    get_new_plans = msg.text
    new_plans = get_new_plans.split(',')
    data = plans_price_db.find_one()
    res = plans_price_db.find_one_and_update({}, update={
        '$set':
            {'plans_price': new_plans,
             'plans_days': data['plans_days']}
    }, return_document=True)

    if res:
        print(plansMenu)

        await msg.answer("Success!")
        await state.finish()
    else:
        await msg.answer("Something went wrong! Please try again!")