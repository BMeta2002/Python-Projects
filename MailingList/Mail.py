class Person:
    def __init__(self, name, address, tele):
        self.__name = name
        self.__address = address
        self.__tele = tele

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address

    def get_tele(self):
        return self.__tele
    def set_tele(self, tele):
        self.__tele = tele

class Customer(Person):
    def __init__(self, name, address, tele, num, yn):
        super().__init__(name, address, tele)
        self.__num = num
        self.__yn = yn

    def get_num(self):
        return self.__num
    def set_num(self, num):
        self.__num = num

    def get_yn(self):
        if self.__yn == "yes":
            return True
        else:
            return False
    def set_yn(self, yn):
        self.__yn = yn