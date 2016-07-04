import sqlite3

def create():
    sqlite_file = 'employeeDatabase.sqlite'
    table_name1 = 'Hourly_Employees'
    table_name2 = 'Salaried_Employees'
    new_field = 'Employee_ID'
    field_type = 'TEXT'
    field_1 = 'Last_Name'
    field_1_type = 'TEXT'
    field_2 = 'First_Name'
    field_2_type = 'TEXT'
    field_3 = 'Hourly_Rate'
    field_3_2 = 'Salaried_Rate'
    field_3_type = 'TEXT'
    field_4_1 = 'Commission_Rate'
    field_4 = 'Union_Dues'
    field_4_type = 'TEXT'
    field_5 = 'Payment_Method'
    field_5_type = 'TEXT'

    table_name3 = 'Time_Cards'
    time_field_1 = 'Clock_In'
    time_type_1_2 = 'INTEGER'
    time_field_2 = 'Clock_Out'
    time_field_3 = 'Date'

    table_name4 = 'Receipts'
    receipt_1 = 'Total'

    con = sqlite3.connect(sqlite_file)
    c = con.cursor()

    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name1, nf=new_field, ft=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name1, cn=field_1, ct=field_1_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name1, cn=field_2, ct=field_2_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name1, cn=field_3, ct=field_3_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name1, cn=field_4, ct=field_4_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name1, cn=field_5, ct=field_5_type))

    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name2, nf=new_field, ft=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=field_1, ct=field_1_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=field_2, ct=field_2_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=field_3_2, ct=field_3_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=field_4_1, ct=field_3_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=field_4, ct=field_4_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=field_5, ct=field_5_type))

    c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name3, nf=new_field, ft=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name3, cn=time_field_1, ct=time_type_1_2))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name3, cn=time_field_2, ct=time_type_1_2))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name3, cn=time_field_3, ct=field_5_type))

    c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name4, nf=new_field, ft=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name4, cn=receipt_1, ct=field_4_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name4, cn=time_field_3, ct=field_5_type))

    con.commit()

    con.close()

create()