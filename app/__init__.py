from flask import Flask, Blueprint

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:postgres@localhost:5432/simons_example_db'
    app.config['SECRET_KEY'] = 'KHGLYTDKTEASRYDT'
    
    db.init_app(app)
    migrate.init_app(app, db)
    from .routes import blog_bp
    app.register_blueprint(blog_bp)
    from .models.users import Users
    return app



 

