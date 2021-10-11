import sys
import os

argumentos = sys.argv
# Si la lista longitud de sys.argv es menor de cuatro terminamos, de lo contrario calcular

if len(argumentos) == 4:

    _FICHERO = argumentos[1]
    palabraOriginal = argumentos[2]
    palabraNueva = argumentos[3]
    # verificamos si existe el archivo
    if os.path.isfile(_FICHERO):
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
else:
    print("Ayuda")
    print("\tpython cambia palabras.py <nombrefichero> <textoOriginal> <textoNuevo>")
