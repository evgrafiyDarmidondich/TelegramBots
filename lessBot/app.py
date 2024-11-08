import asyncio
import os

from aiogram.client.default import DefaultBotProperties

from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from lessBot.common.bot_cmds_list import privat
from lessBot.database.engine import create_db, drop_db
from lessBot.hendlers.admin_privat import admin_router
from lessBot.hendlers.user_group import user_group_router

load_dotenv()

from lessBot.hendlers.user_privat import user_private_router


TOKEN = os.getenv('TOKEN')

# список разрешоных обновлений
ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []



dp = Dispatcher()
# подключение роутера
dp.include_router(admin_router)
dp.include_router(user_private_router)
dp.include_router(user_group_router)

async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()

    await create_db()

async def on_shutdown(bot):
    print('Бот лёг')


# функция запуска бота
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Запуск создания базы данных
    await create_db()
    # Сбрасывает ожидаеме обновления
    await bot.delete_webhook(drop_pending_updates=True)
    # вызов програмных кнопок меню
    await bot.set_my_commands(commands=privat, scope=BotCommandScopeAllPrivateChats())

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

# Вызвали функцию запуска бота
asyncio.run(main())