from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
def create_app():
    #this is our flask app
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(flask_app)
    Migrate(flask_app, db)

    


    return flask_app

# function to render index page
@app.route('/')
def index():
    profiles = profile.query.all()
    return render_template('index.html', profiles=profiles)

@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

# function to add profiles
@app.route('/add', methods=["POST"])
def profile():
    # In this function we will input data from the 
    # form page and store it in our database. Remember 
    # that inside the get the name should exactly be the same 
    # as that in the html input fields
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")

    # create an object of the Profile class of models and 
    # store data as a row in our datatable
    if first_name != '' and last_name != '' and age is not None:
        p = profile(first_name=first_name, last_name=last_name, age=age)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

@app.route('/delete/<int:id>')
def erase(id):
    
    # deletes the data on the basis of unique id and 
    # directs to home page
    data = profile.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


