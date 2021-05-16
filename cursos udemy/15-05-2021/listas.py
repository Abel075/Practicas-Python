
lista=[1,4,5,'perro']

print(lista[3])

lista[1]=8.5

lista.append('gato')

print(lista)
print(lista.count('perro'))
print(lista.index('gato'))

lista.insert(2,'canario')
print(lista)

print(lista.pop())
lista.remove('perro')
print(lista)

#Mostrar el contenido de las listas

for elem in lista:
    print(elem)
    
for i in range(len(lista)):
    print(lista[i])