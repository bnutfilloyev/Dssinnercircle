import json
import pprint

import paypalrestsdk
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.config import MODE, CLIEND_ID, CLIENT_SECRET, CHANEL
from data.text import text
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp, bot

paypalrestsdk.configure({
    "mode": MODE,
    "client_id": CLIEND_ID,
    "client_secret": CLIENT_SECRET})


@dp.callback_query_handler(text='paypal')
async def paypal(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "redirect_urls": {
                "return_url": f"http://t.me/{bot_name}",
                "cancel_url": f"http://t.me/{bot_name}"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": f"{data['plans_price']}.00",
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {"total": f"{data['plans_price']}.00", "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            await bot.send_message(CHANEL, f"<code>{payment}</code>")
        else:
            await bot.send_message(CHANEL, payment.error)

        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                token = approval_url.split('=')[-1]

        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="🅿️Subscribe", url=f'https://www.paypal.com/checkoutnow?token={token}')
            ]
        ])
        await call.message.answer(text=text['pay_text'], reply_markup=pay_button)

@dp.callback_query_handler(text='stripe')
async def stripe(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer('comming soon...')


@dp.callback_query_handler(text='back')
async def back_button(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=plansMenu)
    await call.answer()
