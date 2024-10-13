import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types

load_dotenv()
TOKEN = os.getenv('TOKEN')

# список разрешоных обновлений
ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(TOKEN)

dp = Dispatcher()



# функция запуска бота
async def main():
    # Сбрасывает ожидаеме обновления
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

# Вызвали функцию запуска бота
asyncio.run(main())