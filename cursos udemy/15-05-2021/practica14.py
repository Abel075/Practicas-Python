'''
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El program debe preguntar el articulo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar(pulse tecla f).
Despues se debe mostrar por pantalla la lsita de la compra y el coste total, con el siguiente formato:
Lista de compras
Articulo1    Precio
Articulo2    Precio
Articulo3    Precio
....        .....
Total        Coste
'''

# Almacenamos los productos
producto = ''

#Creamos el diccionario
cesta = {}

while producto.lower() != 'f':
    producto = input('Indica el producto a comprar o pulsa f para salir\n')

    if producto.lower() != 'f':
        precio = float(input(f'Introduce el precio del producto {producto}\n'))
        cesta[producto] = precio

print('Lista de la compra')
suma = 0
for producto in cesta:
    precio = cesta[producto]
    suma += precio
    print(f'{producto}       {precio}')

print(f'Total       {suma}')