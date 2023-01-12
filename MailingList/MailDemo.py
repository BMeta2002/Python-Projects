import time
import os
from Mail import *

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    username = input("Enter your name: ")
    cust = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    phone_num = input("Enter the customer's phone_number: ")
    num = input("Enter the customer's number: ")
    y_or_n = input("Does the customer wish to be on the mailing list?(Yes/No) ")

    cust1 = Customer("", "", "", "", "")
    cust1.set_name(cust)
    cust1.set_address(address)
    cust1.set_tele(phone_num)
    cust1.set_num(num)
    cust1.set_yn(y_or_n)

    print(f'{username}, here is the customer, {cust}\'s information:\n')

    print(f'Name: {cust1.get_name()}')
    print(f'Address: {cust1.get_address()}')
    print(f'Phone number: {cust1.get_tele()}')
    print(f'Customer Number: {cust1.get_num()}')
    print(f'On Mailing List: {cust1.get_yn()}')


main()
