'''
Escribir un programa que solicite dos fechas al usuario con el formato dd/mm/yy.
A continuacion debe crear dos tuplas y almacenar el dia, mes y año de las fechas en dichas tuplas.
Por ultimo, tiene que mostrar cual de las fechas es la mas reciente.
'''

# Solicitamos las fechas al usuario
fecha1 = input('Introduce la primera fecha con formato dd/mm/yy\n')
fecha2 = input('Introduce la segunda fecha con formato dd/mm/yy\n')

#Creamos las tuplas para almacenar
lista_fecha1 = fecha1.split('/')
#tupla 1
tupla1 = tuple(lista_fecha1)

#tupla 2
tupla2 = tuple(fecha2.split('/'))

# Mostromos cual de las fechas es mas reciente

dia1 = int(tupla1[0])
mes1 = int(tupla1[1])
año1 = int(tupla1[2])

dia2 = int(tupla2[0])
mes2 = int(tupla2[1])
año2 = int(tupla2[2])

if año1 > año2:
    print('Fecha mas reciente: ' + fecha1)
elif año2 > año1:
    print('Fecha mas reciente: ' + fecha2)
else:
    if mes1 > mes2:
        print('Fecha mas reciente: ' + fecha1)
    elif mes2 > mes1:
        print('Fecha mas reciente: ' + fecha2)
    else:
        if dia1 > dia2:
            print('Fecha mas reciente: ' + fecha1)
        elif dia2 > dia1:
            print('Fecha mas reciente: ' + fecha2)
        else:
            print('Las fechas son iguales')
            
            
        
    