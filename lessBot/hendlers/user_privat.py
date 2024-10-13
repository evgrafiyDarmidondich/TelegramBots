import dict

import types
from random import choice

from aiogram.filters import CommandStart

from lessBot.app import dp


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
        else:
            await message.answer('Я пока не понимаю того чего ты написал')
    except:
        await message.answer(f'Хорошая попытка {message.text}')
