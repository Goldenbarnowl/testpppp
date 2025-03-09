from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import bot

admin_router = Router()

@admin_router.message()
async def last_stand(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Я тебя не понимаю",
    )
