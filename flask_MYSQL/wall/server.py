import re
import md5
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime
import os, binascii
app = Flask(__name__)
app.secret_key = "THIS is a secret key"
mysql = MySQLConnector(app, 'wall')


@app.route('/', methods=['GET'])
def index():
    if 'user' in session:
        return redirect('/wall')
    return render_template('index.html')

# after LOG IN
@app.route('/login', methods=['post'])
def longinprocess():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    user_query = "SELECT * FROM users where email = :email"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)

    print user
    if user:
        if user[0]['password'] == md5.new(password).hexdigest():
            session['user'] = user[0]
            return redirect('/wall')
        else:
            flash("Your login information was not correct. Please try again")
    else:
        flash("Your login email does not exist.")
    return redirect('/')


@app.route('/register', methods=['POST'])
def check():
    print"/register"
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
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
        query = "INSERT INTO users (email,first_name,last_name,password) VALUES (:email, :first_name,:last_name,:password)"
    # We'll then create a dictionary of data from the POST data received.
        data = {'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'password': password}
        mysql.query_db(query, data)
        session['user'] = mysql.query_db(query, data)
        return redirect('/wall')
    return redirect('/')


@app.route('/wall')
def wall():
    query = "SELECT users.first_name AS first_name, users.last_name AS last_name, messages.id AS id, messages.user_id AS user_id, messages.message AS message, messages.created_at as message_time, messages.id AS msg_id FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(query)
    query = "SELECT users.first_name AS first_name, users.last_name AS last_name, comments.id AS id, comments.user_id AS user_id, comments.comment AS comment, comments.created_at as comment_time, comments.id AS msg_id FROM users JOIN comments ON comments.user_id = users.id ORDER BY comments.created_at ASC"
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


app.run(debug=True)
