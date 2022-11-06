from aiogram.dispatcher.filters.state import State,StatesGroup


class register(StatesGroup):
    name = State()
    zhynys = State()

class re_register(StatesGroup):
    re_register = State()