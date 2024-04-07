from typing import List, Dict
from models.book import Book
from models.category import Category
from exceptions.item_exists import ItemExistsException

class BookRepo:
    def __init__(self) -> None:
        self.__books: Dict[int, Book] = {}

    def add_book(self, ISBN:str, title:str, author:str, category:Category, pages:int):
        if not self.get_book_by_ISBN(ISBN):
            new_book = Book(ISBN, title, author, category, pages)
            self.__books[ISBN] = new_book
            return new_book
        else:
            raise ItemExistsException(f"Book with ISBN: {ISBN} already exists")
        
    def get_book_by_ISBN(self, ISBN:str)->Book:
        for book_isbn in self.__books:
            if book_isbn == ISBN:
                return self.__books[book_isbn]
            
        return None
    