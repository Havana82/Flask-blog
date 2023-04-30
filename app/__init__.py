from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv

def create_app(test_config=None):
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SECRET_KEY'] = os.environ.get("SQLALCHEMY_SECRET_KEY")
    
    db.init_app(app)
    migrate.init_app(app, db)
    from .routes import blog_bp
    app.register_blueprint(blog_bp)
    from .models.users import Users
    return app



 

