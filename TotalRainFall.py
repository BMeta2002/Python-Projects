import time
import os
print("Programmer: " + os.getlogin())
print("Lab 15.4" + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    rainfall = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December "]

    username = input("Enter your name: ")

    for month in months:

        user_rain = f"Enter the rainfall for {month}: "
        user_rain2 = eval(input(f"{user_rain: <40}"))
        rainfall.append(user_rain2)

    total_rainfall = sum(rainfall)
    avg_rainfall = total_rainfall / 12
    highest = max(rainfall)
    lowest = min(rainfall)

    print(f"{username}, here are the results: ")
    print(f"Total rainfall :    {total_rainfall:,.2f}")
    print(f"Average rainfall:   {avg_rainfall:,.2f}")
    print(f"Highest rainfall:   {highest:,.2f}")
    print(f"Lowest rainfall:    {lowest:,.2f}")


if __name__ == '__main__':
    main()
