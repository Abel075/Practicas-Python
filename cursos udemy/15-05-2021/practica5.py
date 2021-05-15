'''
Desarrolla una calculadora de enteros.
El programa debera pedir los operandos la usaurio y realizar las operaciones basicas. Suma, resta, multiplicacion y division. Controla las excepciones que se puedan producir.
'''
#Pedimos los datos
try:
    operando1 = int(input('introduce el primer operando\n'))
    operando2 = int(input('introduce el segundo operando\n'))
except:
    print('Los operandos no son validos. Se estableceran valores por defecto para los operandos.')
    operando1 = 1
    operando2 = 1

#Realizamos la operaciomnes
suma = operando1 + operando2
resta = operando1 - operando2
multiplicacion = operando1 * operando2
try:
    division = round(operando1 / operando2,2)
except:
    print('Error en la division')
    division = "Error"
#Mostramos la slida por pantalla
print(f'El resultado de la sumar el {operando1} y el {operando2} es {suma}')
print(f'El resultado de la restar el {operando1} y el {operando2} es {resta}')
print(f'El resultado de la multiplicar el {operando1} y el {operando2} es {multiplicacion}')
print(f'El resultado de la dividir el {operando1} y el {operando2} es {division}')