from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'anime'
mysql = MySQL(app)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = request.form ['user']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO `usuarios`(`usuario`, `pass`) VALUES (%s,%s)',(user,password))
        mysql.connection.commit()
        print(user)
        print(password)
        return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)