from aiogram import types
from loader import dp
from utils.dp_api import quick_commands as commands
from Keybord.Default import kb_ayel_menu,kb_er_menu
from utils.misc.throttling import rate_limit


@rate_limit(limit=5)
@dp.message_handler(text = '/start')
async def command_start(message: types.Message):
    user = await commands.sel_user(message.from_user.id)
    user_name = await commands.select_user(message.from_user.id)
    zhynys = await commands.select_user_zhynys(message.from_user.id)
    if user == None:
        await message.answer(f"Ассаляму 'алейкум уа рахматуллахи уа баракатух\n\n"
                            f"Ботты қолдануды бастау үшін алдымен тіркелуден өтіңіз,тіркелу үшін:"
                            f"\n\n/register командасын басыңыз немесе төменгі сол жаққатағы меню арқылы таңдау аласыз")
    else:
        if zhynys == 'Ер адам🧔🏻‍♂️':
            await message.answer(f"Ассаляму 'алейкум уа рахматуллахи уа баракатух <b>{user_name}</b>\n\n"
                                 f"Қайта келгеніңізге қуаныштымын",reply_markup=kb_er_menu)
        elif zhynys == 'Әйел адам🧕🏻':
            await message.answer(f"Ассаляму 'алейкум уа рахматуллахи уа баракатух <b>{user_name}</b>\n\n"
                                 f"Қайта келгеніңізге қуаныштымын", reply_markup=kb_ayel_menu)

