from application import app, db
from flask import render_template,flash, request, redirect
from .forms import Add_Instancia_Form, Mod_Instancia_Form, Instancia_Modelo_Form
from datetime import datetime
import time
import subprocess
import json 
from bson import ObjectId

RUTA_AL_MODELO = '../OPS_CPX/emir_cpx'
RUTA_FICHERO_TMP = 'tmp.txt'
RUTA_INSTANCIA_TMP = 'fichero_instancia_tmp.txt'
RUTA_SALIDA_TMP = 'fichero_salida_tmp.txt'
@app.route("/")
def home():
    return render_template('home.html') 

# Por ahora mostrará los instancias y permitirá modificar su contenido o añadir nuevos 
@app.route("/mostrar_instancias", methods=["GET", "POST", "DELETE"])
def mostrar_instancias():
    resultado_ultimo_modelo = ""
    #instancias = db.Instancias.find().sort("nombre")
    #instancias = [convert_objectid_to_str(instancia) for instancia in instancias]
  
    instancias = []
    
    for instancia in db.Instancias.find().sort("nombre"):
        #retocamos algunos datos como el id para que sean enviados como strings
        instancia["_id"] = str(instancia["_id"])
        instancia["nombre"] = str(instancia["nombre"])
        instancia = convert_objectid_to_str(instancia)        
        instancias.append(instancia)

    #Forms
    form_mod_instancia = Mod_Instancia_Form()
    form_instancia_modelo = Instancia_Modelo_Form()
    # Modificar Instancias
    if request.method == "POST":        #Nota revisar ya que probablemente si vamos a mantener los modelos con las instancia, el post deberá de detectar la solicitud si es de mod contenido instancia, o guardar modelo resultante
        print("valores:")
        print(request.form.values)
        print("request value :")
        print(request.form.get("id_instancia_a_probar"))        
        #Diferenciamos las diferentes solicitudes post
        if "probar_btn" in request.form :
            print("Se detectó el btn probar:")
            #Ejecutamos el modelo
            #ins = db.Instancias.find({"_id": ObjectId(request.form.get("id_instancia_a_probar"))}).next()
            #print(ins["contenido"])
            
            for instancia in instancias:
                print("ID: " + instancia["_id"], )
                if instancia["_id"] == request.form.get("id_instancia_a_probar"):
                    #Creamos ficheros temporales
                    f_tmp = open(RUTA_FICHERO_TMP, "w") #revisar si son nesesarios crearlo antes
                    # Escribir el diccionario en un fichero
                    with open(RUTA_INSTANCIA_TMP, 'w') as file:
                        json.dump(instancia["contenido"], file, indent=2)
                    f_salida = open(RUTA_SALIDA_TMP, "w") #revisar si son nesesarios crearlo antes
                    f_tmp.close()
                    f_salida.close()
                    ejecutar_modelo(RUTA_AL_MODELO, RUTA_FICHERO_TMP, RUTA_INSTANCIA_TMP, RUTA_SALIDA_TMP)
                    break
            
            #Para ello deberemos por ahora de crear una serie de ficheros temporales para pasarles el contenido al modelo

            return render_template('instancias.html', instancias= instancias ,form_mod_instancia = form_mod_instancia, form_instancia_modelo = form_instancia_modelo, resultado_ultimo_modelo = resultado_ultimo_modelo)
        
        print("Vamos a modificar una instancia")        
        form_mod_instancia = Mod_Instancia_Form(request.form)
        #necesitamos el id por ahora se me ocurre que se añada al form y que esté en oculto
        modificar_instancia(form_mod_instancia)
        
    return render_template('instancias.html', instancias= instancias ,form_mod_instancia = form_mod_instancia, form_instancia_modelo = form_instancia_modelo,  resultado_ultimo_modelo = resultado_ultimo_modelo)

def modificar_instancia(form_mod_instancia):
    print(str(form_mod_instancia.identificador))
    identificador = form_mod_instancia.identificador.data
    print("ID: " + identificador)
    mod_instancia_contenido = form_mod_instancia.contenido.data
    print("modificar instancia")
    print(mod_instancia_contenido)
        #Pasamos a Json el contenido
    try:
        contenido_json = json.loads(mod_instancia_contenido)
        fecha_actual = time.strftime('%Y-%m-%d_%H:%M:%S')   
        #instancia = db.Instancias.find({"_id": identificador})

        
        #pymongo flask, modificamos en la coleccion Instancias
        #ya que se modifica el contenido la fecha y el nombre se actualizarán
        
        db.Instancias.find_one_and_update({"_id": ObjectId(identificador)}, {"$set": {
            "contenido": contenido_json,
            "fecha" : fecha_actual,
        }})
        
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

@app.route("/probar_instancias", methods=["GET", "POST"])
def probar_instancia():
        
    #instancias = db.Instancias.find().sort("nombre")
    #instancias = [convert_objectid_to_str(instancia) for instancia in instancias]
  
    instancias = []
    
    for instancia in db.Instancias.find().sort("nombre"):
        #retocamos algunos datos como el id para que sean enviados como strings
        instancia["_id"] = str(instancia["_id"])
        instancia["nombre"] = str(instancia["nombre"])
        instancia = convert_objectid_to_str(instancia)        
        instancias.append(instancia)

    #Forms
    form_mod_instancia = Mod_Instancia_Form()
    form_instancia_modelo = Instancia_Modelo_Form()
    # Modificar Instancias
    if request.method == "POST":        #Nota revisar ya que probablemente si vamos a mantener los modelos con las instancia, el post deberá de detectar la solicitud si es de mod contenido instancia, o guardar modelo resultante
        form_mod_instancia = Mod_Instancia_Form(request.form)
        #necesitamos el id por ahora se me ocurre que se añada al form y que esté en oculto
        modificar_instancia(form_mod_instancia)
        
    return render_template('probar_instancias.html', instancias= instancias ,form_mod_instancia = form_mod_instancia, form_instancia_modelo = form_instancia_modelo)

#Función que ejecutará el modelo
def ejecutar_modelo(ruta_del_programa, *args):
    print("Vamos a ejecutar el modelo")
    #se la pasamos al modelo
    
    
    try:
        # Ejecutar el programa con los argumentos dados
        #resultado = subprocess.run([ruta_del_programa, *args], check=True, capture_output=True, text=True)
        #resultado = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
        resultado = subprocess.run([ruta_del_programa, "-h"], shell=True, capture_output=True, text=True)
        print("Argurmentos:" + str(resultado.args))
        print(resultado.stdout)
        return resultado.stdout  # O puedes retornar resultado si quieres incluir stderr y más información
    except subprocess.CalledProcessError as e:
        # Manejar el error si el programa falla
        return f"Error: {e}"