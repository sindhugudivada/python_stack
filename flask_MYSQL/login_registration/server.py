from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from datetime import datetime
import md5
app = Flask(__name__)
app.secret_key = "THIS is a secret key"
mysql = MySQLConnector(app, 'registration')


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login_page')
def login():
    return render_template('success.html')

# after LOG IN

@app.route('/login', methods=['post'])
def longinprocess():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    user_query = "SELECT * FROM registration where email = :email"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)

    print user
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    # invalid email
    if len(request.form['email']) < 1:
        flash("InValid Email format!")
        return redirect('/login_page')
    # email doesn't exists
    elif len(request.form['password']) < 1:
        flash("no password")
        return redirect('/login_page')
    # invalid user
    elif not user:
        flash("Wrong email")
        return redirect('/login_page')
    # invalid password
    elif user[0]['password'] != password:
        flash("Wrong password")
        return redirect('/login_page')
    # correct info
    else:
        session['id'] = user[0]['id']
        return redirect('/welcome')


@app.route('/register', methods=['POST'])
def check():
    print"/register"
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password =request.form['confirm_password']
    regex = re.compile(r'^[^\W_]+(-[^\W_]+)?$', re.U)
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    # invalid first name
    if len(first_name) < 2 or first_name.isalpha() == False:
        flash("First name has to have at least two alphabetic characters ")
        return redirect('/')
    # invalid last name
    elif len(last_name) < 2 or not regex.match(last_name):
        flash("Last name has to have at least two alphabetic characters ")
        return redirect('/')
    # invail email
    elif len(email) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email format!")
        return redirect('/')
    # invalid password
    elif len(password) < 1:
        flash("blank")
    elif password != confirm_password:
        flash("Passwords are not matching!")
        return redirect('/')
    # correct info
    else:
        password = md5.new(request.form['password']).hexdigest()
    # we want to insert into our query.
        query = "INSERT INTO registration (email,first_name,last_name,password) VALUES (:email, :first_name,:last_name,:password)"
    # We'll then create a dictionary of data from the POST data received.
        data = {'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': password}
        mysql.query_db(query, data)
    return redirect('/welcome')


@app.route('/welcome')
def success():
    return render_template("welcome.html")


app.run(debug=True)
