from aiogram import types

from data.text import text
from loader import dp
from utils.db_api.mongo import user_db, transaction_db


@dp.message_handler(text='Status')
async def status_button(msg: types.Message):
    data = user_db.find_one({'telegram_id': msg.from_user.id})
    if data != None:
        textback = ''
        for i in transaction_db.find():
            if i['payment_method'] == 'stripe':
                textback += text['status_text'].format(i['telegram_id'], i['plans_price'], i['plan'], i['days'], i['intenet_id'])
            else:
                textback += text['status_text'].format(i['telegram_id'], i['plans_price'], i['plan'], i['days'], i['pay-id'])

        await msg.answer(textback)
    else:
        await msg.answer("You don't have any active subscriptions at the moment.")