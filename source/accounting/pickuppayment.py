from source.accounting.paymentmethod import PaymentMethod
class PickUpPayment(PaymentMethod):
    def pay(self, val):
        print('A check for $', format(val, ',.2f'), ' is waiting for ', self.__first_name, ' ', self.__last_name,
        ' at the PostMaster.', sep = '')