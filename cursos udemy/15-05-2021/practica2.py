#Escribe un programa que pida al usuario 3 palabras y las muestre en consola separadas por guiones.

#Le pedimos al usuario que ingrese los datos y ls guardamos en variables
palabra1 = input('Ingrese la primera palabra\n')
palabra2 = input('Ingrese la segunda palabra\n')
palabra3 = input('Ingrese la tercera palabra\n')


#Salida de informacion

#primera forma
# print(f"{palabra1}-{palabra2}-{palabra3}")

#Segunda forma
# print("{}-{}-{}".format(palabra1,palabra2,palabra3))

#Tercera forma - solo si son cadenas
print(palabra1+"-"+palabra2+"-"+palabra3)
