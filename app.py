from aiogram import executor
import asyncio
import aioschedule

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def noon_print():
    print("It's noon!")

async def scheduler():
    # aioschedule.every().day.at("16:09").do(noon_print)
    aioschedule.every().minute.do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dispatcher):
    # configure default command
    await set_default_commands(dispatcher)

    # Notify on startup
    await on_startup_notify(dispatcher)

    # schedule user ban
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
