from flask import Flask
from flask_pymongo import PyMongo
#añadidoda ahora para ver si así sí me puedo conectar
from pymongo import MongoClient
from pymongo.server_api import ServerApi #revisar

app = Flask(__name__)

app.config["SECRET_KEY"] = '90355efb416d0e299793fc8e9b19bf9edfc6dc59' #revisar si necesaria
app.config["MONGO_URI"] = "mongodb+srv://kilian:00brinco@cluster0.0kmenyr.mongodb.net/" #debríamos ocultar a futuro la contraseña

# mongodb database
# Debería funcionar pero no lo hace
#mongodb_client = PyMongo(app)
#db = mongodb_client["Modelos"]

#probando otra manera Esta funciona seguro
client = MongoClient(app.config["MONGO_URI"], server_api=ServerApi('1'))
db = client["Modelos"]
  

'''
for coll in db.list_collection_names():
    print(coll)
'''
from application import routes