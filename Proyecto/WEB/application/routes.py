from application import app, db
from flask import render_template,flash, request, redirect
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
@app.route("/add_modelos", methods=["GET", "POST"])
def add_modelos():

    if request.method == "POST":
        form_add_modelo = Add_Modelo_Form(request.form)
        add_modelo_nombre = form_add_modelo.nombre.data
        add_modelo_contenido = form_add_modelo.contenido.data
        
        #pymongo flask, insertamos en la coleccion Instancias
        db.Instancias.insert_one({
            "nombre" : add_modelo_nombre, # por lo visto
            "contenido" : add_modelo_contenido
        })
        #Mensaje al usuario
        flash("Instancia añadida correctamente", "success")
        return redirect("/")
    else:
        form_add_modelo = Add_Modelo_Form()
    return render_template('add_modelos.html', form_add_modelo = form_add_modelo) 