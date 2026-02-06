from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===== Главное меню с 3 кнопками =====
def main_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Тарифы", callback_data="menu_tariffs")],
        [InlineKeyboardButton(
            text="🧑‍💼 Поддержка",
            url="https://t.me/USERNAME_MANAGERA"  # 👈 Замените на своего менеджера
        )],
        [InlineKeyboardButton(text="ℹ️ Доп. информация", callback_data="menu_info")]
    ])


# ===== Клавиатура тарифов =====
def tariffs_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1 месяц — 150₽", callback_data="buy_1m")],
        [InlineKeyboardButton(text="3 месяца — 350₽", callback_data="buy_3m")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu")]
    ])


# ===== Клавиатура кнопки "Назад" для доп. информации =====
def back_to_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")]
    ])
