# -*- coding: utf-8 -*- 
from flask import *
from app import app
from app.models import User
from . import db
from . import date, datetime

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/users')
def users():
    users = db.session.query(User).where(User.is_active == 1)
    return render_template('users.html', users=users)

@app.route('/add_form', methods=['POST'])
def add_row():
    return render_template('add_row.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        user = User(username=request.form['name'],
                     email=request.form['email'],
                     gender=request.form['gender'],
                     date=datetime.strptime(request.form['date'], "%Y-%m-%d").date(),
                     is_active=request.form['is_active']
                     )
        db.session.add(user)
        db.session.commit()
    return redirect('/users')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        user = db.session.query(User).get(id)
        db.session.delete(user)
        db.session.commit()
    return redirect('/users')