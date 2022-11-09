from flask import Flask, request, render_template, url_for, redirect
# import mysql.connector
import sqlite3
from sql_func import init_db

from sql_func import get_employee_values, get_dept_values, update_dept, deleteuser, new_user

app = Flask(__name__, template_folder = 'template')


@app.route('/', methods=['GET', 'POST'])
def employee():

    result = get_employee_values()
    d_result = get_dept_values()

    if request.method == 'GET':
        return render_template('employee.html', result=result, d_result=d_result)

    elif request.method == 'POST':
        updated_dept = request.form.get('departments')
        
        fname = None

        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        salary = request.form.get('salary')
        department = request.form.get('department')

        if fname != None:
            new_user(fname, lname, email, phone, salary, department)

        else:

            e_id = request.form.get('row_edit')
            edit = request.form.get('edit')
            delete = None

            if e_id==None:
                e_id = request.form.get('row_delete')
                delete = request.form.get('delete')
                edit = None

            if edit==None:
                deleteuser(e_id)

            else:
                update_dept(e_id, updated_dept)

        

        return redirect(url_for('employee', result=result, d_result=d_result))



if __name__== '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True)