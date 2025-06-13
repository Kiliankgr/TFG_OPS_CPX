from flask import Flask
from flask_pymongo import PyMongo

from pymongo import MongoClient
from pymongo.server_api import ServerApi 
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") 
app.config["MONGO_URI"] = os.getenv("MONGO_URI") 


client = MongoClient(app.config["MONGO_URI"], server_api=ServerApi('1'))
db = client["Modelos"]
  
from application import routes