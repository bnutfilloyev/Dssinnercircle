from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import GROUP_ID, ADMINS
from filters import AdminFilter, IsGroup
from loader import dp, bot
from utils.db_api.mongo import user_db

# Test
@dp.message_handler(AdminFilter(), Command('kick', prefixes='!/'))
async def ban_member():
    data = user_db.find()
    for i in data:
        if not i['status']:
            await bot.kick_chat_member(GROUP_ID, i['telegram_id'])


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    for i in ADMINS:
        bot.send_message(i, f"A new user has been added to the group. {members}")
