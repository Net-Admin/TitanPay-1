from source.accounting.paymentmethod import PaymentMethod
class PickUpPayment(PaymentMethod):
    def __init__(self, val, first_name, last_name, homeAddress):
        PaymentMethod.__init__(self, val, first_name, last_name, homeAddress)
    def pay(self, val):
        s = 'A check for $' + format(val, ',.2f') + ' is waiting for ' + self.getFirst() + ' ' + self.getLast() + ' at the PostMaster.'
        return s