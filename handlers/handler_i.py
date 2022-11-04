from aiogram import types
from keyboards import kb_urls_i
import texts
from async_table import table_add
from datetime import datetime


async def call1(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text1, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call1.__name__, datetime.now()))


async def call2(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text2, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call2.__name__, datetime.now()))


async def call3(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text3, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call3.__name__, datetime.now()))


async def call4(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text4, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call4.__name__, datetime.now()))


async def call5(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text5, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call5.__name__, datetime.now()))


async def call6(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text6, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call6.__name__, datetime.now()))


async def call7(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text7, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call7.__name__, datetime.now()))


async def call18(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text18, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call18.__name__, datetime.now()))


async def call19(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text19, reply_markup=kb_urls_i)
    await callback.answer()
    await table_add((callback.from_user, call19.__name__, datetime.now()))
