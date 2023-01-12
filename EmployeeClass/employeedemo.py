import time
import os
import productionworker

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():

    name = input("Enter your name: ")
    employee = input("Enter the employee's name: ")
    employee_id = eval(input("Enter the ID number: "))
    shift = eval(input("Enter the shift number: "))
    pay_rate = eval(input("Enter the hourly pay rate: "))
    print(f"{name}, here is the production worker, {employee}'s information:\n")

    emp1 = productionworker.ProductionWorker(employee, employee_id, shift, pay_rate)

    print(f"Name: {emp1.get_name()}")
    print(f"ID number: {emp1.get_id()}")
    print(f"Shift: {emp1.get_shift()}")
    print(f"Hourly Pay Rate: ${emp1.get_pay_rate():,.2f}")


main()
