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

## Notas 
* Actualmente está testeado con el fichero ubicado en "/home/kilian/Escritorio/TFG/Proyecto/OPS_CPX/test_ins.txt" se modificará a posteriori para pasarlo por argumentos
* Se creará un fichero .log con los resultados de la ejecución


## References
![](https://flask.palletsprojects.com/en/3.0.x/)
![](https://flask.palletsprojects.com/en/3.0.x/deploying/)