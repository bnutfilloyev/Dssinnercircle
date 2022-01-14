import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from filters import IsPrivate
from keyboards.inline.callback_data import plans_callback
from keyboards.inline.pay_button import payment_button
from loader import dp
from data.text import  text, plans_name, billing_period, price
from data.config import GROUP_NAME, BILLING_MODE


@dp.callback_query_handler(plans_callback.filter(item_name='plan1'))
async def month_plan(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[0],
                                            GROUP_NAME,
                                            price[0],
                                            billing_period[0],
                                            BILLING_MODE),
            reply_markup=payment_button)

        print(callback_data)
        data['plans_price'] = callback_data.get("plan_price")
        data['plan'] = callback_data.get('item_name')
        data['days'] = callback_data.get('days')
        data['currency'] = "EUR"


@dp.callback_query_handler(plans_callback.filter(item_name='plan2'))
async def half_month_plan(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[1],
                                            GROUP_NAME,
                                            price[1],
                                            billing_period[1],
                                            BILLING_MODE),
            reply_markup=payment_button)
        data['plans_price'] = callback_data.get("plan_price")
        data['plan'] = callback_data.get('item_name')
        data['days'] = callback_data.get('days')
        data['currency'] = "BRL"



@dp.callback_query_handler(plans_callback.filter(item_name='plan3'))
async def year_plan(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[2],
                                            GROUP_NAME, price[2],
                                            billing_period[2],
                                            BILLING_MODE),
            reply_markup=payment_button)

        data['plans_price'] = callback_data.get("plan_price")
        data['plan'] = callback_data.get('item_name')
        data['days'] = callback_data.get('days')
        data['currency'] = "EUR"


@dp.callback_query_handler(plans_callback.filter(item_name='plan4'))
async def year_plan(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    async with state.proxy() as data:
        await call.message.edit_text(
            text=text['choose_plan'].format(plans_name[3],
                                            GROUP_NAME, price[3],
                                            billing_period[3],
                                            BILLING_MODE),
            reply_markup=payment_button)

        data['plans_price'] = callback_data.get("plan_price")
        data['plan'] = callback_data.get('item_name')
        data['days'] = callback_data.get('days')
        data['currency'] = "BRL"

