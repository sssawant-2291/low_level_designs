from typing import List, Dict
from models.stock import BookStock
from models.book import Book
from exceptions.item_exists import ItemExistsException

class StockRepo:
    def __init__(self) -> None:
        self.__stocks: Dict[int, BookStock] = {}

    def add_new_book(self, book:Book, in_stock:int):
        if not self.get_stock_by_book(book):
            new_stock = BookStock(book, in_stock)
            sid = new_stock.get_id()
            self.__stocks[sid] = new_stock
        else:
            raise ItemExistsException(f"Stock with book: {book} already exists")

    def get_stock_by_book(self, book:Book)->BookStock:
        for stock in self.__stocks.values():
            if stock.get_book_from_stock() == book:
                return stock
            
        return None


    def update_stock(self, book:Book, in_stock:int):
        stock = self.get_stock_by_book(book)
        if stock:
            stock.update_stock(in_stock)