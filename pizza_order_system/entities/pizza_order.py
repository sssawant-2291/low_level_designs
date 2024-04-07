from entities.pizza import Pizza

class PizzaOrder:
    prev_id = 0
    def __init__(self, pizza:Pizza, qty:int) -> None:
        self.__id = PizzaOrder.prev_id + 1
        PizzaOrder.prev_id = self.__id

        self.__pizza = pizza
        self.__qty = qty
        self.__calc_price()

    def __calc_price(self):
        self.__tax_price = (self.__pizza.get_price() * self.__qty) * 1.20

    def get_id(self):
        return self.__id
    
    def get_price(self):
        return self.__tax_price