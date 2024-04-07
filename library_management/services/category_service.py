from typing import List
from repos.category_repo import CategoryRepo
from models.category import Category

class CategoryService:
    def __init__(self) -> None:
        self.cat_repo = CategoryRepo()

    def add_category(self, name:str)->Category:
        try:
            return self.cat_repo.add_category(name)
        except Exception as e:
            raise e

    def get_category_by_name(self, name:str)->Category:
       return self.cat_repo.get_category_by_name(name)


    def get_all_categories(self)->List[Category]:
        return self.cat_repo.get_all_categories()
    
