import aiosqlite
from models import Book


class BookRepository:
    def __init__(self, db_path):
        self.db_path = db_path


    async def init_tables(self) -> None:
        sql_command = """
        CREATE TABLE IF NOT EXISTS `Books`(
        `id` INTEGER AUTOINCREMENT PRIMARY KEY,
        `user_id` INTEGER NOT NULL,
        `title` TEXT UNIQUE NOT NULL,
        `pages_read` INTEGER DEFAULT 0,
        `pages_count` INTEGER NOT NULL,
        `created_at` TEXT NOT NULL
        );
        """
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(sql_command)
            await db.commit()


    async def create_book(self, user_id: int, title: str) -> Book:
        sql_command = """
        INSERT INTO `Books` (`user_id`, `title`) VALUES (
        ?, ?, ?
        );
        """
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            await db.execute(sql_command, [user_id, title])
            await db.commit()
            command = """
            SELECT * FROM `Books`
                WHERE `Books`.`title` = ?;
            """

            cursor = await db.execute(command, [title])
            book = await cursor.fetchone()
            return Book(**dict(book))


    async def update_pages(self, user_id: int, book_id: int, pages: int) -> Book:
        sql_command = """
        UPDATE `Books` SET `pages_read` = ?
            WHERE `Books`.`id` = ? AND `Books`.`user_id` = ?;
        """

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row

            await db.execute(sql_command, [book_id, user_id, pages])
            await db.commit()
            command = """
            SELECT * FROM `Books` 
                WHERE `Books`.`id` = ?;
            """

            cursor = await db.execute(command, [book_id])
            book = await cursor.fetchone()
            return Book(**dict(book))


    async def fetch_books(self, user_id: int) -> list[Book]:
        command = """
        SELECT * FROM `Books` 
            WHERE `Books`.`user_id` = ?;
        """

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(command, [user_id])
            book = await cursor.fetchone()
            return Book(**dict(book))


    async def delete_book(self, user_id: int, book_id: int) -> None:
        command = """
        DELETE FROM `Books`
            WHERE `Books`.`id` = ? AND `Books`.`user_id` = ?;
        """

        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            await db.execute(command, [book_id, user_id])
            await db.commit()