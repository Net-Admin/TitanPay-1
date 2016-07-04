from source.accounting.hourlyemployee import HourlyEmployee
from source.accounting.salariedemployee import SalariedEmployee
import sqlite3

def makeHourlyEmployees():
    sqlite_file = 'employeeDatabase.sqlite'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    employees = []

    for x in range(100):
        c.execute('SELECT * FROM Hourly_Employees WHERE Employee_ID=(?)', [x])
        employ = c.fetchall()
        try:
            employ = list(employ[0])
        except IndexError:
            pass
        try:
            if '-' in employ:
                method = str(employ[5]).rstrip(' ')
                method = method.rstrip('\n')
                emp = HourlyEmployee(int(employ[0]), str(employ[2]).rstrip(' '), str(employ[1]).rstrip(' '), float(employ[3]),
                                 0, method)
            else:
                method = str(employ[5]).rstrip(' ')
                method = method.rstrip('\n')
                emp = HourlyEmployee(int(employ[0]), str(employ[2]).rstrip(' '), str(employ[1]).rstrip(' '), float(employ[3]),
                                 float(employ[4]), method)

            employees.append(emp)
        except IndexError:
            pass
    return employees

def makeSalariedEmployees():
    sqlite_file = 'employeeDatabase.sqlite'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    employees = []

    for x in range(100):
        c.execute('SELECT * FROM Salaried_Employees WHERE Employee_ID=(?)', [x])
        employ = c.fetchall()
        try:
            employ = list(employ[0])
        except IndexError:
            pass
        try:
            if '-' in employ:
                method = str(employ[6]).rstrip(' ')
                method = method.rstrip('\n')
                salary = float(employ[3])
                salary /= 12
                emp = SalariedEmployee(int(employ[0]), str(employ[2]).rstrip(' '), str(employ[1]).rstrip(' '), salary,
                                     float(employ[4]) ,0, method)
            else:
                method = str(employ[6]).rstrip(' ')
                method = method.rstrip('\n')
                salary = float(employ[3])
                salary /= 12
                emp = SalariedEmployee(int(employ[0]), str(employ[2]).rstrip(' '), str(employ[1]).rstrip(' '),
                                       salary, float(employ[4]), float(employ[5]), method)
            employees.append(emp)
        except IndexError:
            pass

    return employees

def giveTimes():
    hEmployees = makeHourlyEmployees()
    sqlite_file = 'employeeDatabase.sqlite'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    for x in range (100):
        c.execute('SELECT * FROM Time_Cards WHERE Employee_ID=(?)', [x])
        employ = c.fetchall()
        try:
            piece = list(employ[0])
            for x in hEmployees:
                if int(piece[0]) == x.getID():
                    date = piece[3].rstrip('\n')
                    date = date.split('/')
                    x.clockIn(date, int(piece[1]))
                    x.clockOut(date, int(piece[2]))
        except IndexError:
            pass

    return hEmployees

def makeReceipts():
    sEmployees=makeSalariedEmployees()
    sqlite_file = 'employeeDatabase.sqlite'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    for x in range(100):
        c.execute('SELECT * FROM Receipts WHERE Employee_ID=(?)', [x])
        employ = c.fetchall()
        try:
            piece = list(employ[0])
            for x in sEmployees:
                if int(piece[0]) == x.getID():
                    mon = piece[1].strip('\n')
                    mon = float(mon)
                    x.makeSale('6/21/2016', mon)
        except IndexError:
            pass
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