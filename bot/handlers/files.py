from aiogram import types
from aiogram.dispatcher import filters
from bot.config import ADMINS
from bot.database import db
from bot.utils.buttons import get_file_button
from bot.main import dp, bot
from datetime import datetime, timedelta
import asyncio

# Check if user is admin
def is_admin(user_id):
    return user_id in ADMINS

# Handle media files (documents, videos, etc.)
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT | types.ContentTypes.VIDEO | types.ContentTypes.PHOTO)
async def handle_files(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("🚫 Only admins can upload files.")

    file_type = message.content_type
    telegram_file = getattr(message, file_type)
    file_id = telegram_file.file_id
    file_unique_id = telegram_file.file_unique_id
    file_name = telegram_file.file_name if file_type == "document" else f"{file_type}_{file_unique_id}"

    # Save file info to DB
    file_data = {
        "file_id": file_id,
        "file_unique_id": file_unique_id,
        "file_type": file_type,
        "file_name": file_name,
        "uploaded_by": message.from_user.id,
        "uploaded_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(days=7)
    }
    file_ref_id = await db.save_file(file_data)

    # Reply with link
    link_button = get_file_button(file_ref_id)
    await message.reply(
        f"✅ File saved!\n🆔 File ID: `{file_ref_id}`\n📁 Name: `{file_name}`\n⏳ Expires in 7 days.",
        reply_markup=link_button,
        parse_mode="Markdown"
    )

    # Warn user & delete after 10 minutes
    await asyncio.sleep(600)
    try:
        await message.delete()
        await message.answer(f"⚠️ File message auto-deleted after 10 minutes.")
    except:
        pass
