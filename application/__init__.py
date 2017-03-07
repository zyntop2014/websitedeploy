from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_googlemaps import GoogleMaps

application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)
googlemap = GoogleMaps(application)
