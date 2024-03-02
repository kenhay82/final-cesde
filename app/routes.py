from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infodog')
def infodog():
    return render_template('infodog.html')