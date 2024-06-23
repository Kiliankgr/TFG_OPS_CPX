from application import app, db
from flask import render_template,flash, request, redirect
from .forms import Add_Instancia_Form
from datetime import datetime
import time

import json


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')  #TO DO cambiar post

# Por ahora mostrará los instancias y permitirá modificar su contenido o añadir nuevos 
@app.route("/mostrar_instancias", methods=["GET", "POST"])

def mostrar_instancias():
    instancias = []
    for instancia in db.Instancias.find().sort("nombre" ):
        instancia["_id"] = str(instancia["_id"])
        instancia["nombre"] = str(instancia["nombre"])
        instancia["contenido"] = instancia["contenido"]
        instancias.append(instancia)
    return render_template('instancias.html', instancias= instancias)


# Prueba para comprobar que podemos añadir elementos a la base de datos
@app.route("/add_instancias", methods=["GET", "POST"])
def add_instancias():

    if request.method == "POST":
        form_add_instancia = Add_Instancia_Form(request.form)
        add_instancia_nombre = form_add_instancia.nombre.data
        add_instancia_contenido = form_add_instancia.contenido.data
        #Pasamos a Json el contenido
        try:
            contenido_json = json.loads(add_instancia_contenido)
            fecha_actual = time.strftime('%Y-%m-%d_%H:%M:%S')   
            #pymongo flask, insertamos en la coleccion Instancias
            db.Instancias.insert_one({
                "nombre" : add_instancia_nombre, 
                "nombre_fichero" : add_instancia_nombre + "_" + fecha_actual,
                "fecha" : fecha_actual,
                "contenido" : contenido_json
            })
            #Mensaje al usuario
            flash("Instancia añadida correctamente", "success") # No veo que se muestre el mensaje revisar
        except json.JSONDecodeError as e:
            # Manejo de errores en caso de que el contenido no sea un JSON válido
            flash(f"Error, el contenido no tiene el formato JSON correcto:\n {e}", "error")
        
        
        
        # return redirect("/")
    else:
        form_add_instancia = Add_Instancia_Form()
    return render_template('add_instancias.html', form_add_instancia = form_add_instancia) 