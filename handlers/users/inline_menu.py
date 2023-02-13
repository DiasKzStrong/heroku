from loader import dp
from aiogram import types
from Keybord.Inline import inline_tan,inline_besin,inline_ekinti,inline_aksham,inline_kuptan,inline_utir,inline_ulken_wudu,inline_wudu
from utils.misc.throttling import rate_limit


@rate_limit(limit=5)
@dp.message_handler(text = 'Таң намазы🧔🏻‍♂️')
async def tan(message: types.Message):
    await message.answer('Таң намазы🧔🏻‍♂️',reply_markup=inline_tan)

@rate_limit(limit=5)
@dp.message_handler(text = 'Бесін намазы🧔🏻‍♂️')
async def besin(message: types.Message):
    await message.answer('Бесін намазы🧔🏻‍♂️',reply_markup=inline_besin)

@rate_limit(limit=5)
@dp.message_handler(text='Екінті намазы🧔🏻‍♂️')
async def besin(message: types.Message):
    await message.answer('Екінті намазы🧔🏻‍♂️', reply_markup=inline_ekinti)
@rate_limit(limit=5)
@dp.message_handler(text='Ақшам намазы🧔🏻‍♂️')
async def besin(message: types.Message):
    await message.answer('Ақшам намазы🧔🏻‍♂️', reply_markup=inline_aksham)
@rate_limit(limit=5)
@dp.message_handler(text='Құптан намазы🧔🏻‍♂️')
async def besin(message: types.Message):
    await message.answer('Құптан намазы🧔🏻‍♂️', reply_markup=inline_kuptan)
@rate_limit(limit=5)
@dp.message_handler(text='Үтір намазы🧔🏻‍♂️')
async def besin(message: types.Message):
    await message.answer('Үтір намазы🧔🏻‍♂️', reply_markup=inline_utir)



