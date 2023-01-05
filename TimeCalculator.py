import datetime

timee = datetime.datetime.now()
print(timee.strftime('%B %d, %Y @ %I:%M\n'))


def main():
    user_name = input("Enter Your Username Here: ")
    print(f"Hello {user_name}")
    number_seconds = eval(input("Enter The Number Of Seconds: "))
    cal_time(number_seconds)


def cal_time(number_seconds):
    minutes = number_seconds / 60
    hours = minutes / 60
    days = hours / 24
    t_remainder = number_seconds % 60
    display_time(number_seconds, minutes, hours, days, t_remainder)


def display_time(number_seconds, minutes, hours, days, t_remainder):
    if 60 <= number_seconds < 3600:
        print(f"{number_seconds} is equal to: ")
        print(f"{minutes:,.0f} full minute(s) and {t_remainder} seconds")

    elif 3600 <= number_seconds < 86400:
        print(f"{number_seconds} is equal to: ")
        print(f"{minutes:,.0f} full minute(s) and {t_remainder} seconds")
        print(f"{hours:,.0f} full hours(s) and {t_remainder} seconds")
    else:
        print(f"{number_seconds} is equal to: ")
        print(f"{minutes:,.0f} full minute(s) and {t_remainder} seconds")
        print(f"{hours:,.0f} full hours(s) and {t_remainder} seconds")
        print(f"{days:,.0f} full day(s) and {t_remainder} seconds")


main()
