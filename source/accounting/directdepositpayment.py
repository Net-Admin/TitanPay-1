class DirectDepositPayment:
    def pay(self, val):
        print('$', format(val, ',.2f'), 'is being directly deposited in ', self.__first_name, ' ', self.__last_name,
                  "'s account.", sep = '')
