
class SplitException(Exception):
    def __init__(self):
        super().__init__("Impossible to divide")
