from flask import Flask, render_template

app = Flask(__name__)

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
