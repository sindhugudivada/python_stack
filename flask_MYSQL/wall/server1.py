from flask import Flask, request, redirect, render_template, flash, session
import re
from mysqlconnection import MySQLConnector
import md5
import os, binascii

app = Flask(__name__)
app.secret_key = "secret_key"
salt = binascii.b2a_hex(os.urandom(15))
mysql = MySQLConnector(app,'wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/wall')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['first_name']) < 2 or not request.form['first_name'].isalpha():
         flash("First Name cannot be less than 2 characters!")
    elif len(request.form['last_name']) < 2 or not request.form['last_name'].isalpha():
        flash("Last Name cannot be less than 2 characters!")
    elif len(request.form['password']) < 1:
            flash("Password cannot be blank!")
    elif len(request.form['password']) < 8:
        flash("Password cannot contain less than 8 characters!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match!")
    else:
        password = request.form['password']
        pw_hash = md5.new(password + salt).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash,
            'salt': salt
        }
        mysql.query_db(query, data)
        query = "SELECT * FROM users WHERE email=:email"
        data = {'email' : request.form['email']}
        session['user'] = mysql.query_db(query, data)[0]
        return redirect('/wall')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email=:email LIMIT 1"
    data = {'email' : email}
    user = mysql.query_db(query, data)
    print "user:",user
    if user:
        if user[0]['password'] == md5.new(password + user[0]['salt']).hexdigest():
            session['user'] = user[0]
            return redirect('/wall')
        else:
            flash("Your login information was not correct. Please try again")
    else:
        flash("Your login email does not exist.")
    return redirect('/')

@app.route('/wall')
def wall():
    query = "SELECT users.first_name AS first_name, users.last_name AS last_name, messages.id AS id, messages.user_id AS user_id, messages.message AS message, messages.created_at as message_time, messages.id AS msg_id FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(query)
    query = "SELECT users.first_name AS first_name, users.last_name AS last_name, comments.id AS id, comments.user_id AS user_id, comments.comment AS comment, comments.created_at as comment_time, comments.message_id AS msg_id FROM users JOIN comments ON comments.user_id = users.id ORDER BY comments.created_at ASC"
    comments = mysql.query_db(query)
    return render_template('wall.html', user=session['user'], messages=messages, comments=comments)

@app.route('/messages', methods=['POST'])
def messages():
    message = request.form['message']
    if not message or message.isspace():
        flash("Please enter your meesage!")
    else:
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
        data = {
            'message': message,
            'user_id': session['user']['id']
            }
        mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/messages/<id>/delete', methods=['POST'])
def delete_message(id):
    query = "DELETE FROM comments WHERE message_id = :id; DELETE FROM messages WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/comments/<msg_id>', methods=['POST'])
def comments(msg_id):
    comment = request.form['comment']
    if not comment or comment.isspace():
        flash("Please enter your comment!")
    else:
        query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
        data = {
            'comment': comment,
            'user_id': session['user']['id'],
            'message_id': msg_id
            }
        mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments/<id>/delete', methods=['POST'])
def delete_comment(id):
    query = "DELETE FROM comments WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True