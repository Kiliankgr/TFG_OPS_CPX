from application import app, db
from flask import render_template,flash, request
from .forms import Add_Modelo_Form


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
    return render_template('home.html' , posts = posts)  #TO DO cambiar post

# Por ahora mostrará los modelos y permitirá modificar su contenido o añadir nuevos 
@app.route("/mostrar_modelos")
def mostrar_modelos():
    form_add_modelo = Add_Modelo_Form
    #for instancia in db.Instancias.find()
    return render_template('modelos.html', methods=["GET", "POST"], form_add_modelo = form_add_modelo)

# Prueba para comprobar que podemos añadir elementos a la base de datos
@app.route("/add_modelos")
def add_modelos():
    form_add_modelo = Add_Modelo_Form()
    #for instancia in db.Instancias.find()
    return render_template('add_modelos.html', methods=["GET", "POST"], form_add_modelo = form_add_modelo)