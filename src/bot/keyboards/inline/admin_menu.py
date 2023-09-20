    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__all__ = [
    "get_admin_menu"
]


async def get_admin_menu(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text='Скрин да',callback_data=f"code_{user_id}"),
        InlineKeyboardButton(text='Скрин нет',callback_data=f"denied_{user_id}"),
        InlineKeyboardButton(text='Промо да',callback_data=f"code2_{user_id}"),
        InlineKeyboardButton(text='Промо нет',callback_data=f"denied2_{user_id}"),
        InlineKeyboardButton(text='+50',callback_data=f"plus_{user_id}")
    )
    return keyboard
