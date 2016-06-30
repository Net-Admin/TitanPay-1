#Make a receipt
#Consists of date and amount
class Receipt:
    def __init__(self, date, sale_amount):
        self.__date = date
        self.__sale_amount = sale_amount

    def getAmount(self):
        return self.__sale_amount

    def getDate(self):
        return self.__date