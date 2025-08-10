from Telegram_bots.hw_2.service import BookService
from aiogram.filters import command
from aiogram import Router, F, types


router = Router()


@router.message(command.CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Бот готов помочь разобраться с библиотекой!.")

@router.message(command.Command("add_book"))
async def add_book_handler(message: types.Message, command: command.CommandObject):
    await message.answer("Пожалуйста, введите команду /add_book <название_книги> <количество_страниц>")
    if len(command.args.split()) < 2:
        raise ValueError

    title = " ".join(command.args.split()[:-1])
    pages_count = int(command.args.split()[1])
    user_id = message.from_user.id

    await BookService.add_book(user_id, title, pages_count)
    await message.answer(f"Книга '{title}' успешно добавлена!")


@router.message(command.Command("remove_book"))
async def remove_handler(message: types.Message, command: command.CommandObject):
    if command.args and command.args.isdigit():
        await BookService.remove_book(message.from_user.id, int(command.args))
        await message.answer("Книга удалена!")
    else:
        await message.answer("Использование: /remove_book <id>")

@router.callback_query(F.data.startswith("remove_"))
async def remove_callback_handler(callback: types.CallbackQuery):
    parts = callback.data.split("_")
    if len(parts) == 2 and parts[1].isdigit():
        await BookService.remove_book(callback.from_user.id, int(parts[1]))
        await callback.message.answer("Книга удалена!")
    await callback.answer()
