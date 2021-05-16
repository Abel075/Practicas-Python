'''
Open recibe dos parametros: la ruta del fichero y el modo de apertura
r : Para leer el fichero
w : Para escribir en el fichero
a : Append añadir al fichero
r+ : Leer y escribir
'''
# Abrir un fichero

fichero = open("prueba.txt",'a')

#Escribir ficheros
fichero.write('\nNueva linea')

fichero.close()
fichero = open("prueba.txt",'r')

#Lectura del contenido
contenido = fichero.readlines()

print(contenido)


#cerrar fichero
fichero.close()