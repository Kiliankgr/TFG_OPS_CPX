# Programa para trasforma los fichero txt a json
import json, sys

# Lee el contenido del archivo .txt luego lo modifiaremos para que sea por conosla y lo haga a un fichero o a un directorio

if (len(sys.argv) < 2 ):
    print( "hace falata especificar la ruta de un fichero o directorio")
    exit(1)

if (sys.argv.__contains__("-h")):
    print("Formato de uso: python3 log_files_to_json <ruta_fichero_o_directorio")
    exit(1)

#TO DO falta implementar que formatee todos los ficheros de un directorio    
print(sys.argv)
ruta = sys.argv[1]

filename = ruta.split("/")[-1]
print ( filename)
with open(ruta, 'r') as file:
    lines = file.readlines()

# Procesa las líneas 
TEXT_LINE_ID = "linea"    
contador_linea = 1
contenido = {}

for line in lines:
    key = TEXT_LINE_ID + str(contador_linea)
    value = line
    contenido[key] = value
    contador_linea = contador_linea + 1

datos = {
    "nombre": filename,
    
    "contenido": contenido
}    


# Escribe el diccionario en un archivo .json

with open(ruta.split(".")[0] + ".json", 'w') as json_file:
    json.dump(datos, json_file, indent=4)

print(f"Contenido del {ruta} transformado a .json")