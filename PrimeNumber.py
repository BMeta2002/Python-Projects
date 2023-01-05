# Prime Number
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter Your Name: ")
    number = eval(input("Enter A Integer: "))

    if prime is False:
        print(f"{name}, {number} is not a prime number")
    elif number == 0:
        print("Enter a number other then 0 or 1")
        print(f"{name}, {number} is not a prime number")
    else:
        print(f"{name}, {number} is a prime number")

    prime(number)


def prime(number):
    if number != 0 and number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True


main()
