class Employee:
    def __init__(self, emp_name, emp_id):
        self.__emp_name = emp_name
        self.__emp_id = emp_id

    def set_name(self, emp_name):
        self.__emp_name = emp_name

    def set_id(self, emp_id):
        self.__emp_id = emp_id

    def get_name(self):
        return self.__emp_name

    def get_id(self):
        return self.__emp_id
