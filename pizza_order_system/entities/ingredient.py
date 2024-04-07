class Ingredient:
    def __init__(self, name:str, price_perUnit:float) -> None:
        self.__name = name
        self.__price_perUnit = price_perUnit

    def get_price(self):
        return self.__price_perUnit
    
    def get_name(self):
        return self.__name
