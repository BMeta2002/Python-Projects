# OverTime Calculator

import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


REGULAR_HOURS = 40
OT_RATE = 1.5


def main():
    user_name = input("Enter Your User Name:")
    hours_worked = eval(input("Enter The Amount Of Hours Worked This Week:"))
    hour_rate = eval(input("Enter The Hourly Rate:"))
    pay_cal(user_name, hours_worked, hour_rate)


def pay_cal(user_name, hours_worked, hour_rate):
    if hours_worked > 40:
        ot_pay(user_name, hours_worked, hour_rate)
    else:
        rg_pay(user_name, hours_worked, hour_rate)


def ot_pay(user_name, hours_worked, hour_rate):
    over_time_num = hours_worked - REGULAR_HOURS
    over_time_pay = (over_time_num * OT_RATE * hour_rate) + hour_rate * REGULAR_HOURS
    print(f"{user_name}, you have worked {hours_worked} this week. This includes {over_time_num} overtime hours")
    print(f"Your gross pay is ${over_time_pay:,.2f}")


def rg_pay(user_name, hours_worked, hour_rate):
    reg_pay = (hours_worked * hour_rate)
    print(f"{user_name}, you have worked {hours_worked} this week")
    print(f"Your gross pay is ${reg_pay:,.2f}")


main()
