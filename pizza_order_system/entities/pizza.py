from typing import List
from entities.pizza_base import PizzaBase
from entities.topping import Topping

class Pizza:
    prev_id = 0
    def __init__(self, base:PizzaBase, toppings:List[Topping]) -> None:
        self.__id = Pizza.prev_id + 1
        Pizza.prev_id = self.__id

        self.__base = base
        self.__toppings = toppings
        self.__calcPrice()

    def __calcPrice(self):
        base_price = self.__base.get_price()
        toppping_price = 0

        for topping in self.__toppings:
            toppping_price += topping.get_price()

        self.__price = base_price + toppping_price

    def get_id(self):
        return self.__id
    
    def get_price(self):
        return self.__price

    def __str__(self) -> str:
        return f"{self.__id}"
    
if __name__ == "__main__":
    p1 = Pizza("base", ["topping"])
    p2 = Pizza("base", ["topping"])
    p3 = Pizza("base", ["topping"])
    
    print(p1, p2, p3)