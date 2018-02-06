from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')
@app.route('/dojos',methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    return redirect('/')   
  
    
app.run(debug=True)    
