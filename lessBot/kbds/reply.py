
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
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

# Тестовая клавиатура с кнопками запроса
test_cb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Отправить номер ☎️", request_contact=True),
            KeyboardButton(text="Отправить локацию 🧭", request_location=True)
        ],
    ],
    resize_keyboard=True
)

def get_keyboard(
        *btns: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        sizes: tuple[int] = (2, 2)
):
    keyboard = ReplyKeyboardBuilder()
    for index, text in enumerate(btns, start=0):
        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))

        else:
            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placeholder=placeholder
    )
