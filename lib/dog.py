#!/usr/bin/env python3
import ipdb; 

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, breed = "Mastiff", name = "Bruno"):
        # print("Initializing")
        self.breed = breed
        self.name = name

    def set_name(self, name):
        # print("Setting name")
        if type(name) != str:
            print('Name must be string between 1 and 25 characters.')
        elif 0 >= len(name) or 25 < len(name):
            print('Name must be string between 1 and 25 characters.')
        else: self._name = name

    def get_name(self):
        # print("Getting name")
        return self._name

    def get_breed(self):
        # print("Getting Breed")
        return self._breed

    def set_breed(self, breed):
        # print("Setting Breed")
        if breed in APPROVED_BREEDS:
            self._breed =  breed
        else: print('Breed must be in list of approved breeds.')


    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


# ipdb.set_trace()