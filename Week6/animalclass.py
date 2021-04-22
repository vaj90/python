class Animal:
    def __init__(self, Name='', Gender='', Weight=0, Height=0):
        self.name = Name
        self.gender = Gender
        self._weight = Weight
        self._height = Height
    def getName(self):
        return "the class name is " + __class__.__name__ + "\n" + \
            " and the object name is " + self.name

    def isFemale(self):
        if len(self.gender) == 1 and ord(self.gender) == 70 or ord(self.gender) == 102:
            return True
        return False

class Dog(Animal):
    def __init__(self, Name='', Gender='', Weight=0, Height=0, Teeth=0):
        super().__init__(Name, Gender, Weight, Height)
        self.teeth = Teeth
