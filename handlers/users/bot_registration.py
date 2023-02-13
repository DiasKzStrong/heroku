from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, CallbackQuery,ReplyKeyboardRemove
from Keybord.Default import kb_ayel_menu, kb_er_menu
from loader import dp
from state import register
from utils.dp_api import quick_commands as commands
from utils.dp_api.db_namaz import db
from Keybord.Inline.inline_oblys import namaz_olbys
from utils.misc.throttling import rate_limit


@rate_limit(limit=5)
@dp.message_handler(Command('register'))
async def bot_register(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    if user == None:
        await message.answer(f"Ботқа тіркелу үшін есіміңізді жазыңыз")
        await register.name.set()
    else:
        await message.answer("Cіз тіркелгенсіз")

@dp.message_handler(text = 'Қайта тіркелу⏪️')
async def re_register(message:types.Message):
        await commands.del_user(message.from_user.id)
        await message.answer(f"Ботқа тіркелу үшін есіміңізді жазыңыз")
        await register.name.set()

@dp.message_handler(text = 'Қайта тіркелу◀️')
async def re_register(message:types.Message):
    if await commands.sel_user(message.from_user.id):
        await commands.del_user(message.from_user.id)
        await message.answer(f"Ботқа тіркелу үшін есіміңізді жазыңыз",reply_markup=ReplyKeyboardRemove())
        await register.name.set()
    else:
        await message.answer(f"Ботқа тіркелу үшін есіміңізді жазыңыз",reply_markup=ReplyKeyboardRemove())
        await register.name.set()


@dp.message_handler(state=register.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    zhynys = ReplyKeyboardMarkup(keyboard=
    [[
        KeyboardButton(text='Ер адам🧔🏻‍♂️'),
        KeyboardButton(text='Әйел адам🧕🏻')],
        [
            KeyboardButton(text='Тіркеуді тоқтату')
        ]
    ],
    )
    await message.answer(f"Ассаляму 'алейкум уа рахматуллахи уа баракатух: <b>{message.text}</b>")
    await message.answer(f"Енді жынысыңызды тандаңыз🧔🏻‍♂️🧕🏻", reply_markup=zhynys)
    await register.zhynys.set()



@dp.message_handler(state=register.zhynys)
async def zhynys(message: types.Message, state: FSMContext):
    if message.text == 'Тіркеуді тоқтату':
        await message.answer("Тіркеу тоқтатылды")
        await state.finish()
    elif message.text == 'Ер адам🧔🏻‍♂️'  or message.text == 'Әйел адам🧕🏻':
        await state.update_data(zhynys=message.text)
        if message.text == 'Әйел адам🧕🏻':
            await message.answer("Тіркеу аяқталды", reply_markup=kb_ayel_menu)
        elif message.text == 'Ер адам🧔🏻‍♂️':
            await message.answer("Тіркеу аяқталды", reply_markup=kb_er_menu)
        data = await state.get_data()
        name = data.get('name')
        zhynyss = data.get('zhynys')
        await commands.add_user(user_id=message.from_user.id,
                                user_name=name,
                                zhynys=zhynyss)
        await state.finish()
    elif message.text != 'Ер адам🧔🏻‍♂️'  or message.text != 'Әйел адам🧕🏻':
        await message.delete()


