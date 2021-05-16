'''
Desarrolla un programa que solicite constantemente la carga de un numero al usuario.
El programa finalizara caundo el usuario introduzca un 0, momento en el que se debe visualizaer la suma y el promedio de todos los numeros introducidos.
'''
suma = 0
numero = -1
contador = 0
while numero != 0:
    numero = int(input('Introduce un numero (0 para terminar)\n'))
    if numero != 0:    
        suma += numero
        contador += 1
promedio = round(suma / contador,2)

print(f'La suma de los numeros introducidos es {suma} y el promedio {promedio}')