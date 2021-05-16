'''
Escribir una funcion que reciba como parametros una lista y un numero.
La funcion debe multiplicar cada elemento de la lista por el numero y devolver la lista resultante.
'''

def multiplica_lista_x_numero(lista,numero):
    for x in range(len(lista)):
        lista[x] = lista[x] * numero
        
    return lista

lista = [1,2,3,4,5,6]
numero = 7
resultado = multiplica_lista_x_numero(lista,numero)

print(resultado)