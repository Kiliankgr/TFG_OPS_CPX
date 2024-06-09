from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] = '90355efb416d0e299793fc8e9b19bf9edfc6dc59' #revisar si necesaria
app.config["MONGO_URI"] = "mongodb+srv://kilian:00brinco@cluster0.0kmenyr.mongodb.net/" #debríamos ocultar a futuro la contraseña

# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes   