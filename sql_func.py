# import mysql.connector
import os
import sqlite3



# config = {
#     'user': 'sivanandham',
#     'password': 'password',
#     'host': 'localhost',
#     'port': '3306',
#     'database': 'rails' 
# }


def init_db():
    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()
    print("Database created and opened successfully")

    try:
        cursor.execute('''CREATE TABLE Dept
            (department TEXT PRIMARY KEY
            );''')

        print('Dept database created successfully')

        cursor.execute("insert into Dept values ('Finance')");
        cursor.execute("insert into Dept values ('Booking')");
        cursor.execute("insert into Dept values ('Maintenance')");
        cursor.execute("insert into Dept values ('Food')");
        cursor.execute("insert into Dept values ('Product')");
        cursor.execute("insert into Dept values ('Engineering')");
    except:
        pass


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

        #Insert Data into Dept database
        


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


# def init_db():
#     global config
#     connection = mysql.connector.connect(**config)
#     cursor = connection.cursor()

#     with open("db.sql", 'r') as file1:
#         sql_cmds = file1.read()

#     sql_cmds1 = sql_cmds.split(";")

#     for i in range(0, len(sql_cmds1)-1):
#         query = sql_cmds1[i] + ';'
#         cursor.execute(query)

#     connection.commit()
#     cursor.close()
#     connection.close()


def new_user(fname, lname, email, phone, salary, department):

    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()
    cursor.execute("insert into Employee(fname, lname, email, phone, salary, department) values(?, ?, ?, ?, ?, ?)", (fname, lname, email, phone, salary, department))
    conn.commit()
    conn.close()


    # global config
    # connection = mysql.connector.connect(**config)

    # print('**************************************************', department)
    # cursor = connection.cursor()
    # query = (
    #     f"INSERT INTO Employee "
    #     "(fname, lname, email, phone, salary, department)"
    #     "VALUES (%s, %s, %s, %s, %s, %s)"
    # )
    # cursor.execute(query, (fname, lname, email, phone, salary, department))
    # connection.commit()
    # cursor.close()

    # connection.close()


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

    # global config
    # connection = mysql.connector.connect(**config)

    # cursor = connection.cursor()

    # query = (
    #     "UPDATE Employee "
    #     "SET department = %s "
    #     "WHERE e_id = %s"
    # )


    # cursor.execute(query, (newdept, e_id))
    # connection.commit()
    # cursor.close()

    # connection.close()



def deleteuser(e_id):

    conn = sqlite3.connect('details.db')
    cursor = conn.cursor()

    query = "delete from Employee where rowid = ?"
    cursor.execute(query, (e_id,))
    conn.commit()
    conn.close()
    


    # global config
    # connection = mysql.connector.connect(**config)

    # cursor = connection.cursor()
    # query = f"DELETE FROM Employee WHERE e_id = {e_id}"
    # print(query)


    # cursor.execute(query)  
    # connection.commit()
    # cursor.close()

    # connection.close()



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



    # global config
    # connection = mysql.connector.connect(**config)

    # cursor = connection.cursor()
    # cursor.execute(f'SELECT * FROM {table};')

    # row_headers = [x[0] for x in cursor.description] 
    # result = cursor.fetchall()
    # json_data = []

    # for res in result:
    #     res = list(res)
    #     json_data.append(dict(zip(row_headers, res)))

    # cursor.close()
    # connection.close()
    # return json_data

