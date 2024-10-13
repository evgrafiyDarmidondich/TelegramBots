import asyncio
import os
import dict

from random import choice
from aiogram import Bot, Dispatcher, types
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
        text: str | None = message.text
        text = text.lower()
        if text in dict.greeting:
            # отвечаем на приветствие из списка, приветствием из того же списка
            await message.answer(choice(dict.greeting))
        elif text in dict.parting:
            await message.answer(choice(dict.parting))
    except:
        await message.answer(f'Хорошая попытка {message.text}')



# функция запуска бота
async def main():
    # Сбрасывает ожидаеме обновления
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

# Вызвали функцию запуска бота
asyncio.run(main())