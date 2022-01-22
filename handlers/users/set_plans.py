
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import text
from keyboards.inline.plan_keyboards import price
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
    res = False
    new_plans = get_new_plans.split('\n')
    if len(new_plans) == 4:
        data = plans_price_db.find_one()
        res = plans_price_db.find_one_and_update({}, update={
            '$set':
                {'plans_price': new_plans,
                 'plans_days': data['plans_days']}
        }, return_document=True, upsert=True)

    if res:
        print(price)
        await msg.answer("Success!")
        await state.finish()
    else:
        await msg.answer("Something went wrong! Please try again!")