# Task 3
# -Create a class named Instrument
# -Give it a
#       -constructor
#           -all with default values
#       -destructor
#       -2 public properties
#       -1 private property
#       -a tostring method
class Instrument:
    def __init__(self, serialCode='', types='Strings', name='Violin'):
        self._serialCode = serialCode
        self.types = types
        self.name = name

    _serialCode = ''
    types = ''
    name = ''

    def __del__(self):
        print("Destructor called")

    def toString(self):
        return "Serial Code: {0}\nTypes: {1}\nName: {2}".format(self._serialCode, self.types, self.name)


# inst = Instrument()
# print(inst.toString())
