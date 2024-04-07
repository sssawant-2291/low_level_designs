class ItemAlreadyExists(Exception):
    def __init__(self, msg:str, *args: object) -> None:
        super().__init__(*args)
        self.err_msg = msg
    