from flask import Flask, request
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('config')
#db = SQLAlchemy(app)

from theApp import views #, models -- only need this when we have a db