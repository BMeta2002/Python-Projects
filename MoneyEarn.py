#Money Earned
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter you name: ")
    num_days = eval(input("Enter the number of days: "))
    cal_salary(name, num_days)


def cal_salary(name, num_days):
    if 0 < num_days <= 31:
        print("Days \t \t \t \t \t Dollars")
        print("--------------------------------------")
        penny = 0.01
        current_days = 0
        for i in range(num_days):
            current_days += 1
            print(f"{current_days} \t \t \t \t {penny:>14,.2f}")
            penny = penny * 2
        print("-------------------------------------")
        print(f"{name}, you have earned a total of ${penny:,.2f} for {num_days} days worked.")

    else:
        print("Invalid, days entered must be greater than 0 and less than or equal to 31 \nTry Again")


main()
