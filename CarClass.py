import time
import os

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    # Car Class
    class Car:
        def __init__(self, year_model, make):
            self.__year_model = year_model
            self.__make = make
            self.__speed = 0

        def accelerate(self):
            self.__speed += 5

        def brake(self):
            self.__speed -= 5

        def get_speed(self):
            return self.__speed

    car = Car(2010, "Nissan")

    name = input("Enter your name: ")

    print(f"\n{name} the car is accelerating: ")
    for i in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()}")

    print(f"\n{name} the car is braking: ")
    for i in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()}")


if __name__ == '__main__':
    main()

