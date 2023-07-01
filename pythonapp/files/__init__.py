from flask import Flask
from flask_sqlalchemy import SQLAlchemy;
import mysql.connector
import os;
# from .config import connection
baseDir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'database.db')
    # app.config['SQLALCHEMY_DATABASE_URI'] = connection
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    with app.app_context():
        db.create_all()

    create_database(app)

    return app

def create_database(app):
    if not os.path.exists('files/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created')



