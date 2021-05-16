'''
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float).
Obtener el promedio de las mismas.
Contar cuantas personas son mas altas que el promedio y cuantas mas bajas.
'''
# Creamos un bucle para pedir los datos 5 veces

alturas = []
suma = 0
for i in range(5):
    altura = float(input(f'Ingrese la altura de la persona {i+1}\n'))
    alturas.append(altura)
    suma += altura
    
promedio = round(suma / 5,2)

contador_mayor_promedio = 0
contador_menor_promedio = 0
for altura in alturas:
    if altura > promedio:
        contador_mayor_promedio += 1
    else:
        contador_menor_promedio += 1
print(f'Hay {contador_mayor_promedio} personas con altura mayor que el promedio y {contador_menor_promedio} con altura menor al promedio')
    
