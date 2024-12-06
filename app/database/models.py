from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

#Подключение и создание базы данных
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase): #Основной класс База 
    pass

class User(Base): #Класс полльзовтеля
    __tablename__ = 'users' # Название 

    id: Mapped[int] = mapped_column(primary_key=True) # Идентификатор для бота 
    tg_id = mapped_column(BigInteger) #Идентификатор для распознавания пользователя


class Category(Base): #Класс категории товара
    __tablename__ = 'catigories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25)) #String это ограничитель на вводимое колл-во символов


class Item(Base):#Класс где будет находиться товар
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25)) #Имя товара
    description: Mapped[str] = mapped_column(String(120)) #Описание 
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('catigories.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

