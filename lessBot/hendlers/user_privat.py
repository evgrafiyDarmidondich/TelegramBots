from string import punctuation

import dict

from random import choice

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f

from lessBot.common.bot_cmds_list import privat
from lessBot.dict import restricted_words
from lessBot.filters.chat_types import ChatTypesFilters
from lessBot.kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilters(['private']))

# Хендлер реакции на команду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, я, виртуальный помощник",
                         reply_markup=reply.start_cb)

# хендлер меню
@user_private_router.message(or_f(Command('menu'),F.text.lower().contains('меню')))
async def menu_cmd(message: types.Message):
    await message.answer("Это меню", reply_markup=reply.del_kbd)

# хендлер  абоут
@user_private_router.message(or_f(Command('about'), F.text.lower().contains('о магазине')))
async def menu_cmd(message: types.Message):
    await message.answer("Это про нас", reply_markup=reply.del_kbd)

# хендлер  оплаты
@user_private_router.message(F.text.lower().contains('как заплатить') |
                             F.text.lower().contains('оплат'))
@user_private_router.message(Command('payment'))
async def menu_cmd(message: types.Message):
    await message.answer("Это про оплату", reply_markup=reply.del_kbd)

# хендлер  доставки
@user_private_router.message(F.text.lower().contains('варианты доставки') |
                             F.text.lower().contains('доста'))
@user_private_router.message(Command('shipping'))
async def menu_cmd(message: types.Message):
    await message.answer("Это про доставку", reply_markup=reply.del_kbd)


# Хендлер обработки фото с магическим фильтром
@user_private_router.message(F.photo)
async def foto_handler(message: types.Message):
    await message.answer('Это фото')

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

# хендлер приветствия
@user_private_router.message(F.text)
async def greeting_handler(message: types.Message):
    try:
        # Перехватываем текст из сообщения
        text: str | None = message.text
        text = text.lower()
        if text in dict.greeting:
            # отвечаем на приветствие из списка, приветствием из того же списка
            await message.answer(choice(dict.greeting))
        elif text in dict.parting:
            await message.answer(choice(dict.parting))
        # цензура
        elif restricted_words.intersection(message.text.lower().split()):
            await message.delete()
        else:
            await message.answer('Я пока не понимаю того чего ты написал')
    except:
        await message.answer(f'Хорошая попытка {message.text}')
