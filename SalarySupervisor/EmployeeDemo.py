import time
import os
from Employee import *

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    username = input("Enter your name: ")
    shift = input("Enter the employee name: ")
    id_num = input("Enter the ID number: ")
    salary = input("Enter the annual salary: ")
    bonus = input("Enter the bonus: ")

    sup = ShiftSupervisor(shift, id_num, salary, bonus)

    print(f'{username}, here is the Shift supervisor,{shift}\'s information:\n')

    print(f'Name: {sup.get_name()}')
    print(f'ID number: {sup.get_number()}')
    print(f'Shift: {int(sup.get_salary()):,.2f}')
    print(f'Hourly Pay Rate: ${int(sup.get_bonus()):,.2f}')


main()
