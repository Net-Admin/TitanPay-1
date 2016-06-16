from source.accounting.address import Address
from source.accounting.employee import Employee
class PaymentMethod:
    def __init__(self, value, person, homeAddress):
        self.__value = value
        self.__person = person
        self.__homeAddress = homeAddress

    def pay(self, value):
        value.pay(value)