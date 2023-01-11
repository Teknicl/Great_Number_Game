from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "anotherDirtySecret"
import random

@app.route('/')
def index():
    if "SecretNumber" not in session:
        session["SecretNumber"] = random.randint(1,50)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def check():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return ("Invalid URL")

if __name__ == '__main__':
    app.run(debug=True)