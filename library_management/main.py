from services.book_service import BookService
from services.category_service import CategoryService
from services.stock_service import StockService
from services.user_services import UserService

if __name__ == "__main__":
    cat_service = CategoryService()
    c1 = cat_service.add_category("Science Fiction")

    book_service = BookService()
    b1 = book_service.add_book("B123", "The Book 1", "Author 1", c1, 150)

    user_service = UserService()
    admin1 = user_service.add_user("Sarvesh", "Sawant", "Kalyan", "7977751200", True)
    u1 = user_service.add_user("Nipun", "Sawant", "Kalyan", "8977745678", False)

    stock_service = StockService()
    stock_service.add_new_book(b1, 10)

    user_service.issue_book(u1, b1)

    all_users = user_service.get_all_users()
    for user in all_users:
        print(user)
    print(book_service.get_book_by_ISBN("B123"))