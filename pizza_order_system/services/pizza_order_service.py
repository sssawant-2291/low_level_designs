from typing import List, Dict
from entities.pizza import Pizza
from entities.pizza_order import PizzaOrder

class PizzaOrderService:
    def __init__(self) -> None:
        self.__pizza_orders:Dict[int, PizzaOrder] = {}

    def add_order(self, pizza:Pizza, qty:int):
        pizza_order = PizzaOrder(pizza, qty)
        self.__pizza_orders[pizza_order.get_id()] = pizza_order
        return pizza_order
    
    def get_order_price(self, order_id:int)->float:
        if order_id in self.__pizza_orders:
            return self.__pizza_orders[order_id].get_price()
        return 0.0
    