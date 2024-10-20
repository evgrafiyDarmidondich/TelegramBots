from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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