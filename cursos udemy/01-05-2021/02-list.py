lenguajes = ['Python','Kotlin']
print(lenguajes[0])

aprendiendo = f'Estoy aptendiendo {lenguajes[0]}'
print(aprendiendo)

#modificando valores de un arreglo
lenguajes[1] = 'Php'
print(lenguajes)

#Agregar elementos a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

#eliminar de una arreglo  le  

del lenguajes[1]
print(lenguajes)

#eliminar de un arreglo el ultimo elemento o una posicion
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('Ruby')
print(lenguajes)