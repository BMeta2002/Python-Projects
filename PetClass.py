import time
import os

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age


user_name = input("Enter your name: ")
pet_name = input("Enter the name of your pet: ")
animal_type = input("Enter the type of animal: ")
age = input("Enter the age of your pet: ")

pet = Pet(pet_name, animal_type, age)

print(f"\n {user_name}, here is the data about your pet:\n")
print("Pet's name:", pet.get_name())
print("Pet's type:", pet.get_animal_type())
print("Pet's age:", pet.get_age())
