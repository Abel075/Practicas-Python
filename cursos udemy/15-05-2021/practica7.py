'''
De un operario se conoce su sueldo y los años de antiguedad.
Confecciona un programa que lea dichos datos del teclado y realize los siguiente:
Si el sueldo es inferior a 500 y su antiguedad es igual o superior a 10 años, otorgarle un aumento de 20%.
Si el sueldo es inferior a 500 pero su antiguedad menor a 10 años, otorgarle un aumento de 5%.
Si el sueldo es mayor o igual 500 mostrar el sueldo en pantalla sin cambios.
'''

#Pedimos los datos
sueldo = int(input('Introduce el sueldo del empleado\n'))
antiguedad = int(input('Introduce la antiguedad del empleado\n'))

#Realizamos la operacion
if sueldo < 500 and antiguedad >= 10:
    sueldo += 0.2*sueldo
elif sueldo < 500 and antiguedad < 10:
    sueldo += 0.05*sueldo

#Mostramos los datos
print(f'El sueldo final del empleado es: {sueldo}')

