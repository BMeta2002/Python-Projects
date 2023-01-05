import time
import os

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    numbers_verify = []
    user_name = input("Enter your name: ")

    while True:
        account_name = input("Enter account to open: ")
        try:
            numbers = open(account_name, 'r')
        except FileNotFoundError:
            print("The file could not be found")
            continue

        for i in range(5):
            account = numbers.readline()
            account = account.rstrip("\n")
            numbers_verify.append(account)

        for i in range(5):
            user_number = input("Enter the account number to be validated: ")
            if user_number in numbers_verify:
                print(f'Account number {user_number} is valid.')
            else:
                print(f'Account number {user_number} is not valid.')

        ask = input(f'\n{user_name} , do you want to continue, press Y or N: ')
        if ask == "N":
            break
        elif ask == "Y":
            continue


if __name__ == '__main__':
    main()
