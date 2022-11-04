from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(token="5676704740:AAGd7Qg0gXqQli5WZo5RK_GJahSdcH2JK6o")
bot.db_con = None
bot.active_writer = None
bot.previous_callback = None
bot.message_count = 0
bot.chat_ids = []
dp = Dispatcher(bot)
