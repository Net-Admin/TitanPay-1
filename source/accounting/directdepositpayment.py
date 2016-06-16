class DirectDepositPayment:
    def pay(self, val):
        print('$', format(val, ',.2f'), 'is being directly deposited in ', self.__person.get_first_name(), ' ', self.__person.get_last_name(),
                  "'s account.", sep = '')
