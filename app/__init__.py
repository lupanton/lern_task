from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from app import routes, models
bootstrap = Bootstrap(app)

with app.app_context():
    db.create_all()
    if db.session.query(models.User).first() == None:
        user1 = models.User('Иван Соколов', 'ivan@rumbler.ru', 'м', date(2001,12,15), 1)
        user2 = models.User('Мария Иванова', 'ivanova@rumbler.ru', 'ж', date(2001,12,12), 0)
        user3 = models.User('Егор Фролов', 'egor@rumbler.ru', 'м', date(2003,11,11), 1)
        user4 = models.User('Анна Скворцова', 'anna@rumbler.ru', 'ж', date(2000,12,12), 1)
        user5 = models.User('Федор Николаев', 'nikol@rumbler.ru', 'м', date(2001,12,11), 0)
        user6 = models.User('Светлана Васина', 'vasina@rumbler.ru', 'ж', date(2001,12,12), 1)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)
        db.session.add(user5)
        db.session.add(user6)
        db.session.commit()
        db.session.close()

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)