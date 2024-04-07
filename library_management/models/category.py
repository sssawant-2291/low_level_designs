class Category:
    prev_id = 0
    def __init__(self, name) -> None:
        Category.prev_id += 1
        self.__id = Category.prev_id
        self.__name = name

    def get_name(self)->str:
        return self.__name
    
    def get_id(self)->int:
        return self.__id
    
    def __str__(self) -> str:
        return f"{self.__name}"