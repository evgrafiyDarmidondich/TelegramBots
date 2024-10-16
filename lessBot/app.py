import asyncio
import os

from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from lessBot.common.bot_cmds_list import privat
from lessBot.hendlers.user_group import user_group_router

load_dotenv()

from lessBot.hendlers.user_privat import user_private_router


TOKEN = os.getenv('TOKEN')

# список разрешоных обновлений
ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(TOKEN)

dp = Dispatcher()
# подключение 1-го роутера
dp.include_router(user_private_router)
dp.include_router(user_group_router)



# функция запуска бота
async def main():
    # Сбрасывает ожидаеме обновления
    await bot.delete_webhook(drop_pending_updates=True)
    # вызов програмных кнопок меню
    await bot.set_my_commands(commands=privat, scope=BotCommandScopeAllPrivateChats())

    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

# Вызвали функцию запуска бота
asyncio.run(main())