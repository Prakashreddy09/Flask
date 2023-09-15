from flask import Blueprint,render_template,request,flash,Flask
from flask_mysqldb import MySQL





auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('Password')
    return render_template('login.html')
@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        password1 = request.form.get('Password')
        password2 = request.form.get('Passwordr')
        print(password1)
        if password1 != password2:
            flash('Wrong',category='error')

    return render_template('sign-up.html')


# @auth.route('/doctor')
# def doctor():
#     cur = MySQL.connection.cursor()
#     cur.execute('SELECT * FROM your_table')
#     data = cur.fetchall()
#     cur.close()
#     return render_template('doctor.html', data=data)

@auth.route('/patient')
def patient():
    return "<h1>Patient</h1>"


