import time
import os

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter your name: ")
    print(f"{name}, here are the responses to questions #1, #2, #3:")
    print("\n#1. class Poodle(Dog):")
    print("\n#2. I'm a plant.")
    print("\n#3. class Cola(Beverage):\n\t\tdef_init_(self):\n\t\t\tBeverage.__init__(self, 'cola')")


if __name__ == '__main__':
    main()
