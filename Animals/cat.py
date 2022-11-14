"""
cat.py
This code is part of Martin Y Projects set 2022
__author__: Martin Yanev
__modified__: Initial Check-In 29/04/2022
"""

from pet import Pet


class Cat(Pet):
    def __init__(self, name, hates_dogs, age):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs
        self.age = age

    def hates_dogs(self):
        return self.hates_dogs

    def get_age(self):
        return self.age











