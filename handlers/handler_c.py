from aiogram import types
from keyboards import kb_urls_c
import texts
from async_table import table_add
from datetime import datetime


async def call21(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text21, reply_markup=kb_urls_c)
    await callback.answer()
    await table_add((callback.from_user, call21.__name__, datetime.now()))


async def call22(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text22, reply_markup=kb_urls_c)
    await callback.answer()
    await table_add((callback.from_user, call22.__name__, datetime.now()))


async def call23(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text23, reply_markup=kb_urls_c)
    await callback.answer()
    await table_add((callback.from_user, call23.__name__, datetime.now()))


async def call15(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(texts.text15, reply_markup=kb_urls_c)
    await callback.answer()
    await table_add((callback.from_user, call15.__name__, datetime.now()))
