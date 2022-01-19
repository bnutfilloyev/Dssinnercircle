from aiogram import types
from aiogram.dispatcher.filters import Command

from data.text import text
from filters import IsPrivate
from loader import dp
from utils.db_api.mongo import user_db, transaction_db


@dp.message_handler(IsPrivate(), Command('subscrever', prefixes='/!'))
@dp.message_handler(IsPrivate(), text='Status')
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
        await msg.answer("Você não tem subscrições no momento.")


@dp.message_handler(IsPrivate(), Command('status', prefixes='/!'))
async def check_status_user(msg: types.Message):
    data = user_db.find_one({'telegram_id': msg.from_user.id})
    await msg.answer(text['user_status'].format(data['days'], data['status']))
