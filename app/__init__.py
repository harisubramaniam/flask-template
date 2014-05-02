from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.init_app(app) #might not need this

migrate = Migrate(app, db)
manager = Manager(app)

from app import models, views
