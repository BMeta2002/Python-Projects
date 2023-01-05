# Creating & Adding To Text File
import datetime

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter your name: ")
    name_1 = input("Enter Name One: ")
    name_2 = input("Enter Name Two: ")
    name_3 = input("Enter Name Three: ")
    create_file(name, name_1, name_2, name_3)


def create_file(name, name_1, name_2, name_3):
    c_list = open("List.txt", "w")
    c_list.write(name_1)
    c_list.write('')
    c_list.write(",")
    c_list.write('')
    c_list.write(name_2)
    c_list.write('')
    c_list.write(",")
    c_list.write('')
    c_list.write(name_3)
    c_list.close()
    print(f"{name}, Here are the names entered: {name_1}, {name_2}, {name_3}")
    update_file(name, name_1, name_2, name_3, c_list)


def update_file(name, name_1, name_2, name_3, c_list):
    option = eval(input("Enter 1 to enter additional names or 0 to quit: "))
    if option == 1:
        name_4 = input("Enter Name Four: ")
        name_5 = input("Enter Name Five: ")
        c_list = open("List.txt", "a")
        c_list.write('')
        c_list.write(",")
        c_list.write('')
        c_list.write(name_4)
        c_list.write('')
        c_list.write(",")
        c_list.write('')
        c_list.write(name_5)
        print(f"{name}, This are the updated list: {name_1}, {name_2}, {name_3}, {name_4}, {name_5}")
    elif option == 0:
        print(f"{name}, This is the original list: {name_1}, {name_2}, {name_3}")
        c_list.close()


main()
