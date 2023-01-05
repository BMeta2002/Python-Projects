# Retail Company monthly sales tax report

def main():
    global name
    print(f"Monthly Sales Tax Report\n")
    name = input("Enter Your Name: ")
    print(f"Hi there, {name}\n")
    userinput()


def userinput():
    total_sales = eval(input("Enter Total Sales For The Month:"))
    print(f"The total sales for the month is ${total_sales:,.2f} for this month. Awesome!\n")
    cal_tax(total_sales)


def cal_tax(total_sales):
    print(f"Press enter to calculate your county, state and total tax.\n")
    county_tax = total_sales * 2/100
    state_tax = total_sales * 4/100
    total_tax = county_tax + state_tax
    print(f"Your county sales tax is:   ${county_tax}")
    print(f"Your state sales tax is:    ${state_tax}")
    print(f"Your county sales tax is:   ${total_tax} \n")
    print(f"Great job this month, {name}. See you next month!")


main()
