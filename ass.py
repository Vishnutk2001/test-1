import sqlite3 as sql
from prettytable import PrettyTable
connection = sql.connect("Employeemanagement.db")
x=connection.execute("select name from sqlite_master where type = 'table' and name = 'employee'").fetchall()

if x != []:
    print("table already created")

else:
    connection.execute('''create table employee(
                           ID integer primary key autoincrement,
                           empCode integer,
                           name text,
                           phone integer,
                           email text,
                           designation text,
                           salary integer,
                           company text
);''')
    print("table created successfully")

while True:
    print("1.add the employees")
    print("2.view all employees")
    print("3.search employee using employee name")
    print("4.update employee details using employee code")
    print("5.delete employee using employee code")
    print("6.display all details of employee whose salary > 50000")
    print("7.display total count of employees in company")
    print("8.display employee details in alphabatical order with specific range salary")
    print("9.display employee data whose salary < average salary of all employee")
    print("10. exit")
    choice = int(input("enter the choice"))
    if choice == 1:
        getempcode = input("enter Code :")
        getname = input("enter Name :")
        getphone = input("enter num :")
        getemail = input("enter email :")
        getdesignation = input("enter designation :")
        getsalary = input("enter Salary :")
        getcompany = input("enter Company Name :")

        connection.execute("insert into employee(empCode,name,phone,email,designation,salary,company)\
                                   values(" + getempcode + ",'" + getname + "','" + getphone + "','" + getemail + "','" + getdesignation + "'," + getsalary + ",'" + getcompany + "')")
        print("Inserted Successfully.")
        connection.commit()
    elif choice==2:
           result = connection.execute("select * from employee")
           table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
           for i in result:
             table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
           print(table)

    elif choice == 3:
           getname = input("Search Employee by Employee Name :")
           result = connection.execute("select * from employee where name like '%" + getname + "%'")
           table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
           for i in result:
              table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
           print(table)

    elif choice == 4:
           getempcode = input("Update Employee using Employee Code :")

           getname = input("enter employee Name :")
           getphone = input("enter Phone:")
           getemail = input("enter Email :")
           getdesignation = input("enter Designation :")
           getsalary = input("enter Salary :")
           getcompany = input("enter Company Name :")
           connection.execute("update employee set name='" + getname + "',phone=" + getphone + ",email='" + getemail + "',designation='" + getdesignation + "',salary=" + getsalary + ",company='" + getcompany + "' where empCode=" + getempcode + "")
           print("updated successfully.")
           connection.commit()
    elif choice == 5:
           getempcode = input("Delete Employee using Employee Code :")
           connection.execute("delete from employee where empCode=" + getempcode + "")
           print("Deleted successfully.")
           connection.commit()
    elif choice == 6:
           result = connection.execute("select * from employee where salary > 50000")
           table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
           for i in result:
               table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
           print(table)
           connection.commit()
    elif choice == 7:
           result = connection.execute("select company,count(*) from employee group by company")
           table = PrettyTable(["Company", "Count"])
           for i in result:
               table.add_row([i[0], i[1]])
           print(table)
    elif choice == 8:
           lowersalary = input("Enter low salary :")
           highersalary = input("Enter high salary :")

           result = connection.execute(
               "select * from employee where salary between " + lowersalary + " and " + highersalary + " order by name")
           table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
           for i in result:
               table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
           print(table)
           connection.commit()
    elif choice == 9:
           result = connection.execute("select * from employee where salary < (select avg(salary) from employee)")
           table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
           for i in result:
               table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
           print(table)
           connection.commit()

    elif choice == 10:
        break

    else:
        print("wrong choice")



