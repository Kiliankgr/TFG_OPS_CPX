# TFG_OPS_CPX
## Compilación
Para la compilación del proyecto es necesario una serie de pasos previos
* La instalación de la librería **cplex_studio2211**
* Modificación de los ficheros src/model/CMakeList.txt y src/main/CMakeList.txt modificando la ruta donde se encuentra la instalación de la librería
* Creación de un nuevo build, crear directorio build y ejecutar **cmake ../src/**
* **cmake --build <ruta_directorio_build>**, donde se creará el ejecutable en **<directorio_build>/main/emir_cpx**


## Desarrollo Web
El desarrollo de la web será realizado mediante el uso de **Flask** un framework de Python.
### Instalación - Puesta a punto
* Instalar python (version actual python3.10.2)
* **sudo apt install python3.10-venv**
* Creación de entorno **python3 -m venv venv**
* Activar entorno **. venv/bin/activate**
* 

## Base de datos
Se usará MongoDB, con PyMongo el cual da servicio a nuestra Web hecha en Flask
### Instalación realizada de PyMongo
* MongoDB Atlas cluster [tutorial](https://www.mongodb.com/docs/atlas/getting-started/?_ga=2.90501273.2090826799.1716903787-609048103.1716903786&_gac=1.217694626.1716903787.EAIaIQobChMI7Yba-rywhgMVmKloCR0ckgIpEAAYASAAEgLMrPD_BwE)
* **python3 -m pip install python-dotenv Flask-PyMongo Flask-PyMongo pymongo[srv]**

## Notas 
* Actualmente está testeado con el fichero ubicado en "/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/test_ins.txt" se modificará a posteriori para pasarlo por argumentos
* Se creará un fichero .log con los resultados de la ejecución .

## TO DO
* Manejo de errores
* Eliminación de Logs .
* Añadir elementos al home
* Descargar elementos
* Interfaz modelo-instancia
* Retocar el diseño de los modelos para la instancia, arreglar tambié que el texto de las instancias puede producir un overflow y salir del contenedor
* Guardar modelos en la base de datos
* Permitir arrastrar ficheros para añadir instancias( hecho)


## References
[](https://flask.palletsprojects.com/en/3.0.x/)
[](https://flask.palletsprojects.com/en/3.0.x/deploying/)
[](https://docs.python.org/es/3.8/library/venv.html)
[](https://www.mongodb.com/resources/products/compatibilities/setting-up-flask-with-mongodb)
[](https://wtforms.readthedocs.io/en/2.3.x/)
[](https://getbootstrap.com/docs/4.0/)