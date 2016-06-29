#Make an Employee
#Consists of id, first and last name, hourly rate, and union dues
#get full name returns last name, first name

from source.accounting.employee import Employee
from source.accounting.timecard import TimeCard
from source.accounting.paymentmethod import PaymentMethod

class HourlyEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, paymentMethod):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, paymentMethod)
        self.__hourly_rate = hourly_rate
        self.__timeCards = []

    def clockIn(self, date, time):
        newCard = TimeCard(date, time, 0)
        self.__timeCards.append(newCard)

    def clockOut(self, date, time):
        for x in self.__timeCards:
            if x.getDate() == date:
                x.setEnd(time)

    def getList(self):
        return self.__timeCards

    def pay(self, startDate, endDate):
        val = 0
        for x in self.__timeCards:
            if (x.getDate()[0] >= startDate[0] and x.getDate()[1] >= startDate[1] and x.getDate()[2] >= startDate[2]) and (x.getDate()[0] <= endDate[0] and x.getDate()[1] <= endDate[1] and x.getDate()[2] <= endDate[2]):
                val += x.calculate_daily_pay(self.__hourly_rate)
        method = self.setMethod()
        val = val - self.getDues()
        method.pay(val)
