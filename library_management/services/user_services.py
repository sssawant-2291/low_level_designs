from typing import List
from repos.user_repo import UserRepo
from models.user import LibUser
from models.book import Book

class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepo()

    def add_user(self, fname:str, lname:str, address:str, contact:str, is_admin:bool):
        try:
            return self.user_repo.add_user(fname, lname, address, contact, is_admin)
        except Exception as e:
            raise e

    def issue_book(self, user:LibUser, book:Book):
        self.user_repo.issue_book(user, book)
        
    def get_user_by_name(self, fname:str, lname:str)->LibUser:
        return self.user_repo.get_user_by_name(fname, lname)
        
    def get_user_by_id(self, id:int)->LibUser:
        return self.user_repo.get_user_by_id(id)
    
    def get_all_users(self)->List[LibUser]:
        return self.user_repo.get_all_users()
    
    def delete_user(self, id:int):
        self.user_repo.delete_user(id)