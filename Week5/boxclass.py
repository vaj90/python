class Box :
    numBoxes = 0
    #constructor
    def __init__(self, Name= '', Width=0, Height=0, Depth=0):
        self.name=Name
        self.__width=Width
        self.__height=Height
        self.depth=Depth
        pass

    #getter && setter
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, newValue):
        self.__width = newValue

    @height.setter
    def height(self, newValue):
        self.__height = newValue

    #destructor
    def __del__(self):
        print("Destroying Box")

    def area(self):
        return  self.height * self.__width

    def volume(self):
        return  self.height * self.__width * self.depth

    def MyClassMethod(cls):
        return cls.name + " is the name of the class!"

    def StaticMethod(self):
        return "Hello from my static class " + __class__.__name__
