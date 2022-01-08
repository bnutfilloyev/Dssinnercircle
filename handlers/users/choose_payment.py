from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.text import text
from keyboards.inline.pay_button import payment_button
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp, bot
from utils.paypal import create_token_paypal, check_status_paypal
from utils.stripe import create_link_stripe, check_status_stripe


@dp.callback_query_handler(text='paypal')
async def paypal(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        token = await create_token_paypal(data['plans_price'], bot_name)
        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="🅿️Subscribe", url=f'https://www.paypal.com/checkoutnow?token={token[0]}'),
                InlineKeyboardButton(text='Confirm', callback_data='confirm_paypal')
            ]
        ])
        data['pay-id'] = token[-1]
        await call.message.answer(text=text['pay_text'], reply_markup=pay_button)


@dp.callback_query_handler(text='confirm_paypal')
async def check_paypal(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        pay_id = data['pay-id']
        status = await check_status_paypal(pay_id)
        if status:
            await call.message.edit_text("Congratulations!")
            await state.finish()
        else:
            await call.message.edit_text("You not payed!", reply_markup=payment_button)


@dp.callback_query_handler(text='stripe')
async def stripe(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        link = await create_link_stripe(data['plans_price'] * 100, bot_name)
        print(link)
        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="🅿️Subscribe", url=link[0]),
                InlineKeyboardButton(text='Confirm', callback_data='confirm_stripe')
            ]
        ])
        data['intenet_id'] = link[-1]
        await call.message.answer(text=text['pay_text'], reply_markup=pay_button)


@dp.callback_query_handler(text='confirm_stripe')
async def confirm_stripe(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        status = await check_status_stripe(str(data['intenet_id']))
        if status == 'succeeded':
            await call.message.edit_text("Congratulations!")
            await state.finish()
        else:
            await call.message.edit_text("You not payed!")


@dp.callback_query_handler(text='back')
async def back_button(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=plansMenu)
    await call.answer()
