'''Escibe un programa que pida al usuario los grados centigrados que quiere convertir y muestre en pantalla la equivalencia con grados kelvin y grados farenheit
ºk = 273 + ºC 
ºK = 1,8*ºC +32
'''
try:
    centigrados = int(input('Introduce los grados centigrados que quieres convertir\n'))
except:
    print('Los grados centigrados introducidos no son correctos. Se creara una cantidad de grados por defecto')
    centigrados = 20
kelvin = 273 + centigrados
farenheit = 1.8 * centigrados + 32

print(f'{centigrados} equivalen a {kelvin} grados kelvin y a {farenheit} grados farenheit')

