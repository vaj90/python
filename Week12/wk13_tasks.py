# Task 1
# - Create a class called Home
# - Give the class three properties that cannot be accessible outside of the class.
# - Create the accessors and mutators for these instance variables.
# - Create a constructor that takes 3 arguments and passes each argument to the appropriate property
# - Override the default implementation of the toString method to summarize the 3 properties of Home

class Home:
    _size = 0
    _color = ''
    _no_of_room = 0

    def __init__(self, Color='', Size=0, NoOfRoom=0):
        self._size = Size
        self._no_of_room = NoOfRoom
        self._color = Color

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color

    @property
    def noofroom(self):
        return self._no_of_room

    @size.setter
    def size(self, data):
        self._size = data

    @color.setter
    def color(self, data):
        self._color = data

    @noofroom.setter
    def color(self, data):
        self._no_of_room = data

    def __str__(self):
        return "Size: {0}sqm\nNo of Room: {1}\nColor: {2}".format(self._size, self._no_of_room, self.color)

    def toString(self):
        return self.__str__()


newHome = Home("white", 200, 5)
# print(newHome.__str__())
print(newHome.toString())


# Task 2
# - Create a class called Apartment that is based on the Home class.
# - Give the class two additional properties that can be accessed outside of the class
# - Allow the Apartment class to be constructed like the Home class. (3 marks)
# - Create a constructor that takes 5 arguments and passes each argument to the appropriate properties
# - Override the toString to include the summary of the two new instance variables of Apartment
class Apartment(Home):
    _has_parking = False

    def __init__(self, Color, Size, NoOfRoom, SuiteNo, HasParking=False):
        super().__init__(Color, Size, NoOfRoom)
        self._suite_no = SuiteNo
        self._has_parking = HasParking

    def __str__(self):
        return "Suite No: {0}\n{1}\nHas Parking: {2}".format(self._suite_no, super().__str__(),  "Yes" if self. _has_parking else "No")

    def toString(self):
        return self.__str__()


print("\n")
apartment = Apartment("white", 200, 5, 1216)
print(apartment.__str__())