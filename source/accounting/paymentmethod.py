from source.accounting.employee import Employee

class PaymentMethod:
    def __init__(self, person):
        self.__person = person

    def pay(self, person):
        person.pay(person)

class MailPayment:
    def pay(self, person):
        print('Mailing a check to ', self.__person.get_first_name(), " ", self.__person.get_last_name, ' for $', self.__person.pay(), ' to ',
              self.__person.get_home(), sep = '')


class DirectDepositPayment:
    def pay(self, person):
        print('A check for $', person.pay(), ' is waiting for ', person.get_first_name(), ' ', person.get_last_name,
              ' at the PostMaster.', sep = '')


class PickUpPayment:
    def pay(self, person):
        print('$', person.pay(), 'is being directly deposited in ', person.get_first_name(), ' ', person.get_last_name,
                  "'s account.", sep = '')