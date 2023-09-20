from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data import keyboards_data as kd

__all__ = [
    "get_user_menu",
    "back",
    "course",
    "reg_ref",
    "instruction",
    "fio",
    "trade",
    "take",
    "take_fio",
    "take_num",
    "scren",
    "final",
]


async def get_user_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🎓 О проекте",callback_data="act_1"),
        InlineKeyboardButton("😉 Приведи друга",callback_data="act_2"),
        InlineKeyboardButton("✔ Зарегистрироваться на курс",callback_data="act_3")
    )
    return keyboard
async def scren():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="🔙 Назад",callback_data="back"),
        InlineKeyboardButton(text="📷 Загрузить скриншот",callback_data="act_14"),
        InlineKeyboardButton("✔ Зарегистрироваться на курс",callback_data="act_3")
    )
    return keyboard

async def back():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text="🔙 Назад",callback_data="back"),
    InlineKeyboardButton("✔ Зарегистрироваться на курс",callback_data="act_3")
    )
    return keyboard

async def final():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="🔙 Назад",callback_data="back"),
        InlineKeyboardButton(text="✔ Зарегистрироваться на Госуслуги",url="https://www.gosuslugi.ru/futurecode?view=online&organization=44&sortKey=cfRating"),
        InlineKeyboardButton(text="📷 Загрузить скриншот",callback_data="act_14"),
    )
    return keyboard
async def course():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🤖 Telegram-боты на Python",callback_data="act_4"),
        InlineKeyboardButton("🎮 Разработка 2d-игр на Python",callback_data="act_5"),
        InlineKeyboardButton("🦾 П риручи искусственный интеллект",callback_data="act_51"),
        InlineKeyboardButton("📑 Разработка парсеров на Python",callback_data="act_52"),
        InlineKeyboardButton("🎨 Разработка графических интерфейсов",callback_data="act_53"),
        InlineKeyboardButton("🧑<200d>💻 Этичный хакинг на Python",callback_data="act_54"),
        InlineKeyboardButton(text="🔙 Назад ",callback_data="back"),
    )
    return keyboard

async def reg_ref():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🔗 Реферальное приглашение",callback_data="act_6"),
        InlineKeyboardButton("🎁 Обменять баллы",callback_data="act_9"),
        InlineKeyboardButton("📋 Условия обмена баллов",callback_data="act_91"),
        InlineKeyboardButton("📝 Список приглашенных",callback_data="act_10"),
        InlineKeyboardButton("✔ Зарегистрироваться на курс",callback_data="act_3"),
    )
    return keyboard

async def take_fio():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("✅  Я написал свое ФИО",callback_data="act_12"),
    )
    return keyboard

async def take_num():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("✅  Я написал свой номер заявления",callback_data="act_13"),
    )
    return keyboard

async def instruction():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("✅  Я написал свою почту",callback_data="act_8"),
    )
async def trade():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("🪙 Получить сертификат",callback_data="act_11"),
    )
    return keyboard
async def take():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("✅  Я написал все данные!",callback_data="back"),
    )
    return keyboard
async def fio():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="🔙 Назад ",callback_data="act_3"),
        InlineKeyboardButton("🫡 Выбираю этот курс",callback_data="act_7"),
    )
    return keyboard
