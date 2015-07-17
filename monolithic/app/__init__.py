from flask import Flask
from session import MongoSessionInterface
#FIXME change this to a proper loader
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object( 'config' )
app.session_interface = MongoSessionInterface(
    host=app.config["MONGODB"]["host"],
    db=app.config["MONGODB"]["session"]["db"])

db = MongoClient(app.config["MONGODB"]["host"])[app.config["MONGODB"]["data"]["db"]]
fts = 'data'
from app import views
