from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_TOKEN
from bot.handlers import start, admin, files, broadcast, forcesub

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Register handlers
start.register_handlers(dp)
admin.register_handlers(dp)
files.register_handlers(dp)
broadcast.register_handlers(dp)
forcesub.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp)
