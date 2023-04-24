# Este programa agrega la ruta inmediata superior de la ubicación
#  del archivo actual
import sys
import os

print(sys.path)

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__),('..')))
sys.path.append(lib_path)

print(sys.path)

from fundamentosPython import nuevoTema
import calc.operaciones as c

if __name__ =="__main__":
    nuevoTema("Módulos y paquetes")
    print(c.suma(5,2))
    print(c.resta(5,2))
    print(c.mult(5,2))
    print(c.div(5,2))