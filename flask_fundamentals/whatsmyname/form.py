from flask import Flask,render_template,request,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users')
def create_user1():
    return render_template("form.html")
@app.route('',methods=['POST'])
def create_user():
    print request.form
    name = request.form['name']
    return redirect('/')   
app.run(debug=True)
