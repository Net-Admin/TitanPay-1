from source.accounting.paymentmethod import PaymentMethod
class PickUpPayment(PaymentMethod):
    def pay(self, val):
        print('A check for $', format(val, ',.2f'), ' is waiting for ', self.__person.get_first_name(), ' ', self.__person.get_last_name(),
        ' at the PostMaster.', sep = '')