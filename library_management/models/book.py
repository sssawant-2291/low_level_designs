from models.user import LibUser
from datetime import datetime

class Book:
    def __init__(self, ISBN, title, author, category, pages) -> None:
        self.__ISBN = ISBN
        self.__title = title
        self.__author = author
        self.__category = category
        self.__pages = pages
        self.__issued_to = None
        self.__issued_on = None

    def mark_issued(self, user:LibUser, time_stamp:datetime):
        self.__issued_to = user
        self.__issued_on = time_stamp

    def __str__(self):
        return f"""
                Book: 
                Title: {self.__title}
                Author: {self.__author}
                category: {self.__category}
                issued_to: {self.__issued_to}
                issued_on: {self.__issued_on}
                """
