from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from bot.config import CHANNELS, ADMINS
from bot.main import bot

class ForceSubscribe(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id
        elif update.callback_query:
            user_id = update.callback_query.from_user.id
        else:
            return

        # Skip for admins
        if user_id in ADMINS:
            return

        # Check membership in all required channels
        for channel_id in CHANNELS:
            try:
                member = await bot.get_chat_member(channel_id, user_id)
                if member.status in ["left", "kicked"]:
                    raise Exception("Not subscribed")
            except:
                buttons = types.InlineKeyboardMarkup()
                for ch_id in CHANNELS:
                    chat = await bot.get_chat(ch_id)
                    invite_link = chat.username and f"https://t.me/{chat.username}" or chat.invite_link
                    buttons.add(types.InlineKeyboardButton(text=f"Join {chat.title}", url=invite_link))
                buttons.add(types.InlineKeyboardButton("✅ I've Joined", callback_data="check_sub"))
                if update.message:
                    await update.message.answer("📢 Please join all required channels to use the bot:", reply_markup=buttons)
                elif update.callback_query:
                    await update.callback_query.message.edit_text("📢 Please join all required channels to use the bot:", reply_markup=buttons)
                raise CancelHandler()
