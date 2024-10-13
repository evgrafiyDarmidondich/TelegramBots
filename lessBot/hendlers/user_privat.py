import dict

from random import choice

from aiogram import Router, types
from aiogram.filters import CommandStart, Command

user_private_router = Router()


# Хендлер реакции на команду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, я, виртуальный помощник")

# хендлер меню
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Это меню")

# эхо хендлер
@user_private_router.message()
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
