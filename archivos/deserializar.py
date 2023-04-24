import pickle

# Modo de lectura pero binaria
with open("./Proyecto01/P01/archivos/archivoSerial","rb") as binFile:
    lista = pickle.load(binFile)

print(lista)
print("Archivo binario leido")