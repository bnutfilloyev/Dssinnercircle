import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher, text='SubhonAlloh'):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)

        except Exception as err:
            logging.exception(err)
