'''
Escribir un programa que solicite la entrada de una oracion al usuario y devuelva el numero de espacios en blanco que contiene
'''

oracion = input('Introduce una oracion\n')

contador=0
#Metodo 1
'''
for caracter in oracion:
    if caracter == " ":
        contador +=1
        
'''     
#Metodo 2
for x in range(len(oracion)):
    if oracion[x] == " ":
        contador += 1

print(f'El numero de espaciose en blaco son {contador}')