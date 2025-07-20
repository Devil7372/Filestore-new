from aiogram import types
from aiogram.dispatcher import filters
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
from bot.config import ADMINS
from bot.database import db
from bot.main import dp

# Utility function to check if the user is admin
def is_admin(user_id):
    return user_id in ADMINS


@dp.message_handler(filters.Command("broadcast"))
async def broadcast_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("You are not authorized to use this command.")

    if not message.reply_to_message:
        return await message.reply("Reply to a message to broadcast it to all users.")

    sent = 0
    failed = 0
    users = await db.get_all_users()

    for user in users:
        try:
            await message.reply_to_message.copy_to(user["user_id"])
            sent += 1
        except (BotBlocked, ChatNotFound):
            failed += 1
            continue
        except Exception:
            failed += 1
            continue

    await message.reply(f"📢 Broadcast finished.\n✅ Sent: {sent}\n❌ Failed: {failed}")
