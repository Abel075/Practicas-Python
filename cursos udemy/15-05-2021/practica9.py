'''
Desarrolla un programa que solicite la carga de un numero al usuario.
A continuacion, debera pedir las notas de ese numero de alumnios, y mostrar ppor pantalla el numero de alummnos aprobados y suspensos.
'''
#Pedimos la cantidad de alumnos
numero = int(input('Introduce el numero de alumnos\n'))

#contadores de aprobados y suspensos
contador_aprobados = 0
contador_suspensos = 0

#Operamos segun la cantidad ingresada
for x in range(numero):
    nota = float(input(f'Introduce la nota del alumno {x+1}\n'))
    if nota >= 5:
        contador_aprobados +=1
    else:
        contador_suspensos +=1
print(f'El numero de aprobados es {contador_aprobados} y el numero de suspensos {contador_suspensos}')
    
    