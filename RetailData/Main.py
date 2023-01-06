import time
import os
import retailitems


print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    # Instances of the retail items class
    item1 = retailitems.RetailItems("Jacket", 12, 59.95)
    item2 = retailitems.RetailItems("Designer Jeans", 40, 34.95)
    item3 = retailitems.RetailItems("Shirt", 20, 24.95)

    # Display Results using magic method
    print(f"Retail Item 1:\n"
          f"{item1.__str__()}")
    print(f"Retail Item 2:\n"
          f"{item2.__str__()}")
    print(f"Retail Item 3:\n"
          f"{item3.__str__()}")


if __name__ == '__main__':
    main()
