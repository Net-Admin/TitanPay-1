from source.accounting.paymentmethod import PaymentMethod

class MailPayment(PaymentMethod):
    def pay(self, val):
        print('Mailing a check to ', self.__person.get_first_name(), " ", self.__person.get_last_name(), ' for $', format(val, ',.2f'), ' to ',
              self.homeAddress.get_address(), sep='')