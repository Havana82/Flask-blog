from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Blueprint
from .models.users import Users
from app import db

blog_bp = Blueprint("blog", __name__)

class UserLog(FlaskForm):
    name = StringField('Enter Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    submit = SubmitField('Submit')
    
class UserName(FlaskForm):
    name = StringField('Enter Username', validators = [DataRequired()])
    submit = SubmitField('Submit')
    
@blog_bp.route('/user/add', methods=['GET', 'POST'])

def add_user():
    form = UserLog
    name= None
    email= None
    return render_template("add_user.html",form=form, name=name, email=email)

@blog_bp.route('/')

def index():
    favorite_things = ['man', 'woman', "boy"]
    return render_template("home.html", favorite_things=favorite_things)

@blog_bp.route('/<name>')

def user(name):
    return render_template("user.html", name=name)

@blog_bp.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

@blog_bp.route('/username', methods=['GET','POST'])
def user_name():
    name = None
    form = UserName()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Thank you for your submission")

    return render_template("username.html", name = name, form = form)