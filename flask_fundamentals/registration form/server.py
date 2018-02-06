from flask import Flask, render_template, request, redirect, session, flash
from validations import formIsValid
app = Flask(__name__)
app.secret_key="secretsrunsdeep"

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/submit', methods=['post'])
def show_info():
    state = formIsValid(request.form)
    print state
    if (state['isValid']):
        print "success"
        return redirect('/success')
    else:
        print "error"
        for error in state['errors']:
            flash(error)
        return redirect('/')

@app.route('/success')
def success():
    return "Success"

app.run(debug=True)