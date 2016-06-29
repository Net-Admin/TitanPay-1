from source.accounting.hourlyemployee import HourlyEmployee
from source.accounting.salariedemployee import SalariedEmployee

def makeHourlyEmployees():
    hourlyFile = open('hourly_employees.csv', 'r')
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
    hourlyFile.close()
    return employees

def makeSalariedEmployees():
    salariedFile = open('salaried_employees.csv', 'r')
    line = salariedFile.readline()
    line = salariedFile.readline()
    employees = []
    while line != "":
        employ = line.split(',')
        if employ[5].strip() == '-':
            emp = SalariedEmployee(int(employ[0]), employ[1].strip(), employ[2].strip(), float(employ[3]),
                                   float(employ[4]), 0, employ[6].strip())
        else:
            emp = SalariedEmployee(int(employ[0]), employ[1].strip(), employ[2].strip(), float(employ[3]),
                                   float(employ[4]), float(employ[5]), employ[6].strip())
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
            if piece[0] == x.getID():
                x.clockin(piece[3], int(piece[1]))
                x.clockout(piece[3], int(piece[2]))
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
            if piece[0] == x.getID():
                x.makeSale('6/21/2016', float(piece[5]))
        line = receiptsFile.readline()
    return sEmployees

def dictionaryMaker(start_date, end_date):
    hEmployees = giveTimes()
    sEmployees = makeReceipts()
    dic = {}
    s = ''
    for x in hEmployees:
        if len(x.getList()) > 0:
            dic[x] = x.pay(start_date, end_date)
    for x in sEmployees:
        if len(x.getList()) > 0:
            dic[x] = x.pay(start_date, end_date)
    for person in dic:
        s += dic[person] + "\n"
    return s