from typing import List, Dict
from entities.topping import Topping
from entities.ingredient import Ingredient

class ToppingService:
    def __init__(self) -> None:
        self.__toppings:Dict[int, Topping] = {}

    def get_all_toppings(self)->List[Topping]:
        return [tp for tp in self.__toppings]
    
    def add_topping(self, ingredient:Ingredient, qty:int):
        topping = Topping(ingredient, qty)
        self.__toppings[topping.get_id()] = topping
        return topping

    def get_topping_by_ingredient_name(self, ingredient_name:str):
        for topping in self.__toppings.values():
            if topping.get_ingredient().get_name() == ingredient_name:
                return topping
            
        return None
    