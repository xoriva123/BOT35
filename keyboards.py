from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def tariffs_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1 месяц — 150₽", callback_data="buy_1m")],
        [InlineKeyboardButton(text="3 месяца — 350₽", callback_data="buy_3m")]
    ])
