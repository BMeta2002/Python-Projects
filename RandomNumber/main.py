# Creating & Adding To Text File
import datetime
import random

date = datetime.datetime.now()
print(date.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    name = input("Enter Your Name: ")
    name_file = input("What would you like the name of this file to be: ")
    count_num = eval(input("How many new numbers will you like to be written in this file: "))
    create_file(name, name_file, count_num)


def create_file(name, name_file, count_num):
    name_file = name_file.replace(" ", " ")
    file = open(f"{name_file}.txt", "w")
    for num in range(count_num):
        num = random.randint(1, 100)
        file.write(str(num) + '\n')
    file.close()
    read_file(name, name_file, count_num)


def read_file(name, name_file, count_num):
    total = 0
    print(f"{name.title()}, how are the random numbers to be written to {name_file}.txt: \n")
    file = open(f"{name_file}.txt", "r")
    for num in range(count_num):
        line = file.readline()
        line = line.rstrip("\n")
        print(f"\t{line}")
        total += int(line)
    print(f"{count_num}, numbers were read from the file \n")
    print(f"The total of the numbers read is: {total}. ")


main()
