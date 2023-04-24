import pickle

info = [35, 88, 3.14, 16]

# Modo de escritura pero binaria
with open("./Proyecto01/P01/archivos/archivoSerial","wb") as binFile:
    pickle.dump(info, binFile)

print("Archivo binario escrito")