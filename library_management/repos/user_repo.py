from typing import Dict, List
from models.user import LibUser
from exceptions.item_exists import ItemExistsException
from models.book import Book
from datetime import datetime as dt

class UserRepo:
    def __init__(self) -> None:
        self.__users: Dict[int, LibUser] = {}

    
    def add_user(self, fname:str, lname:str, address:str, contact:str, is_admin:bool):
        if not self.get_user_by_name(fname, lname):
            new_user = LibUser(fname, lname, address, contact, is_admin)
            self.__users[new_user.get_id()] = new_user
            return new_user
        else:
            raise ItemExistsException(f"User with {fname} {lname} already exists")

    def issue_book(self, user:LibUser, book:Book):
        if not user.is_book_issued():
            book.mark_issued(user, dt.now())
            user.set_book_issued(True)
        
    def get_user_by_name(self, fname:str, lname:str)->LibUser:
        name = f"{fname} {lname}"

        for user in self.__users.values():
            if user.get_fname_lname() == name:
                return user
            
        return None
        
    def get_user_by_id(self, id:int)->LibUser:
        if id in self.__users:
            return self.__users[id]
        
        return None
    
    def get_all_users(self)->List[LibUser]:
        return self.__users.values()
    
    def delete_user(self, id:int):
        if id in self.__users:
            del self.__users[id]
