from personalSite import app
from flask import render_template

@app.route('/')
def index():
    #JLC since we are using template inheritance we must render the child template
    return render_template('index.html')

@app.route('/math6')
def math():

    return render_template('math6/homepage.html')

@app.route('/math7')
def math7():

    return render_template('math7/homepage.html')

@app.route('/math8')
def math8():

    return render_template('math8/homepage.html')
