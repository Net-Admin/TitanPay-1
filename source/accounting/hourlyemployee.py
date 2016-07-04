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
        newDate = date
        newCard = TimeCard(newDate, time, 0)
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
            if int(endDate[0]) >= int(x.getDate()[0]) >= int(startDate[0]):
                if int(endDate[1]) >= int(x.getDate()[1]) >= int(startDate[1]):
                    if int(endDate[2]) >= int(x.getDate()[2]) >= int(startDate[2]):
                        val += x.calculate_daily_pay(self.__hourly_rate)
        method = self.setMethod()
        val = val - self.getDues()
        if val > 0:
            return method.pay(val)
        else:
            return method.notpaid()