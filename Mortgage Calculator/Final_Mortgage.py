import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Creates the main window
window = Tk()

window.geometry("320x320")
window.title("Mortgage Calculator")
window.config(background="Aqua")

# Create the input fields for the loan amount, interest rate, and loan period
loan_amount_label = Label(window,
                          text="Loan Amount:",
                          font=("Arial", 12, "bold"),
                          fg="#000000",
                          bg="wheat",
                          pady="10")
loan_amount_label.grid(column=0, row=0)
loan_amount_entry = tkinter.Entry()
loan_amount_entry = tkinter.Spinbox(window,
                                    from_=10000,
                                    to=9999999999999999,
                                    increment=15000)
loan_amount_entry.grid(column=1, row=0)

# Interest Rate
interest_rate_label = tkinter.Label(window,
                                    text="Interest Rate (%):",
                                    font=("Arial", 12, "bold"),
                                    fg="#000000",
                                    bg="wheat",
                                    pady="10")
interest_rate_label.grid(column=0, row=1)
interest_rate_entry = tkinter.Entry()
interest_rate_entry = tkinter.Spinbox(window,
                                      from_=1,
                                      to=30,
                                      increment=1)
interest_rate_entry.grid(column=1, row=1)

# Loan Period
loan_period_label = tkinter.Label(window,
                                  text="Loan Period (years):",
                                  font=("Arial", 12, "bold"),
                                  fg="#000000",
                                  bg="wheat",
                                  pady="10")
loan_period_label.grid(column=0, row=2)
loan_period_entry = tkinter.Entry()
loan_period_entry = tkinter.Spinbox(window,
                                    from_=5,
                                    to=50,
                                    increment=1)
loan_period_entry.grid(column=1, row=2)

# Down Payment
Down_Payment_label = tkinter.Label(window,
                                   text="Down Payment:",
                                   font=("Arial", 12, "bold"),
                                   fg="#000000",
                                   bg="wheat",
                                   pady="10")
Down_Payment_label.grid(column=0, row=3)
Down_Payment_entry = tkinter.Entry()
Down_Payment_entry = tkinter.Spinbox(window,
                                     from_=5000,
                                     to=9999999999999999,
                                     increment=10000)
Down_Payment_entry.grid(column=1, row=3)

# Picture
window.iconbitmap('bank.ico')


# Create the button to calculate the monthly payment
def calc():
    # Getting the user entered info
    loan_amount = eval(loan_amount_entry.get())
    interest_rate = eval(interest_rate_entry.get())
    loan_period = eval(loan_period_entry.get())
    down_payment = eval(Down_Payment_entry.get())

    # Calculate the monthly payment
    total_price = loan_amount - down_payment
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_period * 12
    monthly_payment = total_price * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

    # Display the monthly payment on same window
    '''
    monthly_payment_label = tkinter.Label(window,
                                          text=f"Monthly Payment: ${monthly_payment:.2f}",
                                          font=("Arial", 12, "bold"),
                                          fg="#FFFFFF",
                                          bg="black")
    monthly_payment_label.grid(column=0, row=5)
    '''

    # Display the monthly payment on new window
    messagebox.showinfo(title="Your Results Are Shown Here",
                        message=f"Monthly Payment: ${monthly_payment:.2f}", )


calc_button = tkinter.Button(window,
                             text="Calculate Monthly Payment",
                             command=calc,
                             fg="wheat",
                             bg="black"
                             )

calc_button.grid(column=1, row=6)

# Start the main event loop
window.mainloop()
