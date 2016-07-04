import sqlite3

class EmpBase:
    def __init__(self):
        pass

    def import_h_emp(self):
        sqlite_file = 'employeeDatabase.sqlite'
        id_column = 'Employee_ID'

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        hourlyFile = open('hourly_employees.csv', 'r')
        line = hourlyFile.readline()
        line = hourlyFile.readline()

        while line != "":
            employ = line.split(',')
            id = int(employ[0])
            last = employ[1]
            first = employ[2]
            hourly = employ[3]
            union = employ[4]
            method = employ[5]
            if '-' in employ[4]:
                try:
                    params = (id, last, first, hourly, 0, method)
                    c.execute("INSERT INTO Hourly_Employees VALUES (?, ?, ?, ?, ?, ?)", params)
                except sqlite3.IntegrityError:
                    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
            else:
                try:
                    params = (id, last, first, hourly, union, method)
                    c.execute("INSERT INTO Hourly_Employees VALUES (?, ?, ?, ?, ?, ?)", params)
                except sqlite3.IntegrityError:
                    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
            line= hourlyFile.readline()
        conn.commit()
        conn.close()
        hourlyFile.close()

    def import_s_emp(self):
        sqlite_file = 'employeeDatabase.sqlite'
        id_column = 'Employee_ID'

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        hourlyFile = open('salaried_employees.csv', 'r')
        line = hourlyFile.readline()
        line = hourlyFile.readline()
        while line != "":
            employ = line.split(',')
            id = int(employ[0])
            last = employ[2]
            first = employ[1]
            salary = employ[3]
            comm = employ[4]
            union = employ[5]
            method = employ[6]

            if '-' in employ[5]:
                try:
                    params = (id, last, first, salary, comm, 0, method)
                    c.execute("INSERT INTO Salaried_Employees VALUES (?, ?, ?, ?, ?, ?, ?)", params)
                except sqlite3.IntegrityError:
                    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
            else:
                try:
                    params = (id, last, first, salary, comm, union, method)
                    c.execute("INSERT INTO Salaried_Employees VALUES (?, ?, ?, ?, ?, ?, ?)", params)
                except sqlite3.IntegrityError:
                    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
            line = hourlyFile.readline()
        hourlyFile.close()
        conn.commit()
        conn.close()

    def import_time_cards(self):
        timeCardsFile = open('timecards.csv', 'r')

        sqlite_file = 'employeeDatabase.sqlite'

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        line = timeCardsFile.readline()
        line = timeCardsFile.readline()
        while line != '':
            piece = line.split(',')
            id = piece[0]
            c_in = piece[1]
            c_out = piece[2]
            date = piece[3]

            try:
                params = (id, c_in, c_out, date)
                c.execute("INSERT INTO Time_Cards VALUES (?, ?, ?, ?)", params)
            except sqlite3.IntegrityError:
                print('ERROR: Time Card Error')
            line = timeCardsFile.readline()
        timeCardsFile.close()
        conn.commit()
        conn.close()

    def import_receipt(self):
        receiptsFile = open('receipts.csv', 'r')

        sqlite_file = 'employeeDatabase.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        line = receiptsFile.readline()
        line = receiptsFile.readline()
        while line != '':
            piece = line.split(',')
            id = piece[0]
            amount = piece[5]
            try:
                params = (id, amount, '6/21/2016')
                c.execute("INSERT INTO Receipts VALUES (?, ?, ?)", params)
            except sqlite3.IntegrityError:
                print('ERROR: Receipt Error')
            line = receiptsFile.readline()
        receiptsFile.close()
        conn.commit()
        conn.close()