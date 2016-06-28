from source.accounting.paymentmethod import PaymentMethod
class DirectDepositPayment(PaymentMethod):
    def __init__(self, val, first_name, last_name, homeAddress):
        PaymentMethod.__init__(self, val, first_name, last_name, homeAddress)
    def pay(self, val):
        s = '$' + format(val, ',.2f') + 'is being directly deposited in ' + self.getFirst() + ' ' + self.getLast() + "'s account."
        return s