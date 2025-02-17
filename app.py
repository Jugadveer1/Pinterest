# this file is for creating a database and flask application


from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

# this is a intance of our data base
db = SQLAlchemy()

def create_app():
    #this is our flask app
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(flask_app)
    Migrate(flask_app, db)

    


    return flask_app