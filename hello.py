
from flask import Flask, render_template, flash
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

#create an instance of flask to run application.
app = Flask(__name__)  # always start a flask instance like this.

#CRF token for vorm validation


#create form class
class NameForm(FlaskForm):
    name = StringField("what is your name:?", validators=[DataRequired()])
    submit=SubmitField("submit")

#create index Routes
@app.route('/')

#def index():
   # return "<h1>Hello World!</h1>"
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
   # return "<h1>Hello {}!!</h1>".format(name)
   return render_template("user.html", user=name)

#Create Custom Error Pages:

#InvaliD url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html' ), 404

#interna;l Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

#create Name Page
@app.route('/name', methods=['GET', 'POST'])

def name ():
    name = None
    form = NameForm()
    #Validate form data
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
        flash("Form Submitted Successfully!")
    return render_template('name.html', name=name, form=form)


