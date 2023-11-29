# -*- coding: utf-8 -*- 
from flask import *
from app import app

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
