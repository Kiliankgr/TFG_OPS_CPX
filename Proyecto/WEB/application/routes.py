from application import app, db
from flask import render_template,flash, request, redirect
from .forms import Add_Instancia_Form, Mod_Instancia_Form
from datetime import datetime
import time

import json 
from bson import ObjectId


@app.route("/")
def home():
    return render_template('home.html')  #TO DO cambiar post

# Por ahora mostrará los instancias y permitirá modificar su contenido o añadir nuevos 
@app.route("/mostrar_instancias", methods=["GET", "POST", "DELETE"])
def mostrar_instancias():
    
    #instancias = db.Instancias.find().sort("nombre")
    #instancias = [convert_objectid_to_str(instancia) for instancia in instancias]
  
    instancias = []
    
    for instancia in db.Instancias.find().sort("nombre"):
        #retocamos algunos datos como el id para que sean enviados como strings
        instancia["_id"] = str(instancia["_id"])
        instancia["nombre"] = str(instancia["nombre"])
        instancia = convert_objectid_to_str(instancia)        
        instancias.append(instancia)

    # Modificar Instancias
    form_mod_instancia = Mod_Instancia_Form()
    if request.method == "POST":
        
        form_mod_instancia = Mod_Instancia_Form(request.form)
        modificar_instancia(id, form_mod_instancia)
        
    return render_template('instancias.html', instancias= instancias ,form_mod_instancia = form_mod_instancia)

def modificar_instancia(id, form_mod_instancia):
    mod_instancia_contenido = form_mod_instancia.contenido.data
    print("modificar instancia")
        #Pasamos a Json el contenido
    try:
        contenido_json = json.loads(mod_instancia_contenido)
        fecha_actual = time.strftime('%Y-%m-%d_%H:%M:%S')   
        nombre_nuevo = db.Instancias.find({"_id": id}).nombre

        print("Nombre: " + nombre_nuevo)
        #pymongo flask, modificamos en la coleccion Instancias
        #ya que se modifica el contenido la fecha y el nombre se actualizarán
        '''
        db.Instancias.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "contenido": contenido_json,
            "nombre_fichero" : add_instancia_nombre + "_" + fecha_actual,
            "fecha" : fecha_actual,
        }})
        '''
        #Mensaje al usuario
        flash("Instancia modificada correctamente", "success") # No veo que se muestre el mensaje revisar
    except json.JSONDecodeError as e:
        # Manejo de errores en caso de que el contenido no sea un JSON válido
        flash(f"Error, el contenido no tiene el formato JSON correcto:\n {e}", "error")

#Convertimos el object_id
def convert_objectid_to_str(instancia):
    for key, value in instancia.items():
        if isinstance(value, ObjectId):
            instancia[key] = str(value)
    return instancia


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