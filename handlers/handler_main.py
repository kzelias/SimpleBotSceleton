from aiogram import types
from create_bot import bot
from keyboards import (
    kb_urls,
    kb_urls_i,
    kb_urls_j,
    kb_urls_c,
    kb_urls_contact,
    kb_urls_ch,
)
import texts
from datetime import datetime
from async_table import table_add, table_add_follower


async def command_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id, texts.start_menu, reply_markup=kb_urls
        )
        await table_add_follower(
            (message.from_user, command_start.__name__, datetime.now())
        )
    except BaseException as ex:
        print(f"Ex:{ex}")
        await message.reply("Send PM")


async def call14(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text14, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call14.__name__, datetime.now()))


async def call30(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text30, reply_markup=kb_urls_ch)
    await callback.answer()
    await table_add((callback.from_user, call30.__name__, datetime.now()))


async def call31(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text31, reply_markup=kb_urls_j)
    await callback.answer()
    await table_add((callback.from_user, call31.__name__, datetime.now()))


async def call16(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text16, reply_markup=kb_urls)
    await callback.answer()
    await table_add((callback.from_user, call16.__name__, datetime.now()))


async def call20(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text20, reply_markup=kb_urls_c)
    await callback.answer()
    await table_add((callback.from_user, call20.__name__, datetime.now()))


async def contact(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text25, reply_markup=kb_urls_contact)
    await callback.answer()
    await table_add((callback.from_user, contact.__name__, datetime.now()))


async def back(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.back, reply_markup=kb_urls)
    await callback.answer()
    await table_add((callback.from_user, back.__name__, datetime.now()))
