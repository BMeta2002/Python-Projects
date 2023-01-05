import time
import os
import random
print("Programmer: " + os.getlogin())
print("Lab 15.2 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    username = input("Enter your name: ")

    lottery_numbers = []
    for i in range(7):
        lottery_numbers.append(random.randint(0, 9))

    print(f"{username}, these are the random number in the list: ")

    for number in lottery_numbers:
        print(number, end=', ')


if __name__ == '__main__':
    main()
