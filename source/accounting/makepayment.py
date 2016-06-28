from source.accounting.hourlyemployee import HourlyEmployee
from source.accounting.salariedemployee import SalariedEmployee

hourlyFile = open('hourly_employees.csv', 'r')
timeCardsFile = open('timecards.csv', 'r')
salariedFile = open('salaried_employees.csv', 'r')
receiptsFile = open('receipts.csv', 'r')


class MakePayment:

    def __init__(self, start_date, end_date):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__dic = {}

    def pay(self):
        hEmployees = self.hourlyEmployeeList()
        sEmployees = self.SalariedEmployeeList()

        self.timeCardsList(hEmployees)
        self.recieptList(sEmployees)
        self.__dic = self.makeDic(hEmployees, sEmployees, self.__start_date, self.__end_date)
        return self.makeThePayment()

    def makeThePayment(self):
        s = ''
        for person in self.__dic:
            s += self.__dic[person] + "\n"
        return s

    def hourlyEmployeeList(self):
        employees = []
        line = hourlyFile.readline()
        line = hourlyFile.readline()
        while line != "":
            employ = line.split(',')
            if employ[4].strip() == '-':
                emp = HourlyEmployee(int(employ[0]), employ[1].strip(), employ[2].strip(), float(employ[3]),
                                     0, employ[5].strip())
            else:
                emp = HourlyEmployee(int(employ[0]), employ[1].strip(), employ[2].strip(), float(employ[3]),
                                 float(employ[4]), employ[5].strip())
            employees.append(emp)
            line = hourlyFile.readline()
        return employees

    def SalariedEmployeeList(self):
        employees = []
        line = salariedFile.readline()
        line = salariedFile.readline()
        while line != "":
            employ = line.split(',')
            if employ[5].strip() == '-':
                emp = SalariedEmployee(int(employ[0]), employ[1].strip(), employ[2].strip(), float(employ[3]),
                                       float(employ[4]), 0, employ[6].strip())
            else:
                emp = SalariedEmployee(int(employ[0]), employ[1].strip(), employ[2].strip(), float(employ[3]),
                                   float(employ[4]), float(employ[5]), employ[6].strip())
            line = salariedFile.readline()
        return employees

    def timeCardsList(self, hEmployees):
        line = timeCardsFile.readline()
        line = timeCardsFile.readline()
        while line != '':
            piece = line.split(',')
            for x in hEmployees:
                if piece[0] == x.getID():
                    x.clockin(piece[3], int(piece[1]))
                    x.clockout(piece[3], int(piece[2]))
            line = timeCardsFile.readline()

    def recieptList(self, sEmployees):
        line = receiptsFile.readline()
        line = receiptsFile.readline()
        while line != '':
            piece = line.split(',')
            for x in sEmployees:
                if piece[0] == x.getID():
                    x.makeSale('6/21/2016', float(piece[5]))
            line = receiptsFile.readline()

    def makeDic(self, hEmployees, sEmployees, start_date, end_date):
        dic = {}
        for x in hEmployees:
            s = x.pay(start_date,end_date)
            dic[x] = s
        for y in sEmployees:
            s = y.pay(start_date, end_date)
            dic[y] = s
        return dic