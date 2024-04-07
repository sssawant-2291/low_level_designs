from typing import List
from entities.ingredient import Ingredient
from exceptions.item_already_exists import ItemAlreadyExists

class IngredientService:
    def __init__(self) -> None:
        self.__ingredients = {}

    def get_all_ingredients(self)->List[Ingredient]:
        return [ing for ing in self.__ingredients.values()]
    
    def add_ingredient(self, name:str, price_perUnit:float):
        if name not in self.__ingredients:
            ingr = Ingredient(name, price_perUnit)
            self.__ingredients[name] = ingr
            return ingr
        else:
            raise ItemAlreadyExists(f"Ingredient with name: {name} already exists")
        
    def get_ingredient_by_name(self, name:str)->Ingredient:
        if name in self.__ingredients:
            return self.__ingredients[name]
        else:
            return None
        