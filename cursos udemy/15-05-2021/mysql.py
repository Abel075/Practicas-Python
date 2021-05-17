import pymysql

# Funcion para insertar datos

def insertar_datos(campo1,campo2):
    conexion = pymysql.connect(host='localhost',user='root',passwd='49717576',database='prueba')
    
    #Simpre crear un cursor para realizar las operaciones
    
    cursor = conexion.cursor()

    sql = "INSERT into tabla1(campo1,campo2) values(" + str(campo1) + ",'" + campo2 + "')"
    
    cursor.execute(sql)
    conexion.commit()
    
    conexion.close()

def actualizar_datos(campo1,campo2):
    conexion = pymysql.connect(host='localhost',user='root',passwd='49717576',database='prueba')
    cursor = conexion.cursor()
    
    sql = "UPDATE tabla1 set campo2 = '" + campo2 + "' where campo1 = " + str(campo1)
    
    
    cursor.execute(sql)
    conexion.commit()
    
    conexion.close()
    
    
def eliminar_datos(campo1):
    conexion = pymysql.connet(host='localhost',user='root',passwd='49717576',database='prueba')
    cursor = conexion.cursor()
    
    sql = "DELETE from tabla1 where campo1 = " + str(campo1)
    
    cursor.execute(sql)
    conexion.commit()
    
    conexion.close()

def seleccionar_datos():
    conexion = pymysql.connet(host='localhost',user='root',passwd='49717576',database='prueba')
    cursor = conexion.cursor()
    
    sql = "SELECT * from tabla1"
    cursor.execute(sql)
    filas = cursor.fetchall()
    
    for fila in fila:
        print (str(fila[0]) + " " + fila[1])

    conexion.close()

insertar_datos(1,"valor 1")
insertar_datos(2,"valor 2")
insertar_datos(3,"valor 3")
actualizar_datos(2,"valor1000")
eliminar_datos(3)
seleccionar_datos()
    
    
      
    