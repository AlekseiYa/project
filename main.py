import asyncio
from aiogram import Bot, Dispatcher, F

from app.hendlers import router


async def main():
    bot = Bot(token='7474106208:AAG7ZbEYG8IXGwIci68Qk34qP7sKMRWPF3I')
    dp = Dispatcher() #Диспетчер, обработчик входящих данных
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен. ')

