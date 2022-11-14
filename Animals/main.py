"""
main.py
This is the main runner module
This code is part of Martin Y Projects set 2022
__author__: Martin Yanev
__modified__: Initial Check-In 29/04/2022
"""

from cat import Cat
from dog import Dog

MAX_AGE = 12

# Creating pets for instance classes.
larry = Dog("Larry", True, 7)
mellow = Cat("Mellow", False, 10)

# Print statements to show the pet type and intro.
print(mellow.get_species())
print(larry.get_species())
print(larry)
print(mellow)

# Assigns a user input to larry's age and checks if the input is an integer.
try:
    larry.age = int(input("Please enter dog's age: "))
except ValueError:
    print("ERROR: This is not a valid dog age."
          " Age must be an integer")
print(larry.get_age())

# Checks if larry age is higher or lower than the MAX_AGE.
if larry.get_age() > MAX_AGE:
    print(larry.get_name(), "is too old")
else:
    print(larry.get_age(), "is still young")












