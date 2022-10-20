from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from emoji import emojize
from Keybord.Default import kb_menu, kb_menu_namaz,zhynys_menu


@dp.message_handler(text="Артқа қайту")
async def back(message: types.Message):
    await message.answer("Артқа қайту", reply_markup=zhynys_menu)


@dp.message_handler(text="Менюға артқа қайту")
async def back(message: types.Message):
    await message.answer("Артқа қайту", reply_markup=kb_menu)


@dp.message_handler(Command("menu"))
async def main_menu(message: types.Message):
    await message.answer(text='Жынысыныз?', reply_markup=zhynys_menu)

@dp.message_handler(text = "Ер адам")
async def er_adam(message: types.Message):
    await message.answer(text='Ер адам', reply_markup=kb_menu)

@dp.message_handler(text=f'Намаз окып уйрену 🧔🏻‍♂️')
async def menu_namaz(message: types.Message):
    await message.answer('Намаз', reply_markup=kb_menu_namaz)


# @dp.message_handler(text="Намаз уакыты")
# async def namaz_time(message: types.Message):
#     await message.answer("Қай қаладансыз?")
#     await States.namaz_time.set()
#
#
# @dp.message_handler(state=States.namaz_time)
# async def namaz_output(message: types.Message, state: FSMContext):
#     answer = message.text
#     if find_city(answer) != True:
#         await message.answer("Жок")
#         find_city(answer)
#     elif find_city(answer) == True:
#         await state.update_data(namaz_time=answer)
#         city = await state.get_data()
#         array = get_namaz_time(city.get('namaz_time'))
#         await message.answer(f"Аср намазы:{array['asr']}")
#         await state.finish()
