from flask import Flask
from flask_sqlalchemy import SQLAlchemy;
import mysql.connector
from .config import connection

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin'
    app.config['SQLALCHEMY_DATABASE_URI'] = connection
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    with app.app_context():
        db.create_all()

    return app


