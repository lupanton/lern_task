from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    gender = db.Column(db.String(3))
    date = db.Column(db.Date())
    is_active = db.Column(db.Integer)

    def __init__(self, username, email, gender, date, is_active):
        self.username = username
        self.email = email
        self.gender = gender
        self.date = date
        self.is_active = is_active