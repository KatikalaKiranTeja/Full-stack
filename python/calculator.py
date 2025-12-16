# Simple calculator program using class and while loop
class calculator:
    # Displaying the list of available operations
    print("Types of operations")
    print(" 1.add \n 2.sub \n 3.mul \n 4.div \n 5.reminder \n 6.exit")

    # Constructor to initialize the calculator object with a name
    def __init__(self, name):
        self.name = name

    # Method to perform addition
    def add(self, a, b):
        return a + b

    # Method to perform subtraction
    def sub(self, a, b):
        return a - b

    # Method to perform multiplication
    def mul(self, a, b):
        return a * b

    # Method to perform division
    def div(self, a, b):
        return a / b

    # Method to find remainder
    def reminder(self, a, b):
        return a % b
# Taking user name as input
name = input("Enter your name :")
# Creating an object of the calculator class
call1 = calculator(name)

# Infinite loop for continuous operation until user exits
while True:
    n = int(input("Enter option:"))  # Taking operation choice from user

    # If user selects 6, program exits
    if n == 6:
        break

    # Option 1 - Addition
    elif n == 1:
        a, b = map(int, input("Enter values :").split())
        print(call1.add(a, b))

    # Option 2 - Subtraction
    elif n == 2:
        a, b = map(int, input("Enter values :").split())
        print(call1.sub(a, b))

    # Option 3 - Multiplication
    elif n == 3:
        a, b = map(int, input("Enter values :").split())
        print(call1.mul(a, b))

    # Option 4 - Division
    elif n == 4:
        a, b = map(int, input("Enter values :").split())
        print(call1.div(a, b))

    # Option 5 - Remainder
    elif n == 5:
        a, b = map(int, input("Enter values :").split())
        print(call1.reminder(a, b))

    # If none of the above options match
    else:
        print("Please enter a valid option")
