# Calculating loan payment in python
# User Input
def userinput():
    global name
    name = input("Enter Name:")
    interest_rate = float(input("Enter The Interest Rate:"))
    price = float(input("Enter The Full Price Of The Home:"))
    down_payment = float(input("Enter the DownPayment Amount:"))
    term = float(input("Enter The Term Of Loan:"))
    equations()


# Equations
def equations():
    rate = interest_rate / 100
    loan_amount = price - down_payment
    monthly_rate = rate / 12
    monthly_term = term * 12
    payment = (monthly_rate * loan_amount) / (1 - (1 + monthly_rate) ** -monthly_term)
    monthly_payment()

def monthly_payment():
    print(f"Hello,                       {main.name}")
    print(f"The annual interest rate is: {interest_rate}")
    print(f"The price of the house is:  ${price:,.2f}")
    print(f"The down payment is:        ${down_payment:,.2f}")
    print(f"The loan amount is:         ${loan_amount:,.2f}")
    print(f"The monthly payment is:     ${payment:,.2f}")


# Output
main()
