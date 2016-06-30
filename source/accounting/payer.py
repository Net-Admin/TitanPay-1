from source.accounting.hourlyemployee import HourlyEmployee
from source.accounting.salariedemployee import SalariedEmployee

def makeHourlyEmployees():
    hourlyFile = open('hourly_employees.csv', 'r')
    employees = []
    line = hourlyFile.readline()
    line = hourlyFile.readline()
    while line != "":
        employ = line.split(',')
        if '-' in employ[4]:
            emp = HourlyEmployee(int(employ[0]), employ[2].rstrip(' '), employ[1].rstrip(' '), float(employ[3]),
                                 0, employ[5].rstrip(' '))
        else:
            emp = HourlyEmployee(int(employ[0]), employ[2].rstrip(' '), employ[1].rstrip(' '), float(employ[3]),
                                 float(employ[4]), employ[5].rstrip(' '))

        employees.append(emp)
        line = hourlyFile.readline()
    hourlyFile.close()
    return employees

def makeSalariedEmployees():
    salariedFile = open('salaried_employees.csv', 'r')
    line = salariedFile.readline()
    line = salariedFile.readline()
    employees = []
    while line != "":
        employ = line.split(',')
        if '-' in employ[5]:
            emp = SalariedEmployee(int(employ[0]), employ[2].rstrip(' '), employ[1].rstrip(' '), float(employ[3]),
                                   float(employ[4]), 0, employ[6].rstrip(' '))
        else:
            emp = SalariedEmployee(int(employ[0]), employ[2].rstrip(' '), employ[1].rstrip(' '), float(employ[3]),
                                   float(employ[4]), float(employ[5]), employ[6].rstrip(' '))
        line = salariedFile.readline()
        employees.append(emp)
    salariedFile.close()
    return employees

def giveTimes():
    hEmployees = makeHourlyEmployees()
    timeCardsFile = open('timecards.csv', 'r')
    line = timeCardsFile.readline()
    line = timeCardsFile.readline()
    while line != '':
        piece = line.split(',')
        for x in hEmployees:
            if int(piece[0]) == x.getID():
                x.clockIn(piece[3], int(piece[1]))
                x.clockOut(piece[3], int(piece[2]))
        line = timeCardsFile.readline()
    timeCardsFile.close()
    return hEmployees

def makeReceipts():
    sEmployees=makeSalariedEmployees()
    receiptsFile = open('receipts.csv', 'r')
    line = receiptsFile.readline()
    line = receiptsFile.readline()
    while line != '':
        piece = line.split(',')
        for x in sEmployees:
            if int(piece[0]) == x.getID():
                x.makeSale('6/21/2016', float(piece[5].strip()))
        line = receiptsFile.readline()
    return sEmployees

def dictionaryMaker(start_date, end_date):
    hEmployees = giveTimes()
    sEmployees = makeReceipts()
    dic = {}
    s = ''
    for x in hEmployees:
        try:
            dic[x] = x.pay(start_date, end_date)
        except ValueError:
            "Do Nothing"

    for x in sEmployees:
        try:
            dic[x] = x.pay(start_date, end_date)
        except ValueError:
            "Do Nothing"
    for person in dic:
        try:
            s += dic[person] + "\n"
        except TypeError:
            "Do Nothing"
    return s