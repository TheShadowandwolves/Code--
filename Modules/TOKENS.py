
class Token:
    def __init__(self, type, value, pos):
        self.type = type
        self.value = value
        self.pos = pos

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
    
    def getPos(self):
        return self.pos

    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return self.__str__()
 

