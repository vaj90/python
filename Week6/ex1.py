#function
def print_welcome():
    print("Welcome to the future value calculator ")
    print()

def print_welcome1(message):
    print(message)
    print()

message = "Welcome to the forest"
print_welcome1(message)

def calculating_miles_per_gallon(miles_driven, gallons_used):
    mpg = miles_driven / gallons_used
    mpg = round(mpg, 2)
    return mpg

miles = 500
gallons = 14

mpg = calculating_miles_per_gallon(miles,gallons)
print("the result of the miles per gallon function is: ", mpg)