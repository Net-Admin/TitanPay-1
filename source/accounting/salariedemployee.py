#Make a salaried Employee
#Consists of id, first and last name, commission rate, and union dues
#get full name returns last name, first name
from source.accounting.employee import Employee
from source.accounting.receipt import Receipt
from source.accounting.paymentmethod import PaymentMethod

class SalariedEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues, paymentMethod):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, paymentMethod)
        self.__commission_rate = commission_rate
        self.__salary = salary
        self.__receiptList = []

    def makeSale(self, date, amount):
        self.__receiptList.append(Receipt(date, amount))

    def getList(self):
        return self.__receiptList

    def pay(self, startDate, endDate):
        startDate = startDate.split('/')
        endDate = endDate.split('/')
        val = 0
        for x in self.__receiptList:
            if (x.getDate()[0] >= startDate[0] and x.getDate()[1] >= startDate[1] and x.getDate()[2] >= startDate[
                2]) and (x.getDate()[0] <= endDate[0] and x.getDate()[1] <= endDate[1] and x.getDate()[2] <= endDate[2]):
                val += x.getAmount()
        payment = self.__commission_rate * val
        method = self.setMethod()
        payment = payment - self.getDues()
        method.pay(payment)