
cadena='Esto es una cadena'

print(cadena.count('a'))
print(len(cadena))
print(cadena.index('de'))


cadena1 = '3445'
print(cadena1.isdigit())

print(cadena.lower())
print(cadena.upper())

print(cadena.replace('una','dos'))

#Devuelve una lista con cada palabra como elemento
print(cadena.split())
#Se pude separar cada palabra pasando parametros
print(cadena.split('a'))

'''
Las cadenas se recorren a traves de bucles
'''
for caracter in cadena:
    print(caracter)
    
for i in range(len(cadena)):
    print(cadena[i])