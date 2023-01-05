# BookStore Points
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    user_name = input("Enter Your Username: ")
    quantity_books = eval(input("Enter The Amount Of Books You are buying: "))
    cal_points(user_name, quantity_books)


def cal_points(user_name, quantity_books):
    points = 0
    if quantity_books == 0:
        b_points = points + 0

    elif quantity_books == 1:
        b_points = points + 5

    elif quantity_books == 2:
        b_points = points + 15

    elif quantity_books == 3:
        b_points = points + 30
    else:
        b_points = points + 60
    display(user_name, quantity_books, b_points)


def display(user_name, quantity_books, b_points):
    print(f"Hello, {user_name}, you have purchased {quantity_books}.")
    print(f"You have earned {b_points}.")


main()
