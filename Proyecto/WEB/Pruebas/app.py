from flask import Flask, render_template
from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.server_api import ServerApi #revisar

config = dotenv_values(".end")

app = Flask(__name__)

uri = "mongodb+srv://kilian:00brinco@cluster0.0kmenyr.mongodb.net/"
#example should be change
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    } 
]

@app.route("/")
def home():
    #conexción a Mongo
    #app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database= MongoClient(uri, server_api=ServerApi('1'))
    #app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    try:
        app.database.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return render_template('home.html', posts = posts)  

@app.route("/about")
def about():
    return render_template('about.html', title='About')