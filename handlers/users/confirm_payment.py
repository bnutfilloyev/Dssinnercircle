from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import CHANEL, GROUP_ID, ADMINS
from data.text import text
from loader import dp, bot
from utils.database import database
from utils.db_api.mongo import user_db
from utils.paypal import check_status_paypal
from utils.stripe import check_status_stripe


@dp.callback_query_handler(text='confirm_stripe')
async def confirm_stripe(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    async with state.proxy() as data:
        status = await check_status_stripe(str(data['intenet_id']))
        if status == 'succeeded':
            print(data.as_dict())
            await call.message.edit_text("Congratulations! {}".format(await bot.export_chat_invite_link(GROUP_ID)))
            await state.finish()
            for admin in ADMINS:
                data = user_db.find_one({'telegram_id': call.message.from_user.id})
                bot.send_message(admin, text['user_status'].format(data['days'], data['status']))
            try:
                await database(data, call.from_user.id)
            except Exception as ex:
                await dp.bot.send_message(CHANEL, str(ex))
        else:
            print(data.as_dict())
            await call.message.edit_text("You not payed!")


@dp.callback_query_handler(text='confirm_paypal')
async def check_paypal(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    async with state.proxy() as data:
        pay_id = data['pay-id']

        status = await check_status_paypal(pay_id)
        if status:
            try:
                await database(data, call.from_user.id)
            except Exception as ex:
                await dp.bot.send_message(CHANEL, str(ex))
            for admin in ADMINS:
                data = user_db.find_one({'telegram_id': call.message.from_user.id})
                bot.send_message(admin, text['user_status'].format(data['days'], data['status']))

            await call.message.edit_text("Congratulations! {}".format(await bot.export_chat_invite_link(GROUP_ID)))
            await state.finish()
        else:
            await call.message.edit_text("Ainda não efectuou o pagamento")
