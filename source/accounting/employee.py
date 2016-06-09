#Make an Employee
#Consists of id, first and last name, hourly rate, and union dues
#get full name returns last name, first name

from source.accounting.worker import Worker

class Employee(Worker):
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        Worker.__init__(self, first_name, last_name, weekly_dues)
        self.__hourly_rate = hourly_rate
