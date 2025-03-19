import sqlite3


class UserTable:

    def __init__(self):
        self.__connect = sqlite3.connect('database.db')
        self.__cursor = self.__connect.cursor()

    def __create_user_table(self) -> None:
        """
        Создает таблицу для хранения данных пользователей
        :return: None
        """
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        telegram_id INTEGER NOT NULL,
        email TEXT,
        notifications TEXT
        )
        """)

        self.__connect.commit()


class VacanciesTable:

    def __init__(self):
        self.__connect = sqlite3.connect('database.db')
        self.__cursor = self.__connect.cursor()

    def __create_vacancies_table(self) -> None:
        """
        Создает таблицу для хранения данных вакансии
        :return: None
        """
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        salary TEXT NOT NULL,
        company TEXT NOT NULL,
        description TEXT NOT NULL,
        link TEXT NOT NULL,
        city TEXT NOT NULL,
        date_added TEXT NOT NULL
        )
        """)

        self.__connect.commit()
