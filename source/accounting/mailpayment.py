from source.accounting.paymentmethod import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, val, first_name, last_name, homeAddress):
        PaymentMethod.__init__(self, val, last_name, first_name, homeAddress)
    def pay(self, val):
        s = 'Mailing a check to ' + self.getFirst() + " " + self.getLast() + ' for $' + format(val, ',.2f') + ' to ' + self.getAdd()
        return s