#Make an Employee
#Consists of id, first and last name, hourly rate, and union dues
#get full name returns last name, first name

from source.accounting.employee import Employee
from source.accounting.timecard import TimeCard
from source.accounting.paymentmethod import PaymentMethod

class HourlyEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, payMethod):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payMethod)
        self.__hourly_rate = hourly_rate
        self.__timeCards = []

    def clockIn(self, date, time):
        newCard = TimeCard()
        newCard.setDate(date)
        newCard.setStart(time)
        self.__timeCards.append(newCard)

    def clockOut(self, date, time):
        for x in self.__timeCards:
            if x.getDate() == date:
                x.setEnd(time)

    def pay(self, startDate, endDate):
        val = 0
        for x in self.__timeCards:
            if (x.getDate() >= startDate and x.getDate() <= endDate):
                val += x.calculate_daily_pay(self.__hourly_rate)
        self.__payMethod.pay(val)