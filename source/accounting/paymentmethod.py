from source.accounting.address import Address

class PaymentMethod:
    def __init__(self, value, first_name, last_name, homeAddress):
        self.__value = value
        self.__first_name = first_name
        self.__last_name = last_name
        self.__homeAddress = homeAddress

    def pay(self, value):
        value.pay(value)