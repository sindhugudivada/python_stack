from flask import Flask,render_template,redirect,request,session,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app=Flask(__name__)
app.secret_key="sindhu"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results',methods=['POST'])
def create_user():
    email = request.form['email']
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password =  request.form['password']
    confirm_password = request.form['confirm_password']
    return render_template('results.html',email = email, first_name = first_name, last_name = last_name, password = password,confirm_password=confirm_password)
app.run(debug=True) 

