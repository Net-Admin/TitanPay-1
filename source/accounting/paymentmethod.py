from source.accounting.address import Address
class PaymentMethod:
    def __init__(self, value, last_name, first_name, homeAddress):
        self.__value = value
        self.__first_name = first_name
        self.__last_name = last_name
        self.__homeAddress = homeAddress

    def setValue(self, value):
        self.__value = value

    def getFirst(self):
        return self.__first_name

    def getLast(self):
        return self.__last_name

    def getAdd(self):
        return self.__homeAddress.get_address()

    def pay(self, value):
        value.pay(value)

    def notpaid(self):
        s = self.__first_name + " " + self.__last_name + " is not paid this week."
        return s