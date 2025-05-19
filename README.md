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


## TO DO
* Manejo de errores
* Añadir interfaz con los nuevos datos
* Sustituir los mensajes de ejecución del algoritmo por una "pantalla de carga", bloquear la ventana web mientras.
* Mostrar instancia, el texto de los nombres de instancia no deberían de sobresalir
* Remodelar la interfaz de instancias, no me termina de convencer el text area de modificar, tal vez lo de modificar que sea un pop up y alli se modifica, recolocar botones, añadir un filtro/buscador (dos opciones en esa misma interfaz o, modificamos la interfaz, quitamos la columna que muestra todos las intancias y añadimos un botoón  de seleccion que nos muestre todas las intancias en una ventana tipo como explorador de archivos).
* Añadir transiciones o efectos a la hora de seleccionar ciertos elementos

##

* Arreglar base de datos tiempo cambiar a coste beneficio (hecho)
* Cambiar el mensaje de carga, sutituir con un pop up de un modal /// ó /// bloquear solo los botones 
* Arreglar front instancias overflow del texto (hecho)

## REVISION
Plantearse en un futuro eliminar el texto de Instancias en la pestaña de mostrar instancias

##
Añadir  instancia (hecho).
Responsive (Hecho).
(Para hacer ahora) utitlizar el span en lugar del p( para que no estén los espacios) (hecho)
Alto del TexArea de añadir instancias igual al de añadir instancia.(hecho)
Reestructurar el formato de la fecha (que se vea con el formato nuestro DD--MM--YY) (hecho)
Ordenar instancias por fecha. (hecho)

Añadir un botón que permita cambiar el orden de mostrar instancias por nombre o por fecha más reciente.
Al probar la instancia, revisar el reenvío de formulario, que mantenga la instancia seleccionada si hubiese una (Importante, pero no realizar ahora).
Sustituir el contenido de About por un manual, que explique el funcionamiento de la aplicación.
Intercambiar la pestaña de OPS_CPX(Inicio) por el contenido de "instancias" , en el contenido de instancias se quedará el conetenido que hay al inicio (sutituir nombre de instancias por algo más adecuado).
Ajustar el overflow del nombre del modelo al recuadro.
Añadir una guía de usuario
Permitir un modo oscuro a la web(No tan prioritario).
Solucionar espacios entre líneas en la información del contenido (Se ven espacios más grandes entre líneas).
Número de línea, al ver el contenido (Muy opcional, ya para el final)


## Funcionamiento del OPS
* Se le pasan el fichero con la instancia y el fichero con la salida, así como un fichero temporal. 
* El programa genera un objeto con la información de la instancia con el fichero de instancia (OPS_instance)
* Dicho objeto se le entrega al OPS_input, donde genera la estructura a partir de la información


## References
[](https://flask.palletsprojects.com/en/3.0.x/)
[](https://flask.palletsprojects.com/en/3.0.x/deploying/)
[](https://docs.python.org/es/3.8/library/venv.html)
[](https://www.mongodb.com/resources/products/compatibilities/setting-up-flask-with-mongodb)
[](https://wtforms.readthedocs.io/en/2.3.x/)
[](https://getbootstrap.com/docs/4.0/)