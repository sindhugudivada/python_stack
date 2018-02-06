from flask import Flask, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = "key"
@app.route('/', methods=['GET','POST'])
def hello_work():
    try:
        session["guess"] = request.form['guess']
        guess = int(session["guess"])
        theRandom = int(session['randomNumber'])

        print "  ", theRandom , "  Random number:" , theRandom , " User Guess: ", guess

        if (guess == theRandom ):
            print "    Good Guess!"
            return render_template('Correct.html')
        if (guess < theRandom):
            print "    Too Small!"
            return render_template('tooLow.html')
        if (guess > theRandom):
            print "    Too Large!"
            return render_template('tooHigh.html')

    except Exception as e:
        print "exception thrown", e
        session["randomNumber"] = random.randrange(0,101)
    return render_template('index.html')
app.run(debug=True)
