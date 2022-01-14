from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import GROUP_ID
from filters import AdminFilter
from loader import dp, bot
from utils.db_api.mongo import user_db

# Test
@dp.message_handler(AdminFilter(), Command('kick', prefixes='!/'))
async def ban_member():
    data = user_db.find()
    for i in data:
        if not i['status']:
            await bot.kick_chat_member(GROUP_ID, i['telegram_id'])

