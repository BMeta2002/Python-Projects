#Software Sales
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))

RETAIL_PRICE = 99


def main():
    user_name = input("Enter Your User Name Here:")
    quantity = eval(input("Enter The Amount Of Packages You Are Buying:"))
    cal_discount(user_name, quantity)


def cal_discount(user_name, quantity):
    if quantity >= 10 and quantity <= 19:
        first_total = RETAIL_PRICE * quantity
        discount_rate = 20/100
        discount_price = first_total * discount_rate
        discount_total = first_total - discount_price

    elif quantity >= 20 and quantity <= 49:
        first_total = RETAIL_PRICE * quantity
        discount_rate = 30/100
        discount_price = first_total * discount_rate
        discount_total = first_total - discount_price

    elif quantity >= 50 and quantity <= 99:
        first_total = RETAIL_PRICE * quantity
        discount_rate = 40/100
        discount_price = first_total * discount_rate
        discount_total = first_total - discount_price

    else:
        first_total = RETAIL_PRICE * quantity
        discount_rate = 50/100
        discount_price = first_total * discount_rate
        discount_total = first_total - discount_price

    display(user_name, quantity,  discount_price, discount_total)


def display(user_name, quantity, discount_price, discount_total):
    print(f"Hello {user_name}, you have purchased {quantity} packages")
    print(f"Your discount is ${discount_price:,.2f}")
    print(f"Your price after the discount is ${discount_total:,.2f}")


main()
