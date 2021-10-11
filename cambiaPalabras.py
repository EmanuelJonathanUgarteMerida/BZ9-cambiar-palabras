import os
import sys

argumentos = sys.argv



_FICHERO = input("Fichero: ")

# verificamos si existe el archivo
if os.path.isfile(_FICHERO):
    palabraOriginal = input("Palabra vieja: ")
    palabraNueva = input("Palabra nueva: ")
    fichero = open(_FICHERO, 'r')
    original = fichero.read()
    fichero.close()
    nueva = original.replace(palabraOriginal, palabraNueva)

    fichero = open(_FICHERO, 'w')
    fichero.write(nueva)
    fichero.close()
    print("Listo!")
else:
    print("No existe el fichero {} en el directorio".format(_FICHERO))
