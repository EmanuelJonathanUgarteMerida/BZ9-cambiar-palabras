fichero = open('fichero.txt', 'r')
original = fichero.read()
fichero.close()
nueva = original.replace('tizas', 'yesos')


fichero= open('fichero.txt','w')
fichero.write(nueva)
fichero.close()
