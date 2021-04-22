# recursive functions
def display_message():
    while True:
        print("Press Ctrl+C to stop!")
        display_message()

# write a function that adds that numbers in a range
# iterative solution
def add_numbers(upper):
    total = 0
    for number in range(upper + 1):
        total +=number
    return total

# recursive solution
def addNumbers(upper):
    total = 0
    if upper == 0:
        return upper
    else:
        return  upper + addNumbers(upper-1)

# calculate a factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return  num + factorial(num-1)

# calculate a fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-1)