from bot.database import db

async def delete_file_by_id(file_id):
    """
    Deletes a file by its reference ID from the database.
    """
    result = await db.delete_file(file_id)
    return result

async def get_stats():
    """
    Returns basic bot statistics.
    """
    user_count = await db.count_users()
    file_count = await db.count_files()
    return f"👥 Users: {user_count}\n📁 Files: {file_count}"
