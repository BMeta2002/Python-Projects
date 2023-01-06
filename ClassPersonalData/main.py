import person
import time
import os

print("Programmer: " + os.getlogin())
print("Lab 15.4 " + time.strftime("%b %d, %Y @ %I:%M\n"))


def main():
    person1 = person.Person("Bilal Malik", "85 Broad Street", 22, "555-555-1281")
    person2 = person.Person("Keith Jones", "86 Broad Street", 30, "555-523-1284")
    person3 = person.Person("Cynthia Smith", "87 Broad Street", 25, "555-555-1565")

    print("My information: ")
    print('Name: ', person1.get_name())
    print('Address ', person1.get_address())
    print('Age: ', person1.get_age())
    print('Phone Number: ', person1.get_number())

    print("\nFriend 1's Information: ")
    print('Name: ', person2.get_name())
    print('Address ', person2.get_address())
    print('Age: ', person2.get_age())
    print('Phone Number: ', person2.get_number())

    print("\nFriend 2's Information: ")
    print('Name: ', person3.get_name())
    print('Address ', person3.get_address())
    print('Age: ', person3.get_age())
    print('Phone Number: ', person3.get_number())


if __name__ == '__main__':
    main()
