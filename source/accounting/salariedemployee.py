#Make a salaried Employee
#Consists of id, first and last name, commission rate, and union dues
#get full name returns last name, first name
from source.accounting.employee import Employee
from source.accounting.receipt import Receipt
from source.accounting.paymentmethod import PaymentMethod

class SalariedEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, commission_rate, weekly_dues, method, home):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, method, home)
        self.__commission_rate = commission_rate
        self.__receiptList = []

    def makeSale(self, date, amount):
        self.__receiptlist.append(Receipt(date, amount))

    def pay(self):
        val = 0
        for x in self.__receiptList:
            val += x.getAmount()
        payment = self.__commission_rate * val
        PaymentMethod.pay(payment, self.__method)
