from aiogram import types
from datetime import datetime
from keyboards import kb_urls_contact, kb_urls, kb_urls_contact_back
from async_table import table_add, table_add_contact
from create_bot import bot
import texts


async def contact_info(callback: types.CallbackQuery):
    bot.active_writer = "information"
    await callback.message.delete()
    prev_mess = await callback.message.answer(
        texts.text26, reply_markup=kb_urls_contact_back
    )
    await callback.answer()
    await table_add((callback.from_user, contact_info.__name__, datetime.now()))
    bot.previous_callback = (callback.message.chat.id, prev_mess.message_id)


async def contact_comm(callback: types.CallbackQuery):
    bot.active_writer = "commerce"
    await callback.message.delete()
    prev_mess = await callback.message.answer(
        texts.text27, reply_markup=kb_urls_contact_back
    )
    await callback.answer()
    await table_add((callback.from_user, contact_comm.__name__, datetime.now()))
    bot.previous_callback = (callback.message.chat.id, prev_mess.message_id)


async def contact_back(callback: types.CallbackQuery):
    bot.active_writer = None
    await callback.message.delete()
    await callback.message.answer(texts.text25, reply_markup=kb_urls_contact)
    await callback.answer()
    await table_add((callback.from_user, contact_back.__name__, datetime.now()))


async def contact_text_message(message: types.Message):
    if bot.active_writer is not None:
        await bot.delete_message(*bot.previous_callback)
        await bot.send_message(message.from_user.id, texts.text28, reply_markup=kb_urls)
        await table_add(
            (message.from_user, contact_text_message.__name__, datetime.now())
        )
        await table_add_contact(
            (message.from_user, message.date, bot.active_writer, message.text)
        )
        bot.active_writer = None
