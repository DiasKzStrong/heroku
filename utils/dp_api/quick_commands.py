from asyncpg import UniqueViolationError

from utils.dp_api.db_namaz import db
from utils.dp_api.schemas.user import User

async def add_user(user_id: int, user_name: str, zhynys: str,city:str = None):
    try:
        users = User(user_id=user_id, user_name=user_name, zhynys=zhynys)
        await users.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.select('user_name').where(User.user_id == user_id).gino.scalar()
    return user

async def select_user_city(user_id):
    city = await User.select('city').where(User.user_id == user_id).gino.scalar()
    return city

async def sel_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def update_city(user_id,cityy):
    user = await sel_user(user_id)
    await user.update(city=cityy).apply()
