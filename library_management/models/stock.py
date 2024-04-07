from models.book import Book

class BookStock:
    prev_id = 0
    def __init__(self, book:Book, in_stock:int) -> None:
        BookStock.prev_id += 1
        self.__id = BookStock.prev_id

        self.__book = book
        self.__in_stock = in_stock

    def get_book_from_stock(self)->Book:
        return self.__book
    
    def get_id(self)->int:
        return self.__id
    
    def update_stock(self, change_in_stock:int):
        if change_in_stock < 0 and abs(change_in_stock) >= self.__in_stock:
            self.__in_stock = 0
        else:
            self.__in_stock += change_in_stock

    def get_in_stock(self)->int:
        return self.__in_stock