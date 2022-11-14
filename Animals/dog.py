"""
dog.py
This code is part of Martin Y Projects set 2022
__author__: Martin Yanev
__modified__: Initial Check-In 29/04/2022
"""

from pet import Pet


class Dog(Pet):
    def __init__(self, name, chases_cats, age):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
        self.age = age

    __secret = "This is a secret"
    not_a_secret = "Not a secret"

    def chases_cats(self):
        return self.chases_cats

    def get_age(self):
        return self.age











