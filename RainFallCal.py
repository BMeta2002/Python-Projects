# RainFall
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter your name:")
    num_years = eval(input("Enter the number of years: "))
    if num_years <= 0:
        print("Invalid, years entered must be greater than 0 \nTry Again!")
    cal_rain_fall(name, num_years)


def cal_rain_fall(name, num_years):
    rain_sum = 0
    for i in range(num_years):
        print(f"For year {i+1}")
        for j in range(12):
            rain_fall = eval(input('Enter the inches of rainfall for this month:'))
            num_months = (1+i) * 12
            rain_sum += rain_fall
            average = rain_sum / num_months

        print(f"{name}, here are your results: ")
        print(f"For {num_months} months")
        print(f"Total rainfall: {rain_sum:,.2f} inches")
        print(f"Average monthly rainfall: {average:,.2f} inches")


main()
