from typing import Dict, List
from models.category import Category
from exceptions.item_exists import ItemExistsException

class CategoryRepo:
    def __init__(self) -> None:
        self.__categories: Dict[int, Category] = {}

    def add_category(self, name:str):
        if not self.get_category_by_name(name):
            new_category = Category(name)
            self.__categories[new_category.get_id()] = new_category
            return new_category
        else:
            raise ItemExistsException(f"Category with name: {name} already exists")

    def get_category_by_name(self, name:str)->Category:
        for category in self.__categories.values():
            if category.get_name() == name:
                return category

        return None


    def get_all_categories(self)->List[Category]:
        return [category for category in self.__categories.values()]
    
    def remove_category(self, id:int):
        pass