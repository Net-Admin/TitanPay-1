#Make a time card for the employee
#Consists of date, start time and end time
#calculate daily pay returns the time * rate * 1.5 only if over 8 hours worked
class TimeCard:
    def __init__(self, date, start_time, end_time):
        self.__date = date.split('/')
        self.__start_time = start_time
        self.__end_time = end_time

    def setDate(self, date):
        self.__date = date

    def setStart(self, start_time):
        self.__start_time = start_time

    def setEnd(self, end_time):
        self.__end_time = end_time

    def getDate(self):
        return self.__date

    def calculate_daily_pay(self, rate):
        time = self.__end_time - self.__start_time
        if time > 8:
            return time * rate * 1.5
        else:
            return time * rate
