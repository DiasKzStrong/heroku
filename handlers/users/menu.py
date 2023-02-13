from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from Keybord.Default import kb_er_menu, kb_er_menu_namaz,zhynys_menu,kb_ayel_menu_namaz,kb_ayel_menu
from Keybord.Inline.inline_er_keyboard import inline_Quran
from utils.dp_api import quick_commands as commands
from utils.misc.throttling import rate_limit


@dp.message_handler(text='Менюға артқа қайту◀')
async def back(message:types.Message):
    zhynys = await commands.select_user_zhynys(message.from_user.id)
    if zhynys == "Ер адам🧔🏻‍♂️":
        await message.answer('Менюға артқа қайту◀',reply_markup=kb_er_menu)
    elif zhynys == "Әйел адам🧕🏻":
        await message.answer('Менюға артқа қайту◀',reply_markup=kb_ayel_menu)

@dp.message_handler(text="Менюға артқа қайту◀️")
async def back(message: types.Message):
    await message.answer("Артқа қайту", reply_markup=kb_er_menu)


@dp.message_handler(text="Менюға артқа қайту⏪️")
async def back(message: types.Message):
    await message.answer("Артқа қайту", reply_markup=kb_ayel_menu)

@rate_limit(limit=5)
@dp.message_handler(Command("menu"))
async def main_menu(message: types.Message):
    zhynys = await commands.select_user_zhynys(message.from_user.id)
    if zhynys == "Ер адам🧔🏻‍♂️":
        await message.answer('Меню Ер адам🧔🏻‍♂️ ', reply_markup=kb_er_menu)
    elif zhynys == "Әйел адам🧕🏻":
        await message.answer('Меню Әйел адам🧕🏻', reply_markup=kb_ayel_menu)
    else:
        await message.answer("Ботпен қолданбас бұрын алдымен тіркелуден өтіңіз,алдымен тіркелуден өтіңіз")

@rate_limit(limit=5)
@dp.message_handler(text = "Ер адам🧔🏻‍♂️")
async def er_adam(message: types.Message):
    await message.answer(text='Ер адам🧔🏻‍♂️', reply_markup=kb_er_menu)

@rate_limit(limit=5)
@dp.message_handler(text = 'Әйел адам🧕🏻')
async def ayel(message: types.Message):
    await message.answer(text = 'Әйел адам🧕🏻',reply_markup=kb_ayel_menu)

@rate_limit(limit=5)
@dp.message_handler(text=f'Намаз окып уйрену🧔🏻‍♂️')
async def menu_namaz(message: types.Message):
    await message.answer('Намаз🧔🏻‍♂️', reply_markup=kb_er_menu_namaz)

@rate_limit(limit=5)
@dp.message_handler(text=f'Намаз окып уйрену🧕🏻')
async def menu_namaz(message: types.Message):
    await message.answer('Намаз🧕🏻', reply_markup=kb_ayel_menu_namaz)

@rate_limit(limit=5)
@dp.message_handler(text = "Құран☪️")
async def Quran(message:types.Message):
    await message.answer("Құран☪️",reply_markup=inline_Quran)