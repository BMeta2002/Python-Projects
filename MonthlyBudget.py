# Monthly Budget
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter Your Name:  ")
    monthly_budget = eval(input(f"{name}, Enter Your Monthly Budget: "))
    spent_total = 0
    x = 1
    while x != 0:
        spent = eval(input("Enter The Amount Spent (type 0 quit): "))
        spent_total = spent_total + spent
        budget_under = monthly_budget - spent_total
        budget_over = spent_total - monthly_budget
        x = spent
    show_spending(name, monthly_budget, spent_total, budget_under, budget_over)


def show_spending(name, monthly_budget, spent_total, budget_under, budget_over):
    print(f"Budgeted: ${monthly_budget:,.2f}")
    print(f"Spent: ${spent_total:,.2f}")
    if spent_total == monthly_budget:
        print(f"Spending matches budget. GOOD PLANNING!, {name} ")
    elif spent_total < monthly_budget:
        print(f"You are ${budget_under:,.2f} under budget. WELL DONE! {name} ")
    else:
        print(f"You are ${budget_over:,.2f} over budget. PLAN BETTER NEXT TIME! {name} ")


main()
