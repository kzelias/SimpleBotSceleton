from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(token="{YOUR_BOT_TOKEN}")
bot.db_con = None
bot.active_writer = None
bot.previous_callback = None
bot.message_count = 0
bot.chat_ids = []
dp = Dispatcher(bot)
