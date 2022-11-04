from aiogram.utils import executor
from create_bot import dp, bot
from handlers import register
import aiosqlite


async def on_startup(_):
    if bot.db_con is None:
        bot.db_con = await aiosqlite.connect("table.db", check_same_thread=False)
        cur = await bot.db_con.cursor()
        await cur.execute(
            """CREATE TABLE IF NOT EXISTS clicks
            (click_id INTEGER PRIMARY KEY, user_id INTEGER, username VARCHAR(32), button_name VARCHAR(20), time TIMESTAMP, 
            first_name VARCHAR(64), last_name VARCHAR(64), is_bot INTEGER, language_code VARCHAR(20), 
            is_premium INTEGER, added_to_attachment_menu INTEGER, can_join_groups INTEGER,
            can_read_all_group_messages INTEGER, supports_inline_queries INTEGER)"""
        )

        await cur.execute(
            """CREATE TABLE IF NOT EXISTS followers
            (click_id INTEGER PRIMARY KEY, user_id INTEGER, username VARCHAR(32), button_name VARCHAR(20), time TIMESTAMP, 
            first_name VARCHAR(64), last_name VARCHAR(64), is_bot INTEGER, language_code VARCHAR(20), 
            is_premium INTEGER, added_to_attachment_menu INTEGER, can_join_groups INTEGER,
            can_read_all_group_messages INTEGER, supports_inline_queries INTEGER, status VARCHAR(10))"""
        )

        await cur.execute(
            """CREATE TABLE IF NOT EXISTS contacts
        (contact_id INTEGER PRIMARY KEY, user_id INTEGER, username VARCHAR(32),
        first_name VARCHAR(64), last_name VARCHAR(64), time TIMESTAMP, question VARCHAR(12), text_message TEXT)"""
        )

        await bot.db_con.commit()
    print("Bot online")


register.register_handlers_client(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
