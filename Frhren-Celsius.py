# Fahrenheit to Celsius Converter
def intro():
    print("Welcome to the Fahrenheit to Celsius Converter!")
    main()


def main():
    name = input("Enter Your Username Here:")
    print(f"Hello, {name}")
    fahren_first = eval(input("Enter the degrees in Fahrenheit:"))
    convert(fahren_first)


def convert(fmain):
    celsius = (fmain - 32) * 5/9
    celsius = round(celsius, 2)
    print(f"Temperature entered in Fahrenheit is: {fmain}")
    print(f"{fmain} degrees in Fahrenheit is equivalent to {celsius} degrees in Celsius")


intro()