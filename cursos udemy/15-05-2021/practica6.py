#Escibir un programa que pida las tres notas de un alumno. Si el promedio es mayor o igual a 5, mostrat un mensaje "Promocionado"

#Pedimos los datos
nota1 = float(input('Ingrese la primera nota\n'))
nota2 = float(input('Ingrese la segunda nota\n'))
nota3 = float(input('Ingrese la tercera nota\n'))

#Realizamos las operacion
promedio = (nota1 + nota2 + nota3)/3

if promedio >= 5:
    print('PROMOCIONADO')
else:
    print('NO PROMOCIONADO')
