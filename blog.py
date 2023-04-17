from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///face_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'KHGLYTDKTEASRYDTFL'

db = SQLAlchemy(app)



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return self.name

if __name__ == '__main__':
    app.run(debug=True)    
class UserLog(FlaskForm):
    name = StringField('Enter Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    submit = SubmitField('Submit')
    
class UserName(FlaskForm):
    name = StringField('Enter Username', validators = [DataRequired()])
    submit = SubmitField('Submit')
    
@app.route('/user/add', methods=['GET', 'POST'])

def add_user():
    form = UserLog
    name= None
    email= None
    return render_template("add_user.html",form=form, name=name, email=email)
@app.route('/')

def index():
    favorite_things = ['man', 'woman', "boy"]
    return render_template("index.html", favorite_things=favorite_things)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/username', methods=['GET','POST'])
def user_name():
    name = None
    form = UserName()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Thank you for your submission")

    return render_template("username.html", name = name, form = form)
