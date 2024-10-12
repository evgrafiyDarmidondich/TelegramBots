import asyncio
import os

from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import CommandStart

from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher()

# Хендлер реакции на команду /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}")

# эхо хендлер
@dp.message()
async def echo_handler(message: types.Message):
    try:
        # Перехватываем текст из сообщения
        await message.answer(message.text)
    except:
        await message.answer(f'Хорошая попытка {message}')



# функция запуска бота
async def main():
    await dp.start_polling(bot)

# Вызвали функцию запуска бота
asyncio.run(main())