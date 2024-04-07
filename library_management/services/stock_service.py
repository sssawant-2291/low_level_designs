from models.stock import BookStock
from models.book import Book
from exceptions.item_exists import ItemExistsException
from exceptions.stock_value_error import StockValueError
from repos.stock_repo import StockRepo

class StockService:
    def __init__(self) -> None:
        self.stock_repo = StockRepo()

    def add_new_book(self, book:Book, in_stock:int):
        try:
            if in_stock < 0:
                raise StockValueError("In stock can't be negative value")
            self.stock_repo.add_new_book(book, in_stock)
        except ItemExistsException as e:
            raise e
        except StockValueError as e:
            raise e
        
    def get_stock_by_book(self, book:Book)->BookStock:
        return self.stock_repo.get_stock_by_book(book)


    def update_stock(self, book:Book, in_stock:int):
        self.stock_repo.update_stock(book, in_stock)