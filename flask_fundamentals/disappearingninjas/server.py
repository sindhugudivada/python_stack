from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def index1():
    return render_template('ninjas.html')
@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        return render_template("leo.html")
    elif color == "orange":
        return render_template("mic.html")
    elif color == "red":
        return render_template("ralph.html")
    elif color == "purple":
        return render_template("dona.html")
    else:
        return render_template("nota.html")

app.run(debug=True) 