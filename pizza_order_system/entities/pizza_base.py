class PizzaBase:
    def __init__(self, name:str, price:float) -> None:
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

# if __name__ == "__main__":
#     b = Base("plain", 80)
#     b._Base__name = "flat_plain"
#     print(b._Base__name)


