from string import punctuation

from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.types import Message

from lessBot.dicts import restricted_words
from lessBot.filters.chat_types import ChatTypesFilters

user_group_router = Router()
user_group_router.message.filter(ChatTypesFilters(["group", 'supergroup']))

@user_group_router.message(Command("admin"))
async def get_admins(message: Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)

    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    else:
        pass


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.delete()