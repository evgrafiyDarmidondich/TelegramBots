from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_cb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Меню"),
        KeyboardButton(text="О магазине"),
        KeyboardButton(text="Варианты доставки"),
        KeyboardButton(text="Варианты оплаты"),
        ]
    ],
    resize_keyboard=True
)