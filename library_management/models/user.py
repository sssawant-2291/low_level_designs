
class LibUser:
    prev_id = 0
    def __init__(self, fname:str, lname:str, address:str, contact:str, is_admin:bool) -> None:
        LibUser.prev_id += 1
        self.__id = LibUser.prev_id

        self.__fname = fname
        self.__lname = lname
        self.__address = address
        self.__contact = contact
        self.__is_admin = is_admin
        self.__is_book_issued = False

    def get_fname_lname(self)->str:
        return f"{self.__fname} {self.__lname}"
    
    def get_id(self):
        return self.__id
    
    def is_book_issued(self):
        return self.__is_book_issued
    
    def set_book_issued(self, value):
        self.__is_book_issued = value
        
    def __str__(self) -> str:
        return f"""
                    User:
                    Name: {self.__fname} {self.__lname}
                    Address: {self.__address}
                    Contact: {self.__contact}
                    is_admin: {"YES" if self.__is_admin else "NO"}
                    is_book_issued: {"YES" if self.__is_book_issued else "NO"}
                """