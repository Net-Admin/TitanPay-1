from source.accounting.employee import Employee
from source.accounting.receipt import Receipt


class SalariedEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues, paymentMethod):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, paymentMethod)
        self.__commission_rate = commission_rate
        self.__salary = salary
        self.__receiptList = []

    def makeSale(self, date, amount):
        newDate = date.split('/')
        self.__receiptList.append(Receipt(newDate, amount))

    def getList(self):
        return self.__receiptList

    def pay(self, startDate, endDate):
        val = 0
        for x in self.__receiptList:
            if int(endDate[0]) >= int(x.getDate()[0]) >= int(startDate[0]):
                if int(endDate[1]) >= int(x.getDate()[1]) >= int(startDate[1]):
                    if int(endDate[2]) >= int(x.getDate()[2]) >= int(startDate[2]):
                        val += x.getAmount()
        payment = self.__commission_rate * val
        method = self.setMethod()
        payment = payment - self.getDues()
        if payment > 0:
            return method.pay(payment)
        else:
            return ''
