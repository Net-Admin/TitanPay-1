#Make an Employee
#Consists of id, first and last name, hourly rate, and union dues
#get full name returns last name, first name

from source.accounting.employee import Employee
from source.accounting.timecard import TimeCard
from source.accounting.paymentmethod import PaymentMethod

class HourlyEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, method, home):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, method, home)
        self.__hourly_rate = hourly_rate
        self.__card = []

    def clockin(self, date, time):
        newCard = TimeCard
        newCard.setDate(date)
        newCard.setStart(time)
        self.__card.append(newCard)

    def clockout(self, date, time):
        for x in self.__card:
            if x.getDate() == date:
                x.setEnd(time)
                break

    def pay(self):
        val = 0
        for x in self.__card:
            val = x.calculate_daily_pay(self.__hourly_rate)
        PaymentMethod.pay(val, self.__method)