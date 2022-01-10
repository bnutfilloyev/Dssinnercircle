from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup, AdminFilter
from loader import dp

@dp.message_handler(IsGroup(), AdminFilter(), Command('check_member'))
async def get_member(msg: types.Message, telegram_id):
    data = await msg.chat.kick(user_id=850500610)
    print(data)
