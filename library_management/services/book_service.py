from models.book import Book
from models.category import Category
from repos.book_repo import BookRepo
from models.book import Book

class BookService:
    def __init__(self) -> None:
        self.book_repo = BookRepo()

    def add_book(self, ISBN:str, title:str, author:str, category:Category, pages:int)->Book:
        try:   
            return self.book_repo.add_book(ISBN, title, author, category, pages)
        except Exception as e:
            raise e
        
    def get_book_by_ISBN(self, ISBN:str)->Book:
        return self.book_repo.get_book_by_ISBN(ISBN)