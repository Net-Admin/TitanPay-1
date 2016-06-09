#Make a salaried Employee
#Consists of id, first and last name, commission rate, and union dues
#get full name returns last name, first name
from source.accounting.worker import Worker

class SalariedEmployee(Worker):
    def __init__(self, employee_id, first_name, last_name, commission_rate, weekly_dues):
        Worker.__init__(self, first_name, last_name, weekly_dues)
        self.__commission_rate = commission_rate
