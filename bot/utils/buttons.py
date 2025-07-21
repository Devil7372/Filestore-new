from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import USE_SHORTENER

def get_file_button(file_id: str):
    """
    Generate a file access button with optional shortener.
    """
    if USE_SHORTENER:
        link = f"https://t.me/OG_FILESTORE_ROBOT?start=short_{file_id}"  # Replace with your bot username
    else:
        link = f"https://t.me/OG_FILESTORE_ROBOT?start=file_{file_id}"  # Replace with your bot username

    buttons = InlineKeyboardMarkup(row_width=1)
    buttons.add(InlineKeyboardButton("📥 Download File", url=link))
    return buttons


def close_button():
    """
    Returns a close/cancel inline button.
    """
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("❌ Close", callback_data="close"))
    return markup
