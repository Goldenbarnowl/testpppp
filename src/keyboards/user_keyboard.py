from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton

button = {
    "settings": "⚙️ Настройки",
    "Отправить геолокацию": "📍 Отправить геолокацию",
    "Отправить контакт": "📞 Отправить контакт",
    "Информация": "ℹ️ Информация",
    "shop": "🛍 Магазин"}


def get_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=button["settings"]))
    builder.row(
        KeyboardButton(text="📍 Отправить геолокацию", request_location=True),
        KeyboardButton(text="📞 Отправить контакт", request_contact=True)
    )
    builder.row(
        KeyboardButton(text="ℹ️ Информация"),
        KeyboardButton(text=button["shop"])
    )
    return builder.as_markup(resize_keyboard=True)


def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm"),
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
    )
    builder.row(
        InlineKeyboardButton(text="🔗 Открыть сайт", url="https://example.com")
    )
    return builder.as_markup()
