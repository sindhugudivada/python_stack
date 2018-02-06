from flask import Flask,session,redirect,request,render_template
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def counter():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1    
    return render_template('counter.html')  
app.run(debug=True)  
@app.route('/count')
def counter1():
    session['count']=1
    return redirect('/') 
app.run(debug=True)  
