
class Person:
    def __init__(self, name, address, age, number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
    
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        self.__number = number
        
    