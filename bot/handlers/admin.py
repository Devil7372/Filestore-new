from aiogram import types
from aiogram.dispatcher import filters
from bot.config import ADMINS
from bot.database import db
from bot.utils.helper import delete_file_by_id, get_stats
from bot.utils.buttons import close_button
from bot.main import dp

# Only allow commands from admins
def is_admin(user_id):
    return user_id in ADMINS


@dp.message_handler(filters.Command("stats"))
async def stats_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("You are not authorized to use this command.")
    
    stats = await get_stats()
    await message.reply(f"📊 Bot Statistics:\n\n{stats}")


@dp.message_handler(filters.Command("delete"))
async def delete_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("You are not authorized to use this command.")

    args = message.get_args()
    if not args:
        return await message.reply("⚠️ Usage:\n`/delete <file_id>`", parse_mode="Markdown")
    
    file_id = args.strip()
    success = await delete_file_by_id(file_id)

    if success:
        await message.reply(f"✅ File with ID `{file_id}` deleted.", parse_mode="Markdown")
    else:
        await message.reply(f"❌ No file found with ID `{file_id}`.", parse_mode="Markdown")
