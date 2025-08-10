import asyncio
from configs import TOKEN
from aiogram import Dispatcher, Bot
from Telegram_bots.hw_2.handlers import handler_books



async def main():
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_routers(handler_books.router)


    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
