from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from Script import get_namaz_time,print_namaz_time
from Keybord.Inline.inline_oblys import namaz_olbys
from Keybord.Inline.inline_oblys_ciau import inline_akmola_obl,inline_zhetisy_obl,inline_almaty_obl,inline_ulytau_obl,inline_turkistan_obl,inline_krg_obl,inline_atyrau_obl,inline_aktay_obl,inline_oral_obl,inline_shygys_obl,inline_kostanay_obl,inline_kyzylorda_obl,inline_soltystuk_obl,inline_aktobe_obl,inline_pavlodar_obl,inline_zhambyl_obl,inline_abai_obl


@dp.callback_query_handler(text="Артқа қайту")
async def get_back(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=namaz_olbys)


@dp.message_handler(text='Намаз уакыты')
async def namaz_time(message: types.Message):
    await message.answer("Қай қаладансыз?", reply_markup=namaz_olbys)


@dp.callback_query_handler(text="Астана")
async def Astana(call: CallbackQuery):
    await print_namaz_time(call.data, call)
    await call.message.delete()

@dp.callback_query_handler(text="Алматы")
async def Astana(call: CallbackQuery):
    await print_namaz_time(call.data, call)
    await call.message.delete()

@dp.callback_query_handler(text="Шымкент")
async def Astana(call: CallbackQuery):
    await print_namaz_time(call.data, call)
    await call.message.delete()


@dp.callback_query_handler(text="Ақмола облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_akmola_obl)

    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Жетісу облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_zhetisy_obl)

    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Алматы облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_almaty_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Қарағанды облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_krg_obl)

    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Ұлытау облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_ulytau_obl)

    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Түркістан облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_turkistan_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()

@dp.callback_query_handler(text="Жамбыл облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_zhambyl_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()

@dp.callback_query_handler(text="Қызылорда облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_kyzylorda_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()

@dp.callback_query_handler(text="Абай облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_abai_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()

@dp.callback_query_handler(text="Шығыс қазақстан облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_shygys_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Қостанай облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_kostanay_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Петропавл облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_soltystuk_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Павлодар облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_pavlodar_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Ақтөбе облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_aktobe_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()

@dp.callback_query_handler(text="Ақтау облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_aktay_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Атырау облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_atyrau_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()


@dp.callback_query_handler(text="Орал облысы")
async def Akmola(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=inline_oral_obl)
    @dp.callback_query_handler()
    async def akmola_list(call: CallbackQuery):
        await print_namaz_time(call.data, call)
        await call.message.delete()
