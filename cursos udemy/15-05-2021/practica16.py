'''
Escribir un programa que pida un numero entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese numero donde n es el numero introducido.
'''


numero = int(input('Introduce un numero entre 1 y 10\n'))

if numero >= 1 and numero <= 10:
    nombre_fichero = 'tabla-' + str(numero) + '.txt'
    fichero = open(nombre_fichero,'w')
    
    # bucle para la tabla de multiplicar
    for i in range(1,11):
        x = numero *i
        fichero.write(str(x) + '\n')
    fichero.close()
else:
    print('Numero introducido incorrecto')


