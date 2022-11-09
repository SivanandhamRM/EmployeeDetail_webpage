import os
import sqlite3


def init_db():
    #connecting to existing database, if database not exists, it creates a new database.
    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()
    print("Database created and opened successfully")

    try:
        cursor.execute('''CREATE TABLE Dept
            (department TEXT PRIMARY KEY
            );''')

        print('Dept database created successfully')

    #insert Dept data
        cursor.execute("insert into Dept values ('Finance')");
        cursor.execute("insert into Dept values ('Booking')");
        cursor.execute("insert into Dept values ('Maintenance')");
        cursor.execute("insert into Dept values ('Food')");
        cursor.execute("insert into Dept values ('Product')");
        cursor.execute("insert into Dept values ('Engineering')");
    except:
        pass

    #create Employee table
    try:
        cursor.execute('''CREATE TABLE Employee
            (rowid INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT,
            email TEXT NOT NULL,
            phone INT,
            salary INT,
            department TEXT,
            FOREIGN KEY (department)
            REFERENCES Dept(department));''')

        print('Employee database created successfully')      


        #Insert data into Employee table
        cursor.execute("insert into Employee(fname, lname, email, phone, salary, department) values ('Sivanandham', 'RM', 'siva1342001@gmail.com', 78675532768, 50000, 'Finance')");
        cursor.execute("insert into Employee(fname, lname, email, phone, salary, department) values ('Sivaram', 'T', 'siva@gmail.com', 7861554268, 55000, 'Food')");
        cursor.execute("insert into Employee(fname, lname, email, phone, salary, department) values ('rahul', 'RM', 'rahul@gmail.com', 78675532768, 50000, 'Finance')");
        cursor.execute("insert into Employee(fname, lname, email, phone, salary, department) values ('harish', 'RM', 'harish@gmail.com', 78675532768, 50000, 'Product')");

    except Exception as e:
        print(e)
        

    conn.commit()

    print("Records inserted successfully")

    conn.close()


#function to insert new user into Employee data
def new_user(fname, lname, email, phone, salary, department):

    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()
    cursor.execute("insert into Employee(fname, lname, email, phone, salary, department) values(?, ?, ?, ?, ?, ?)", (fname, lname, email, phone, salary, department))
    conn.commit()
    conn.close()


#function to update the department value
def update_dept(e_id, newdept):

    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()

    query = (
        '''UPDATE Employee 
        SET department = ? 
        WHERE rowid = ?''')

    cursor.execute(query, (newdept, e_id))
    conn.commit()
    conn.close()


#function to delete the record in Employee table
def deleteuser(e_id):

    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()

    query = "delete from Employee where rowid = ?"
    cursor.execute(query, (e_id,))
    conn.commit()
    conn.close()
    

#function to read Employee table records
def get_employee_values():
    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()
    cursor.execute('select * from Employee')
    

    row_headers = [x[0] for x in cursor.description] 
    result = cursor.fetchall()
    json_data = []

    for res in result:
        res = list(res)
        json_data.append(dict(zip(row_headers, res)))

    conn.close()
    return json_data


#function to read Dept table records
def get_dept_values():
    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()
    cursor.execute('select * from Dept')

    row_headers = [x[0] for x in cursor.description] 
    result = cursor.fetchall()
    json_data = []

    for res in result:
        res = list(res)
        json_data.append(dict(zip(row_headers, res)))

    conn.close()
    return json_data
