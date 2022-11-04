from aiogram import types
from keyboards import kb_urls_j_d, kb_urls_j_i, kb_urls_j_back
import texts
from async_table import table_add
from datetime import datetime


async def call8(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text8, reply_markup=kb_urls_j_i)
    await callback.answer()
    await table_add((callback.from_user, call8.__name__, datetime.now()))


async def call13(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text13, reply_markup=kb_urls_j_back)
    await callback.answer()
    await table_add((callback.from_user, call13.__name__, datetime.now()))


async def call9(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text9, reply_markup=kb_urls_j_d)
    await callback.answer()
    await table_add((callback.from_user, call9.__name__, datetime.now()))


async def call10(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text10, reply_markup=kb_urls_j_d)
    await callback.answer()
    await table_add((callback.from_user, call10.__name__, datetime.now()))


async def call11(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text11, reply_markup=kb_urls_j_d)
    await callback.answer()
    await table_add((callback.from_user, call11.__name__, datetime.now()))


async def call12(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text12, reply_markup=kb_urls_j_d)
    await callback.answer()
    await table_add((callback.from_user, call12.__name__, datetime.now()))
