from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import CHANEL, GROUP_ID
from loader import dp, bot
from utils.database import database
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
            await call.message.edit_text("Congratulations! {}".format(await bot.export_chat_invite_link(GROUP_ID)))
            await state.finish()
        else:
            await call.message.edit_text("You not payed!")
