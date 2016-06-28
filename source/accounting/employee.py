from source.accounting.directdepositpayment import DirectDepositPayment
from source.accounting.pickuppayment import PickUpPayment
from source.accounting.mailpayment import MailPayment
from source.accounting.address import Address

class Employee:
    def __init__(self, employee_id, first_name, last_name, weekly_dues, payMethod):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues
        self.__paymentMethod = payMethod

    def get_full_name(self):
        s = self.__last_name + ', ' + self.__first_name
        return s

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def setMethod(self):
        if self.__paymentMethod == 'DD':
            method = DirectDepositPayment(0, self.__first_name, self.__last_name,
                                          Address('6605 Fifth Ave. N', 'St. Petersburg', 'Florida', '33710'))
        elif self.__paymentMethod == 'PU':
            method = PickUpPayment(0, self.__first_name, self.__last_name,
                                   Address('6605 Fifth Ave. N', 'St. Petersburg', 'Florida', '33710'))
        else:
            method = MailPayment(0, self.__first_name, self.__last_name,
                                 Address('6605 Fifth Ave. N', 'St. Petersburg', 'Florida', '33710'))
        return method

    def getDues(self):
        return self.__weekly_dues

    def getMethod(self):
        return self.__paymentMethod

    def getID(self):
        return self.__employee_id