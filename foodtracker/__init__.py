from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME = 'database.db'  # Database name


def create_database(app):
    # If the DB doesn't exist, create it
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)


app = Flask(__name__)
app.config['SECRET_KEY'] = '0ea83976c3188e275b425fc35796ddc9'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db = SQLAlchemy(app)

from .routes import main

app.register_blueprint(main)

from .models import Food, Log

# login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'  # where to go if user NOT logged in
# login_manager.login_message = 'You must be logged in to access this page.'
# login_manager.login_message_category = 'info'
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

create_database(app)
