# Tax Calculator

def main():
    global name
    print(f"Tax Calculator")
    name = input("Enter Your Full Name: ")
    userinput()

# User Input for Dependents and Gross Income
def userinput():
    dependents = eval(input("Enter Number of dependents: "))
    gross_income = eval(input("Enter Gross income: "))
    cal_tax(gross_income, dependents)

# Math equations and print statements
def cal_tax(gross_income, dependents):
    dependents_deduction = dependents * 2000
    taxable_income = (gross_income - 10000) - dependents_deduction
    income_tax = (taxable_income * 20/100)
    print("\n")
    print(f"Hello, {name} ")
    print(f"You have entered {dependents} dependents")
    print(f"You have entered a gross income of: ${gross_income:,.2f}")
    print(f"{name}, your taxable income is:     ${taxable_income:,.2f}")
    print(f"And your income tax is:             ${income_tax:,.2f}")


main()
