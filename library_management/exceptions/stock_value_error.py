class StockValueError(Exception):
    def __init__(self, msg:str, *args: object) -> None:
        super().__init__(*args)
        self.error_msg = msg
        