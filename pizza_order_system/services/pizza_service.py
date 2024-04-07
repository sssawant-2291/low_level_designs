from typing import List
from entities.pizza_base import PizzaBase
from entities.topping import Topping
from entities.pizza import Pizza

class PizzaService:
    def __init__(self) -> None:
        self.__pizzas = {}

    def add_pizza(self, pizzabase:PizzaBase, toppings:List[Topping]):
        pizza = Pizza(pizzabase, toppings)
        self.__pizzas[pizza.get_id()] = pizza
        return pizza
    