# Random Number Guesser
import random
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    attempts = 0
    name = input("Enter You Name: ")
    print(f"Hello, {name}, Welcome To The Guessing Number Game!! ")
    number = eval(input("Enter number between 1 and 100, or 0 to quit: "))

    if number == 0:
        print("You Quit? Goodbye!")
    guessing_game(name, number, attempts)


def guessing_game(name, number, attempts):
    random_number = random.randint(1, 100)

    while number != 0:
        if number > random_number:
            print("Too high, try again")
            number = eval(input("Enter number between 1 and 100, or 0 to quit: "))
            attempts += 1
        elif number < random_number:
            print("Too Low, try again")
            number = eval(input("Enter number between 1 and 100, or 0 to quit: "))
            attempts += 1
        else:
            attempts += 1
            print(f"Congrats {name}, you guessed the right number within {attempts} tries!! ")
            number = eval(input("Enter number between 1 and 100, or 0 to quit: "))
    return number


main()
