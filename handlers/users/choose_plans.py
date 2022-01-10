import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from filters import IsPrivate
from keyboards.inline.pay_button import payment_button
from loader import dp
from data.text import plans_price, text, plans_name, billing_period
from data.config import GROUP_NAME, BILLING_MODE


@dp.callback_query_handler(IsPrivate(), text='plans:month')
async def month_plan(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[0], GROUP_NAME, plans_price[0], billing_period[0], BILLING_MODE),
                                     reply_markup=payment_button)
        data['plans_price'] = plans_price[0]
        data['plan'] = 'month'
        data['days'] = 30


@dp.callback_query_handler(IsPrivate(), text='plans:half_year')
async def half_month_plan(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[1], GROUP_NAME, plans_price[1], billing_period[1], BILLING_MODE),
                                     reply_markup=payment_button)
        data['plans_price'] = plans_price[1]
        data['plan'] = 'half_year'
        data['days'] = 183



@dp.callback_query_handler(IsPrivate(), text='plans:year')
async def year_plan(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[2], GROUP_NAME, plans_price[2], billing_period[2], BILLING_MODE),
                                     reply_markup=payment_button)
        data['plans_price'] = plans_price[2]
        data['plan'] = 'year'
        data['days'] = 365

