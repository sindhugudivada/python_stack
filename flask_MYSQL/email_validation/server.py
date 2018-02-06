from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = "THIS is a secret key"
mysql = MySQLConnector(app, 'email')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def check():
    print "in result"
    email = request.form['emails']
    print email
    data = {'email': email,'now':datetime.now()}
    query = "INSERT INTO emails (emails, created_at) VALUES (:email, :now)"

    retrieve_emails = "SELECT * FROM emails"

    # Each row contains both email and timestamps.
    email_entries = mysql.query_db(retrieve_emails)

    print email_entries,

    my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not my_re.match(email):
        flash("INVALID email")
        return redirect('/')
    for entry in email_entries:
        if entry['emails'] == email:
            flash("email is available")
            return redirect('/success')
    print "the email you entered is valid! thankyou!"
    mysql.query_db(retrieve_emails, data)
    return redirect("/")
    

@app.route('/success')
def success():
    """
    Success 
    """
    query = "SELECT emails, created_at FROM emails"
    emails = mysql.query_db(query)
    print emails
    return render_template("success.html",emails=emails)
app.run(debug=True)
