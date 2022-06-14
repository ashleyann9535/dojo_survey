from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import survey

# put in routes
@app.route('/')
def home():
    return render_template('index.html')

#Create 
@app.route('/create', methods = ['POST'])
def process():
    # if there are errors:
    # We call the staticmethod on model to validate
    if not survey.Survey.validate_survey(request.form):
        # redirect to the route where the form is rendered.
        return redirect('/')
    # else no errors:
    survey.Survey.create_survey(request.form)

    return redirect('/result')

#Read 
@app.route('/result/')
def result():
    this_survey = survey.Survey.read_survey()
    print('*****', this_survey)
    return render_template('result.html', this_survey = this_survey)

#Update 


#Delete 
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')