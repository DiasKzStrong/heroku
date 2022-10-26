from loader import dp
from aiogram import types
from Keybord.Inline import inline_ayel_ulken_wudu,inline_ayel_besin,inline_ayel_aksham,inline_ayel_utir,inline_ayel_kuptan,inline_ayel_ekinti,inline_ayel_wudu,inline_ayel_tan
@dp.message_handler(text = 'Таң намазы🧕🏻')
async def tan(message: types.Message):
    await message.answer('Таң намазы',reply_markup=inline_ayel_tan)

@dp.message_handler(text = 'Бесін намазы🧕🏻')
async def besin(message: types.Message):
    await message.answer('Бесін намазы',reply_markup=inline_ayel_besin)


@dp.message_handler(text='Екінті намазы🧕🏻')
async def besin(message: types.Message):
    await message.answer('Екінті намазы', reply_markup=inline_ayel_ekinti)

@dp.message_handler(text='Ақшам намазы🧕🏻')
async def besin(message: types.Message):
    await message.answer('Ақшам намазы', reply_markup=inline_ayel_aksham)

@dp.message_handler(text='Құптан намазы🧕🏻')
async def besin(message: types.Message):
    await message.answer('Құптан намазы', reply_markup=inline_ayel_kuptan)

@dp.message_handler(text='Үтір намазы🧕🏻')
async def besin(message: types.Message):
    await message.answer('Үтір намазы', reply_markup=inline_ayel_utir)

@dp.message_handler(text='Дарет алып уйрену🧕🏻')
async def wudu(message: types.Message):
    await message.answer('Дарет алып уйрену', reply_markup=inline_ayel_wudu)

@dp.message_handler(text='Ғұсыл алып үйрену🧕🏻')
async def ulken_wudu(message: types.Message):
    await message.answer('Ғұсыл алып үйрену', reply_markup=inline_ayel_ulken_wudu)



