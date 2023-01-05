import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M \n"))
print("Programmer: Bilal Malik")


def main():
    sales = []
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    username = input("Enter UserName: ")
    for day in days:
        sales_for_day = float(input(f"Enter sales for {day}: "))
        sales.append(sales_for_day)

    total_sales = sum(sales)
    print(f"{username}, Here are the results: ")
    print(f"Total sales for the week: ${total_sales:,.2f}")

    print("Which day's sales to display: ")
    day = input()

    day_index = days.index(day)
    print(f"Current sales for {day}: ${sales[day_index]:,.2f}")

    print(f"Enter the new sales for day {day}: ")
    new_sales = float(input())

    sales[day_index] = new_sales
    print(sales)
    print(f"Updated total sales for the week: ${sum(sales):,.2f}")


if __name__ == '__main__':
    main()
