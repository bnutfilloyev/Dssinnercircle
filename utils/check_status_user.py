import asyncio

from data.config import CHANEL, ADMINS
from data.text import text
from handlers.groups.moderator import ban_member
from loader import bot
from utils import on_startup_notify
from utils.db_api.mongo import user_db


async def check_status_user():
    data = user_db.find()
    for i in data:
        if not i['status']:
            await bot.send_message(i['telegram_id'], text=text['kick_notification_user'])
            await asyncio.sleep(100)
            for admin in ADMINS:
                await bot.send_message(admin, text=text['kick_notification_admin'])
            await bot.send_message(CHANEL, text=text['kick_notification_admin'])
            await ban_member()

        else:
            user_db.update_one({'telegram_id': i['telegram_id']}, {
                "$set": {
                    'days': i['days'] - 1
                }
            })

