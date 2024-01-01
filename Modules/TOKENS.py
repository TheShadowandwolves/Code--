
class Token:
    def __init__(self, type, value, pos):
        self.type = type
        self.value = value
        self.pos = pos

    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return self.__str__()
 

