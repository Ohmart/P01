''' El archivo se va a crear donde se esté ejecuntando el intérpre
de Python, en este caso la carpeta que agregué es "Proyectos" '''

import sys
import os
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__),('..')))
sys.path.append(lib_path)
from fundamentosPython import nuevoTema

# Abrir el archivo en modo escritura
file = open("ejemploArchivo.txt",  "w")
# Grabar en el archivo
file.write("Este es el contenido del archivo.\n")
# Cerrar el archivo
file.close() 

lista = ["Fresa", "Mango", "Papaya"]
# Abrir el archivo en modo escribir al final
with open("ejemploArchivo.txt",  "a") as file:
    for e in lista:
        file.write(e + "\n")

lista2 = ["Honda ", "Suzuki ", "BMW "]
with open("ejemploArchivo.txt",  "a") as file:
        #Ya no es necesario agregar for
        file.writelines(lista2)

nuevoTema("Imprimir el contenido del archivo:")
# Abrir el archivo en modo lectura
with open("ejemploArchivo.txt",  "r") as file:
        print(file.read())

nuevoTema("Leer 2 y lineas y 3 caracteres de la 3ra línea:")
with open("ejemploArchivo.txt",  "r") as file:
        print(file.readline())
        print(file.readline())
        print(file.readline(3))

nuevoTema("Guardar el contenido del archivo en una lista:")
with open("ejemploArchivo.txt",  "r") as file:
    contenido = file.readlines()
    print(contenido)

nuevoTema("Muestra la última líea del archivo en una lista:")
with open("ejemploArchivo.txt",  "r") as file:
    contenido = file.readlines()
    print(contenido[-1])