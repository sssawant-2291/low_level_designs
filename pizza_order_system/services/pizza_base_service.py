from typing import List
from entities.pizza_base import PizzaBase
from exceptions.item_already_exists import ItemAlreadyExists

class PizzaBaseService:
    def __init__(self) -> None:
        self.__pizza_bases = {}
    
    def get_all_bases(self)->List[PizzaBase]:
        return [pizza for pizza in self.__pizza_bases.values()]
    
    def get_base_by_name(self, name:str)->PizzaBase:
        if name in self.__pizza_bases:
            return self.__pizza_bases[name]
        return None
    
    def add_base(self, name:str, price:float):
        if name not in self.__pizza_bases:
            pizza_base = PizzaBase(name, price)
            self.__pizza_bases[name] = pizza_base
            return pizza_base
        else:
            raise ItemAlreadyExists(f"Pizza Base with name: {name} already exists")