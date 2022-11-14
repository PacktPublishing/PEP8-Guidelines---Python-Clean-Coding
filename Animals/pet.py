"""
pet.py
This code is part of Martin Y Projects set 2022
__author__: Martin Yanev
__modified__: Initial Check-In 29/04/2022
"""


class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)



