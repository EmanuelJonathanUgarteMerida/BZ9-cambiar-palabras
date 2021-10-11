_FICHERO = 'fichero.txt'
palabraOriginal = 'yesos'
palabraNueva = 'tizas'
fichero = open(_FICHERO, 'r')
original = fichero.read()
fichero.close()
nueva = original.replace(palabraOriginal, palabraNueva)


fichero = open('fichero.txt', 'w')
fichero.write(nueva)
fichero.close()
