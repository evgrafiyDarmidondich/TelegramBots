from string import punctuation

from aiogram import Router, types, F
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message

from lessBot.filters.chat_types import ChatTypesFilters
from lessBot.kbds import reply
from lessBot.kbds.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilters(['private']))

# Хендлер реакции на команду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, я, виртуальный помощник",
                         reply_markup=get_keyboard(
                             "Меню",
                             "О магазине",
                             "Варианты оплаты",
                             "Варианты доставки",
                             placeholder="Что вас интересует?",
                             sizes=(2, 2)
                         ))

# хендлер меню
@user_private_router.message(or_f(Command('menu'),F.text.lower().contains('меню')))
async def menu_cmd(message: types.Message):
    await message.answer("Это меню", reply_markup=reply.del_kbd)

# хендлер  абоут
@user_private_router.message(or_f(Command('about'), F.text.lower().contains('о магазине')))
async def about_cmd(message: types.Message):
    await message.answer("Это про нас", reply_markup=reply.del_kbd)

# хендлер  оплаты
@user_private_router.message(F.text.lower().contains('как заплатить') |
                             F.text.lower().contains('оплат'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):

    text = as_marked_section(
        Bold("Варианты оплаты:\n"),
        "Картой в боте\n",
        "При получение карта/кэш\n",
        "В заведении",
        marker="✅ "
    )

    await message.answer(text.as_html(), reply_markup=reply.del_kbd)

# хендлер  доставки
@user_private_router.message(F.text.lower().contains('варианты доставки') |
                             F.text.lower().contains('доста'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):

    text = as_list(as_marked_section(
        Bold("Варианты доставки:\n"),
        "Курьер\n",
        "Самовывоз(Сейчас приду заберу)\n",
        "Покушаю у вас (Сейчас прибегу)",
        marker="✅ "
    ),
    as_marked_section(
        Bold("Нельзя:\n"),
        "📯 Почта\n",
        "🕊 Голуби",
        marker="❌ "
    ),
    sep = "\n-----------------\n")

    await message.answer(text.as_html(), reply_markup=reply.del_kbd)

# хендлер обработки кнопки "Оставить отзыв"
@user_private_router.message(F.text.lower().contains('Оставить отзыв') |
                             F.text.lower().contains('отзы'))
async def get_fedback(message: Message):
    await message.answer("Отправте контакты и локацию", reply_markup=reply.test_cb)


# Хендлер обработки фото с магическим фильтром
@user_private_router.message(F.photo)
async def foto_handler(message: types.Message):
    await message.answer('Это фото')

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

# Хендлеры обработки кнопок запросов Контакта и локации
@user_private_router.message(F.contact)
async def get_contact(message: Message):
    await message.answer(f"Контакт получен \n{message.contact.first_name}\n"
                         f"☎️ {message.contact.phone_number}")

@user_private_router.message(F.location)
async def get_location(message: Message):
    await message.answer(f"Местоположение получено \nдолгота:{message.location.longitude}\nширота:"
                         f"{message.location.latitude}")

