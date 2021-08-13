from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contact'
 
mysql = MySQL(app)
 
@app.route('/form')
def form():
    return render_template('form.html')

 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO contact_form VALUES(%s,%s,%s,%s)''',(name,email,contact,address))
        mysql.connection.commit()
        cursor.close()
        
        return f"Data submitted successfully!!"
 
app.run(host='localhost', port=5000, debug=True)