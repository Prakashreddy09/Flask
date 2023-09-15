from flask import Flask,render_template,redirect,request
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'prakashreddy'

    app.config['MYSQL_HOST'] = 'localhost'  # Your MySQL server hostname
    app.config['MYSQL_USER'] = 'root'  # Your MySQL username
    app.config['MYSQL_PASSWORD'] = ''  # Your MySQL password
    app.config['MYSQL_DB'] = 'assignment'  # Your MySQL database name
    mysql = MySQL(app)
    
    @app.route('/doctor')
    def doctor():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Parts')
        data1 = cur.fetchall()
        cur.close()
        return render_template('doctor.html', data=data1)
    
    def get_db():
       return mysql.connector.connect(
        host='your_host',
        user='your_username',
        password='your_password',
        database='your_database'
       )

    @app.route('/doctor/<Age>', methods=['POST'])
    def update_data(id):
    # Retrieve data from the request (e.g., form submission)
        new_value = request.form.get('new_value')

    # Connect to the database
        db = get_db()
        cursor = db.cursor()

    # Perform the data update using SQL
        try:
            update_query = "UPDATE your_table SET column_to_update = Age  WHERE id = 3"
            cursor.execute(update_query, (new_value, id))
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            cursor.close()
            db.close()

    # Redirect to a relevant page or return a response
        return redirect('/success')


    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    
    return app