from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.config import MODE, CLIEND_ID, CLIENT_SECRET, CHANEL
from data.text import text
from keyboards.inline.plan_keyboards import plansMenu
from loader import dp, bot
from utils.paypal import create_token
from utils.stripe import create_link, check_pay


@dp.callback_query_handler(text='paypal')
async def paypal(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        token = await create_token(data['plans_price'], bot_name)
        pay_button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="🅿️Subscribe", url=f'https://www.paypal.com/checkoutnow?token={token}')
            ]
        ])
        await call.message.answer(text=text['pay_text'], reply_markup=pay_button)


@dp.callback_query_handler(text='stripe')
async def stripe(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        bot_name = dict(await bot.get_me())['username']
        link = await create_link(data['plans_price'] * 100, bot_name)
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
        status = await check_pay(str(data['intenet_id']))
        if status == 'succeeded':
            await call.message.edit_text("Congratulations!")
        else:
            await call.message.edit_text("You not payed!")


@dp.callback_query_handler(text='back')
async def back_button(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=plansMenu)
    await call.answer()
