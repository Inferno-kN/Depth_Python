import asyncio
import aiogram
from aiogram import types
from aiogram.filters import command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class KinomanBotData:

    def __init__(self):
        self.favorites = {}
        self.movies_db = {
            'comedy': {
                2022: ['чушь', 'чушь 2', 'чушь 3'],
                2023: ['хрень', 'хрень 2']
            },
            'drama': {
                2022: ['жесть', 'жесть 2'],
                2023: ['дичь']
            },
            'action': {
                2022: ['лютая хрень', "лютейшая хрень"],
                2023: ['ну уже нормас']
            }
        }


    def save_movie(self, user_id, movie_title):

        if user_id not in self.favorites:
            self.favorites[user_id] = []

        if movie_title not in self.favorites[user_id]:
            self.favorites[user_id].append(movie_title)
            return "Сохранено!"

        return "Фильм уже в избранном"

    def get_recommendation(self, genre, year):

        if genre in self.movies_db and year in self.movies_db[genre]:
            return self.movies_db[genre][year]

        return None

    def get_favorites(self, user_id):
        return self.favorites.get(user_id, [])


bot_data = KinomanBotData()

bot = aiogram.Bot(token='')
dp = aiogram.Dispatcher()

iter_movies = None
current_movie = None


def create_keyboard(names, bottons_in_row):

    kb_builder = ReplyKeyboardBuilder()

    for name in names:
        kb_builder.add(types.KeyboardButton(text= str(name)))
    kb_builder.adjust(bottons_in_row)

    return kb_builder.as_markup(resize_keyboard = True)


# Обработчик команды /start
@dp.message(command.CommandStart())
async def start_command(message: types.Message):

    REFERENCE = (
        "Привет! Я бот-киноман!\n\n"
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/recommend <жанр> <год> - получить рекомендацию\n"
        "/save <название фильма> - сохранить фильм\n"
        "/mylist - посмотреть избранные фильмы"
    )
    await message.answer(REFERENCE)


@dp.message(command.Command('mylist'))
async def mylist_command(message: types.Message):
    favorites = bot_data.get_favorites(message.from_user.id)
    if not favorites:
        await message.answer("Ваш список избранного пуст")
        return

    response = "Ваши избранные фильмы:\n"
    for i, movie in enumerate(favorites):
        response += f"{i+1}. {movie}\n"

    await message.answer(response)


@dp.message(command.Command('save'))
async def save_command(message: types.Message, command: command.Command):

    args = command.args
    if not args:
        await message.answer("Укажите название фильма после команды")
        return

    response = bot_data.save_movie(message.from_user.id, args)
    await message.answer(response)


@dp.message(F.text.lower() == 'сохранить')
async def save_button_handler(message: types.Message):
    global current_movie
    if current_movie:
        response = bot_data.save_movie(message.from_user.id, current_movie)
        await message.answer(response)
    else:
        await message.answer("Нет текущего фильма для сохранения.")


@dp.message(F.text.lower() == 'следующий')
async def next_button_handler(message: types.Message):
    global iter_movies, current_movie
    try:
        current_movie = next(iter_movies)
        await message.answer(current_movie)
    except StopIteration:
        await message.answer("Мне больше нечего предложить :(", reply_markup=types.ReplyKeyboardRemove())


@dp.message(command.Command('recommend'))
async def recommendation_film(message: types.Message, command: command.CommandObject):

    args = command.args
    if args is None:
        await message.answer("Используйте формат: /recommend <жанр> <год>")
        return

    args = list(map(lambda elem: int(elem) if elem.isdigit() else elem,args.split(' ')))
    find_movies = bot_data.get_recommendation(*args)

    if not find_movies:
        await message.reply("Таких фильмов нет :(")
        return

    global current_movie,iter_movies
    iter_movies = find_movies.__iter__()
    current_movie = iter_movies.__next__()
    await message.answer(current_movie, reply_markup=create_keyboard(["Сохранить", "Следующий"], 2))


async def main():
    print("Бот просыпайся")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())