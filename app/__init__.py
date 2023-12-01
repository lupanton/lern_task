from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.app_context().push()
from app import routes, models
bootstrap = Bootstrap(app)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)