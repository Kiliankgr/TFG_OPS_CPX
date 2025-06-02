from application import app, db
from flask import render_template,flash, request, redirect
from .forms import Add_Instancia_Form, Mod_Instancia_Form, Instancia_Modelo_Form
from datetime import datetime
import time
import subprocess
import json 
from bson import ObjectId
import os

RUTA_AL_MODELO = '../OPS_CPX/emir_cpx'
RUTA_FICHERO_TMP = 'tmp.txt'
RUTA_INSTANCIA_TMP = 'fichero_instancia_tmp.txt'
RUTA_SALIDA_TMP = 'fichero_salida_tmp.txt'

RUTA_RESULTADOS_TMP = 'resultados_tmp.txt'

@app.route("/introduccion")
def introduccion():
    return render_template('introduccion.html') 

@app.route("/about")
def about():
    return render_template('about.html') 

# Por ahora mostrará los instancias y permitirá modificar su contenido o añadir nuevos 
@app.route("/", methods=["GET", "POST", "DELETE"])
def mostrar_instancias():    
    #Comprobamos si hemos recibido alguna solicitud especifica desde el front
    criterio_orden = request.args.get("criterio_orden", default="fecha")
    
    instancia_anteriormente_seleccionada = None
    instancias = []
    print("Criterio routes: " + criterio_orden)
    
    if(criterio_orden == 'nombre'):
        for instancia in db.Instancias.find().sort([("nombre", 1)]):
            #retocamos algunos datos como el id para que sean enviados como strings
            instancia["_id"] = str(instancia["_id"])
            instancia["nombre"] = str(instancia["nombre"])
            instancia = convert_objectid_to_str(instancia)        
            instancias.append(instancia)
    else:
        #damos por hecho que es por fecha
        for instancia in db.Instancias.find().sort([(criterio_orden, -1)]):
            #retocamos algunos datos como el id para que sean enviados como strings
            instancia["_id"] = str(instancia["_id"])
            instancia["nombre"] = str(instancia["nombre"])
            instancia = convert_objectid_to_str(instancia)        
            instancias.append(instancia)
    logs = obtener_logs()

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
        if "ejecutar_btn" in request.form :
            
            #Ejecutamos el modelo
            #ins = db.Instancias.find({"_id": ObjectId(request.form.get("id_instancia_a_probar"))}).next()
            #print(ins["contenido"])
            id_instancia_seleccionada = request.form.get("id_instancia_a_ejecutar")
            
            for instancia in instancias:
                
                #print("ID: " + instancia["_id"], )
                if instancia["_id"] == id_instancia_seleccionada:
                    instancia_anteriormente_seleccionada = instancia
                    print("routes.py, instancia_seleccionada previa _nombre:" + instancia_anteriormente_seleccionada["nombre"] + ", ")
                    print(type(instancia_anteriormente_seleccionada))
                    #flash("Se está ejecutando el modelo, porfavor tenga paciencia, el modelo puede tardar unos minutos. Una vez acabado se guardará en la instancia seleccionada","warning")
                    #Creamos ficheros temporales
                    f_tmp = open(RUTA_FICHERO_TMP, "w") #revisar si son nesesarios crearlo antes
                    # Escribir el diccionario en un fichero
                    with open(RUTA_INSTANCIA_TMP, 'w') as file:
                        json.dump(instancia["contenido"], file, indent=2)
                    f_salida = open(RUTA_SALIDA_TMP, "w") #revisar si son nesesarios crearlo antes
                    f_tmp.close()
                    f_salida.close()        

                    f_resultados = open(RUTA_RESULTADOS_TMP, "w") #revisar si son nesesarios crearlo antes         
                    f_resultados.close()

                    ejecutar_modelo(instancia["_id"],RUTA_AL_MODELO, RUTA_FICHERO_TMP, RUTA_INSTANCIA_TMP, RUTA_SALIDA_TMP, RUTA_RESULTADOS_TMP)
                    logs = obtener_logs()                    
                    
            #Para ello deberemos por ahora de crear una serie de ficheros temporales para pasarles el contenido al modelo                    
            return render_template('instancias.html', instancias= instancias ,form_mod_instancia = form_mod_instancia, form_instancia_modelo = form_instancia_modelo, logs = logs, instancia_anteriormente_seleccionada = instancia_anteriormente_seleccionada)
        
        print("Vamos a modificar una instancia")        
        form_mod_instancia = Mod_Instancia_Form(request.form)
        #necesitamos el id por ahora se me ocurre que se añada al form y que esté en oculto
        instancia_anteriormente_seleccionada_id = modificar_instancia(form_mod_instancia)
        
        #volvemos a obtener las instancias, ya que la informacion a cambiado, tal vez a futuro solo mod
        instancias = []
        if(criterio_orden == 'nombre'):
            for instancia in db.Instancias.find().sort([("nombre", 1)]):
                #retocamos algunos datos como el id para que sean enviados como strings
                instancia["_id"] = str(instancia["_id"])
                instancia["nombre"] = str(instancia["nombre"])
                instancia = convert_objectid_to_str(instancia)        
                instancias.append(instancia)
                if(instancia["_id"] == instancia_anteriormente_seleccionada_id):
                    instancia_anteriormente_seleccionada = instancia
        else:
            #damos por hecho que es por fecha
            for instancia in db.Instancias.find().sort([(criterio_orden, -1)]):
                #retocamos algunos datos como el id para que sean enviados como strings
                instancia["_id"] = str(instancia["_id"])
                instancia["nombre"] = str(instancia["nombre"])
                instancia = convert_objectid_to_str(instancia)        
                instancias.append(instancia)
                if(instancia["_id"] == instancia_anteriormente_seleccionada_id):
                    instancia_anteriormente_seleccionada = instancia
        logs = obtener_logs()          

    #instance_id = request.form.get('id_instancia_a_eliminar')
    return render_template('instancias.html', instancias= instancias ,form_mod_instancia = form_mod_instancia, form_instancia_modelo = form_instancia_modelo, logs = logs, instancia_anteriormente_seleccionada=instancia_anteriormente_seleccionada)

def obtener_logs():
    logs = []        
    for log in db.Logs.find().sort("nombre"):
        #retocamos algunos datos como el id para que sean enviados como strings
        log["_id"] = str(log["_id"])
        log["nombre"] = str(log["nombre"])
        
        log = convert_objectid_to_str(log)
        contenido_array = log.get("resumen_contenido", [])        
        log["resumen_contenido"] = '\n'.join(contenido_array)
        logs.append(log)
    return logs


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
        fecha_actual_texto = time.strftime('%d-%m-%Y_%H:%M:%S')    
        fecha_actual = datetime.strptime(fecha_actual_texto, '%d-%m-%Y_%H:%M:%S')        
        #pymongo flask, modificamos en la coleccion Instancias
        #ya que se modifica el contenido la fecha y el nombre se actualizarán  
        
        db.Instancias.find_one_and_update({"_id": ObjectId(identificador)}, {"$set": {
            "contenido": contenido_json,
            "fecha_texto" : fecha_actual_texto, 
            "fecha" : fecha_actual,

        }})
        
        #Mensaje al usuario
        flash("Instancia modificada correctamente", "success") # No veo que se muestre el mensaje revisar

        # Eliminamos el modelo referente a la instancia en cuestión si existe, para garantizar la correlacion de los datos
        eliminar_modelo_si_existe(identificador)
    except json.JSONDecodeError as e:
        # Manejo de errores en caso de que el contenido no sea un JSON válido
        flash(f"Error, el contenido no tiene el formato JSON correcto:\n {e}", "error")
    return identificador


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
            
            fecha_actual_texto = time.strftime('%d-%m-%Y_%H:%M:%S')   
            fecha_actual = datetime.strptime(fecha_actual_texto, '%d-%m-%Y_%H:%M:%S')
            #pymongo flask, insertamos en la coleccion Instancias
            db.Instancias.insert_one({
                "nombre" : add_instancia_nombre,
                "fecha_texto" : fecha_actual_texto, 
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
#### Diria que probar intancias template y todo sobran, ya que lo tengo todo dentro de la ruta instancia y instancias.html----------------------------------------------------------


#Función que ejecutará el modelo
def ejecutar_modelo(instancia_id, ruta_del_programa, *args):
    print("Vamos a ejecutar el modelo")
    #se la pasamos al modelo
    try:
        # Ejecutar el programa con los argumentos dados
        
        resultado = subprocess.run([ruta_del_programa, *args], capture_output=True, text=True)
        #resultado = subprocess.run(["pwd"], shell=True, capture_output=True, text=True)
        #resultado = subprocess.run([ruta_del_programa, "-h"], capture_output=True, text=True)
        print("Argumentos:" + str(resultado.args))
        #comprobamos que se ha generado la solución si el fichero está vacío mandamos error
        print("Fichero: " + str(args[2]))
        print("Tamañofichero vacio: " +str(os.stat(args[2]).st_size == 0))
        print("Tamañofichero vacio: " +str(os.stat(args[3]).st_size == 0))
        #Comprobamos el tamaño del fichero para saber si este se ha escrito
        if(os.stat(args[2]).st_size == 0):
            flash("Hubo un error al ejecutar el modelo, no salieron resultados, compruebe el contenido del fichero instancia:", "error")
            return f"No se ha podido ejecutar el modelo, comprueba el formato de la instancia"
        print(resultado.stdout)
        if(os.stat(args[3]).st_size == 0):
            flash("Hubo un error al ejecutar el modelo, no salieron resultados con los objetos resultantes, compruebe el contenido del fichero instancia:", "error")
            return f"No se ha podido ejecutar el modelo, no salieron resultados con los objetos resultantes, comprueba el formato de la instancia"
        print(resultado.stdout)
        #se entiende que si se ha llegado aquí todo ha ido bien
        
        flash("Se ha ejecutado el modelo de manera correcta","success")

        #Guardamos el modelo en la base de datos y eliminamos el modelo viejo si existiese
        guardar_resultados_modelo(instancia_id, str(args[2]), str(args[3]))
        #Mensaje al usuario
        flash("Modelo  ejecutado correctamente y guardado en la instancia correspondiente", "success") 
        return resultado.stdout  # O puedes retornar resultado si quieres incluir stderr y más información
    except subprocess.CalledProcessError as e:
        # Manejar el error si el programa falla
        print("fallo")
        flash("Hubo un error al ejecutar el modelo:", e)
        return f"Error: {e}"
    except Exception as e:
        print("fallo no conocido", e)
        flash("Hubo un error al ejecutar el modelo, probablemente la información de la instancia no es correcta", e)
        return f"Error: {e}"

def eliminar_modelo_si_existe(instancia_id):
    try:
        # Eliminar el documento cuyo _id sea igual al object_id
        result = db['Logs'].find_one_and_delete({"instancia_id": instancia_id})
        if result:
            print(f"Modelo eliminado: {id}")
            flash("Modelo eliminado/sustituido correctamente", "success")
            return True
        else:
            print(f"No se encontró ningun modelo con id: {id}")
    except Exception as e:
        print(f"Error al eliminar la modelo: {e}")    
    return False

    
def guardar_resultados_modelo(instancia_id, ruta_fichero_contenido, ruta_fichero_resultados):
    try:
        #obtenemos la información de la instancia utilizada
        object_id = ObjectId(instancia_id)
        #instancia_usada =  db.Instancias.find({"_id": object_id})
        instancia_usada = db.Instancias.find_one({"_id": object_id})
        
        #transformamos el contenido del fichero a JSON
        with open(ruta_fichero_contenido, 'r') as file:
            resumen_contenido = file.read().splitlines()
        
        
        nombre_modelo = instancia_usada.get("nombre") + "_" + str(instancia_usada.get("fecha_texto"))
        
        
        
        #contenido_json = json.loads(add_instancia_contenido)
        fecha_actual = time.strftime('%d-%m-%Y_%H:%M:%S')   
        #pymongo flask, insertamos en la coleccion Instancias
        

        with open(ruta_fichero_resultados, 'r') as archivo:
            resultados = json.load(archivo)

        # separamos la información recabada
        momento_seleccionado = resultados["momento_seleccionado"]
        valor_beneficio = resultados["valor_beneficio"]
        objetos_seleccionados = resultados["objetos_seleccionados"]

        #Eliminamos los modelos antiguos y guardamos el nuevo
        eliminar_modelo_si_existe(instancia_id)

        

        db.Logs.insert_one({
            "nombre" : nombre_modelo, 
            "fecha" : fecha_actual,
            "objetos_seleccionados" : objetos_seleccionados,
            "momento_seleccionado" : momento_seleccionado,
            "valor_beneficio" : valor_beneficio,
            "resumen_contenido" : resumen_contenido,
            "instancia_id" : instancia_id
        })
        
        return True
    except Exception as e:
        flash(f"Hubo un error al guardar el modelo en la base de datos: {e}", "error" )
        return f"Hubo un error al guardar el modelo en la base de datos: {e}"


    
    
# Eliminación de instancias
@app.route("/eliminar_instancia/<id>")
def eliminar_instancia(id):
    print("Eliminar instancia:" + str(id))            
    try:

        # Convertir id a ObjectId
        object_id = ObjectId(id)
        # Eliminar el documento cuyo _id sea igual al object_id
        result = db['Instancias'].find_one_and_delete({"_id": object_id})
        if result:
            print(f"Instancia eliminada: {id}")
            flash("Instancia eliminada correctamente", "success")
            #Eliminamos el resultado de la instancia en cuestión
            eliminar_modelo_si_existe(id)
        else:
            print(f"No se encontró ninguna instancia con id: {id}")
    except Exception as e:
        print(f"Error al eliminar la instancia: {e}")
    return redirect("/")

# Eliminación de modelos a partir de instancia
@app.route("/eliminar_modelo/<id>")
def eliminar_modelo(id):
    print("Eliminar modelo de la intancia con id:" + str(id))            
    eliminar_modelo_si_existe(id)
    return redirect("/")