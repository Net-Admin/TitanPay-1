#define address
#address consists of street_address, city, state and zipcode
#needs to return address as string
class Address:
    def __init__(self, street_address, city, state, zipcode):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
    
    def get_address(self):
        s = self.__street_address + ' ' + self.__city + ', ' + self.__state + ' ' + self.__zipcode
        return s
