'''
Desarrollar una aplicacion para la gestion de empleados de una empresa.
La aplicacion mostrara un menu con las siguientes opciones:
1- inicializar: Creara la base de datos y la tabla(si no existen) donde almacenar los empleados.
2- insertar empleado: Pedira dni, nombre y apellidos, edad y departamento y realizara la insercion del empleado en la base de datos.
3- Consultar: Pedira el dni del empleado y mostrar sus datos.
4- Finalizar: Saldra de la aplicacion.
'''

import pymysql
from pymysql import cursors

def inicializar():
    conexion = pymysql.connect(host="localhost",user="root",passwd="49717576")
    
    cursor = conexion.cursor()

    sql = "CREATE database if not exists practica21"
    cursor.execute(sql)

    sql = "USE practica21"
    cursor.execute(sql)
    
    sql = "CREATE table if not exists empleado(dni varchar(10), nombre varchar(255), edad smallint, departamento varchar(255))"
    cursor.execute(sql)

    conexion.close()

    #Insertar empleados
    
def insertar_empleados(dni,nombre,edad,departamento):
    conexion = pymysql.connect(host="localhost",user="root",passwd="49717576",database="practica21")
    
    cursor = conexion.cursor()
    
    sql = "INSERT into empleado(dni,nombre,edad,departamento) values('" + dni + "', '" + nombre + "'," + str(edad) + ",'" + departamento + "')"
    cursor.execute(sql)
    
    conexion.commit()
    conexion.close()

# Consultar 

def consultar_empleados(dni):
    conexion = pymysql.connect(host="localhost",user="root",passwd="49717576",database="practica21")
    cursor = conexion.cursor()
    
    sql = "SELECT * from empleados where dni = '" + dni + "'"

    cursor.execute(sql)

    filas = cursor.fetchall()

    if len(filas) == 0:
        print('Empleado no encontrado')
    else:
        for fila in filas:
            print(f'Empleado con dni {fila[0]}, de nombre {fila[1]} y edad {fila[2]}, trabaja en el departamento {fila[3]}')
    
    conexion.close()
    

opcion = -1

while opcion !=4:
    opcion = int(input('Introduce alguna de las opciones siguientes:\n1-Inicializar base de datos\n2-Insertar empleado\n3-Consultar empleado\n4-Salir\n'))
    
    if opcion == 1:
        inicializar()
    elif opcion == 2:
        dni = input('Introduce dni\n')
        nombre = input('Introduce nombre y apellido\n')
        edad = int(input('Introduce edad\n'))
        departamento = input('Introduce departamento\n')
    elif opcion == 3:
        dni = input('Introduce dni\n')
        consultar_empleados(dni)
    elif opcion != 1 and opcion != 2 and opcion !=3 and opcion != 4:
        print('Opcion seleccionada no valida')