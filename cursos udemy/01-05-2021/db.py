import mysql.connector
# mi db instancia de objeto con la base de datos
midb = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = '49717576',
    database = 'prueba',
)
# objeto que me permite interactuar con la base de datos mediante sql
cursor = midb.cursor()


# Listar Datos fetchall = todos  fetchone= el primer resultado
# cursor.execute('select * from usuario')
# resultado = cursor.fetchall()
# print(resultado)

# Listar solo un set de datos de la DB con limit
cursor.execute('select * from usuario limit 2')
resultado = cursor.fetchall()
print(resultado)


# Creando e Ingresando datos nuevos
# sql = 'insert into usuario (email,username,edad) values(%s,%s,%s)'
# values = ('micorreo@correo.com','nombreusuario',45)


# Update datos creados
# sql = 'update usuario set email = %s where id = %s'
# values = ('micorreo@correo.com.ar',5)
# cursor.execute(sql,values)
# midb.commit()


# Eliminar Datos
# sql = 'delete from usuario where id= %s'
# values = (3, ) # Importante poner coma y dejar espacio o tira error
# cursor.execute(sql,values)
# midb.commit()


# Script de como fue creada la tabla
# cursor.execute('show create table usuario')


# consultas y agregado de valores nuevos
# cursor.execute(sql, values)
# midb.commit()
# print(cursor.rowcount)




