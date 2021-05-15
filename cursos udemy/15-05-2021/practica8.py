# Escibir un programa que muestre por pantalla los numeros pares entre 1 y 100

# Primera forma-Facil
for i in range(0,101,2):
    print(i)
    
# Segunda forma

for i in range(101):
    if i % 2 == 0:
        print(i)