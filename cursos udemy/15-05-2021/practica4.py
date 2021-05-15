'''Escibe un programa que pida al usuario los grados centigrados que quiere convertir y muestre en pantalla la equivalencia con grados kelvin y grados farenheit
ºk = 273 + ºC 
ºK = 1,8*ºC +32
'''

centigrdos = int(input('Introduce los grados centigrados que quieres convertir\n'))
kelvin = 273 + centigrdos
farenheit = 1.8 * centigrdos + 32

print(f'{centigrdos} equivalen a {kelvin} grados kelvin y a {farenheit} grados farenheit')