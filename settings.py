import types


class Setting:

    def __init__(self, size=(1., 1., 1.), size_units="world", color="absolute", pos=(0., 0., 0.), axis=(0., 0., 1.)):
        self.size = size
        self.size_units = size_units
        self.color = color
        self.pos = pos
        self.axis = axis

    def Get_Size(self):
        return self.size

    def Get_Size_Units(self):
        return self.size_units

    def Get_Color(self):
        return self.color

    def Get_Pos(self):
        return self.pos

    def Get_Axis(self):
        return self.axis

    def Set_Size(self, size=""):
        if types.TupleType == type(size):
            self.size = size
        else:
            print("  # Size (tuple): length, width, height")
            self.Set_Size(input())

    def Set_Size_Units(self, size_units=""):
        string = types.StringType == type(size_units)
        valid = "world" == size_units or "pixels" == size_units
        if string and valid:
            self.size_units = size_units
        else:
            print("  # Size_Units (string): \"world\" or \"pixels\"")
            self.Set_Size_Units(input())

    def Set_Color(self, color=[]):
        string = types.StringType == type(color)
        valid = "abs" == color or "mid" == color
        if string and valid:
            self.color = color
        else:
            print("  # Color (string): \"abs\" or \"mid\"")
            self.Set_Color(input())

    def Set_Pos(self, pos=""):
        if types.TupleType == type(pos):
            self.pos = pos
        else:
            print("  # Pos (tuple): x, y, z")
            self.Set_Pos(input())

    def Set_Axis(self, axis=""):
        if types.TupleType == type(axis):
            self.axis = axis
        else:
            print("  # Axis (tuple): v(x, y, z)")
            self.Set_Axis(input())

settings = Setting()

def Set():
    settings.Set_Size()
    settings.Set_Size_Units()
    settings.Set_Color()
    settings.Set_Pos()
    settings.Set_Axis()
    
def Get_Size():
    return settings.Get_Size()

def Get_Size_Units():
    return settings.Get_Size_Units()

def Get_Color():
    return settings.Get_Color()

def Get_Pos():
    return settings.Get_Pos()

def Get_Axis():
    return settings.Get_Axis()
