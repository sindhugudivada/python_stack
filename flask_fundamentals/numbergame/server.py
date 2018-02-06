import random
from flask import Flask,session,redirect,request,render_template
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def random():
    if 'somekey' in session 
    session['somekey']=random.randrange(0,101) 
    if a > 0 and a < 50
        print 'Too low!' 
    else:
        print 'Too high'     
    session['somekey']=60
    session.pop('somekey')
    return render_template('counter.html')  
app.run(debug=True)  
@app.route('/count')
def counter1():
    session['count']=1
    return redirect('/') 
app.run(debug=True)  
