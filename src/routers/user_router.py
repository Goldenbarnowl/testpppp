from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from config import bot
from src.keyboards.user_keyboard import get_reply_keyboard, button, get_inline_keyboard

user_router = Router()


@user_router.message(CommandStart())
@user_router.message(Command("privet"))
async def start_command(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Привет",
        reply_markup=get_reply_keyboard()
    )


@user_router.message(F.text == button["settings"])
async def poka(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Пока",
        reply_markup=get_inline_keyboard()
    )


@user_router.message()
async def last_stand(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Я тебя не понимаю",
    )


@user_router.callback_query(F.data == "confirm")
async def confirm(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Подтверждено",
    )

