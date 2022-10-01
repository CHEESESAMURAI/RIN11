from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data import keyboards_data as kd

__all__ = [
    "get_user_menu",
    "back",
]


async def get_user_menu():
    keyboard = InlineKeyboardMarkup()

    return keyboard


async def back():
    keyboard = InlineKeyboardMarkup()

    return keyboard
