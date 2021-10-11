import sys

_FICHERO = sys.argv[1]
palabraOriginal = sys.argv[2]
palabraNueva = sys.argv[3]
fichero = open(_FICHERO, 'r')
original = fichero.read()
fichero.close()
nueva = original.replace(palabraOriginal, palabraNueva)


fichero = open(_FICHERO, 'w')
fichero.write(nueva)
fichero.close()
