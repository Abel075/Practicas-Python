'''
Un diccionario es una estructura que almacena un conjunto de pares, en el cual unos de los valores es una clave y vamos a tener un valor asociado a esa clave
'''

dic = {'primera':7,'segunda':1.6,'tercera':'tres'}

print(type(dic))


print(dic['segunda'])

dic['segunda'] = [1,2,3]

print(dic)

#Eliminar todos los elementos de un diccionario

# dic.clear()
# print(dic)

#Tranformar un diccionario en lista y tuplas
print(dic.items())

#Mostrar las claves en un diccionario
print(dic.keys())
#Mostrar los valores en un diccionario
print(dic.values())

#Eliminar un valor
dic.pop('primera')
print(dic)

#Recorrer un diccionario

for x in dic:
    print(x)
    
for x in dic:
    print(dic[x])
