import re
from this import d
from flask import Flask, render_template

#create an instance of flask to run application.
app = Flask(__name__)  # always start a flask instance like this.

#create Routes
@app.route('/')

#def index():
   # return "<h1>Hello World!</h1>"
def index():
    return render_template("index.html")
@app.route('/user/<name>')

def user(name):
    return "<h1>Hello {}!!</h1>".format(name)

#Create Custom Error Pages:

#InvaliD url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html' ), 404

#interna;l Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
