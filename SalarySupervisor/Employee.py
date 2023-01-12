class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name


    def set_name(self):
        self._name = name


    def get_number(self):
        return self.__number


    def set_number(self):
        self._number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay = pay

    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay


class ShiftSupervisor(Employee):
    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self.__salary = salary
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def set_salary(self):
        self._salary = salary

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self):
        self._bonus = bonus
