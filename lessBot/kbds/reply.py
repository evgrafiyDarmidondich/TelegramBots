from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_cb = ReplyKeyboardMarkup(
    keyboard=[
        # Первый ряд кнопок
        [
        KeyboardButton(text="Меню"),
        KeyboardButton(text="О магазине"),
        ],
        # Второй ряд кнопок
        [
        KeyboardButton(text="Варианты доставки"),
        KeyboardButton(text="Варианты оплаты"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)
# Переменная удаления клавиатуры
del_kbd = ReplyKeyboardRemove()

# Второй способ создания клавиатуры
start_cb2 = ReplyKeyboardBuilder()
start_cb2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О магазине"),
    KeyboardButton(text="Варианты доставки"),
    KeyboardButton(text="Варианты оплаты"),
)
start_cb2.adjust(2, 2)

# Добавление кнопки к клавиатуре методом row
start_cb3 = ReplyKeyboardBuilder()
start_cb3.attach(start_cb2)
start_cb3.row(KeyboardButton(text="Оставить отзыв"))