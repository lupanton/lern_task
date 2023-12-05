# -*- coding: utf-8 -*- 
from flask import *
from app import app
from app.models import User 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)
