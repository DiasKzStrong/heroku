async def on_startup(dp):


    from utils.notify_admin import on_startup_notify
    await on_startup_notify(dp)

    from utils.dp_api import db_namaz
    await db_namaz.on_startup(dp)

    from utils.set_bot_commands import  set_default_commands
    await set_default_commands(dp)
    print("Бот запущен")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp,on_startup=on_startup)