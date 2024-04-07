# Functional requirements
Functional Requirements for a Library Management System
The following are the functional requirements for a Library Management System:

Ability to add and remove books from the library
Ability to search for books in the library by title, author, or ISBN
Ability to check out and return books
Ability to display a list of all books in the library
Ability to store and retrieve information about library patrons, including their name and ID number
Ability to track which books are currently checked out and when they are due to be returned
Ability to generate reports on library usage and checkouts

# Entities/ Models
1. User
    - id
    - fname
    - lname
    - address
    - contact
    - is_admin
    - book

2. Category
    - id
    - name

3. Book
    - ISBN
    - title
    - author
    - category
    - pages
    - issued_to
    - issued_at

4. Stock
    - id
    - book
    - in_stock

# Repositories
1. User repo
    - add_user(fname, lname, address, contact, is_admin)
    - issue_book(user, book)
    - get_user(fname, lname)
    - get_user(id)
    - get_all_users()
    - delete_user(id)

2. CAtegory repo
    - add_category(name)
    - get_all_categories()
    - remove_category(id)

3. Book repo
    - add_book(ISBN, title, author, category, pages, is_available)


4. Stock repo
    - add_new_book(book, in_stock)
    - update_stock(book, in_stock)