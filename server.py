from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)