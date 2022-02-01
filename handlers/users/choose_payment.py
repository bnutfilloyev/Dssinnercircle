from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.text import text, confirm_payment_button_text
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp, bot
from utils.paypal import create_token_paypal
from utils.stripe import create_link_stripe


@dp.callback_query_handler(text='paypal')
async def paypal(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        token = await create_token_paypal(data['plans_price'], bot_name, data['currency'])
        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=confirm_payment_button_text['subscribe'], url=f'https://www.paypal.com/checkoutnow?token={token[0]}'),
                InlineKeyboardButton(text=confirm_payment_button_text['confirm'], callback_data='confirm_paypal')
            ]
        ])
        data['pay-id'] = token[-1]
        data['payment_method'] = 'paypal'
        await call.message.answer(text=text['pay_text'], reply_markup=pay_button)


@dp.callback_query_handler(text='stripe')
async def stripe(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        print(data)
        link = await create_link_stripe(int(float(data['plans_price']) * 100), bot_name, data['currency'], data['plan_type'])
        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=confirm_payment_button_text['subscribe'], url=link[0]),
                InlineKeyboardButton(text=confirm_payment_button_text['confirm'], callback_data='confirm_stripe')
            ]
        ])
        data['intenet_id'] = link[-1]
        data['payment_method'] = 'stripe'
        await call.message.answer(text=text['pay_text'], reply_markup=pay_button)


@dp.callback_query_handler(text='back')
async def back_button(call: CallbackQuery):
    await call.message.edit_text(text=text['plan'], reply_markup=await plansMenu())
    await call.answer("Cancel")
    # await call.answer(cache_time=60)


