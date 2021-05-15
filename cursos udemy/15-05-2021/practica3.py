#Escribe un programa que pida al usuario el radio de un circulo y calcule su area, sabiendo que: Area = pi*r^2

radio = float(input('Introduce el radio del circulo\n'))
pi = 3.14

area = round(pi* pow(radio,2),2)

print(f'El area del circulo de radio {radio} es {area}')
