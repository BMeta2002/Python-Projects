# mph calculator
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))

name = input("Enter your name: ")


def main():
    speed = eval(input("Enter the speed of the vehicle in mph: "))
    hours = eval(input("Enter the number of hours traveled: "))
    show_travel(speed, hours)


def show_travel(speed, hours):
    print(f"\nHours \t Distance Traveled \n")
    print("---------------------------------")
    total = 0
    for i in range(1, hours + 1):
        distance = i * speed
        totals = total + distance
        print(f"{i} \t {distance:,.2f}")
    print("---------------------------------")
    print(f"{name}, the total cumulative distance traveled is  {totals:,.2f} miles.")


main()
