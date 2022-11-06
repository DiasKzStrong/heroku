from sqlalchemy import Column, BigInteger, String,sql

from utils.dp_api.db_namaz import TimedBaseModel

class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger,primary_key=True)
    user_name = Column(String(200),primary_key=True)
    zhynys = Column(String(200),primary_key=True)
    city = Column(String(200))

    query: sql.select
