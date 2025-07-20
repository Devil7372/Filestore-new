from aiogram import types, Dispatcher
from bot.utils.buttons import start_buttons

async def start_handler(message: types.Message):
    await message.answer("👋 Welcome to the bot!", reply_markup=start_buttons())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
