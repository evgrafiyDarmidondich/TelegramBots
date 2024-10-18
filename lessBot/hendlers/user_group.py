
from string import punctuation

from aiogram import Router, types

from lessBot.dict import restricted_words
from lessBot.filters.chat_types import ChatTypesFilters

user_group_router = Router()
user_group_router.message.filter(ChatTypesFilters(["group", 'supergroup']))


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.delete()