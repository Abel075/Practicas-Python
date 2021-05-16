'''
Las tuplas son inmutables, no puedo eliminar ni modificar ninguno de los elementos en ellas.

'''

t = (1,3.6,4,7,'casa')

print(t[4])

print(len(t))

print(t[0:2])

l = [1,2,3,1]

t = ('uno','dos','tres')

#Convertir lista en tupla

l = tuple(l)
print(l)

#convertir una tupla a una lista

t = list(t)
print(t)

print(l.count(1))