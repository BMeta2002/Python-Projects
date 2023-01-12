from employee import Employee


class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_id, shift, pay_rate):
        super().__init__(emp_name, emp_id)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate
