from entities.ingredient import Ingredient

class Topping:
    prev_id = 0
    def __init__(self, ingredient:Ingredient, qty:int) -> None:
        self.__id = Topping.prev_id + 1
        Topping.prev_id = self.__id
        
        self.__ingredient = ingredient
        self.__qty = qty
        self.__calc_price()

    def get_id(self):
        return self.__id
    
    def __calc_price(self):
        self.__price = self.__ingredient.get_price() * self.__qty

    def get_ingredient(self):
        return self.__ingredient
    
    def get_price(self):
        return self.__price