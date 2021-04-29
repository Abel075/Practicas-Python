# # # 1

# # def funcion():

# #     contador = 0

# #     while contador<5:
# #         # print(contador)

# #         contador += 1

# #         if (contador == 4):
# #             print('Se rompio')
# #             break
# #         print(contador)


# # funcion()

# frutas = ['Kiwi', 'mango', 'cereza']

# for fruta in frutas:
#     print(fruta)


# 1-----

# num = input('Ingrese un numero: ')

# print('Usted ingreso: ',num)

# 2-----

# lado1 = int(input('Ingrese lado 1: '))
# lado2 = int(input('Ingrese lado 2: '))

# area = lado1*lado2
# perimetro = (lado1*2)+(lado2*2)

# print('Area: ', area ,'\nPerimetro: ', perimetro)

# 3----

# num1 = int(input('Ingrese el primer numero: '))
# num2 = int(input('Ingrese el segundo numero: '))

# suma = num1+num2
# resta = num1-num2
# multiplicacion = num1*num2
# divisionEntera = num1//num2
# divisionReal = num1/num2

# print('La suma es: ', suma,
#     '\nLa resta es:' ,resta,
#     '\nLa multiplicacion es:', multiplicacion,
#     '\nLa division entera es: ',divisionEntera,
#     '\nLa division real es: ',divisionReal)

# 4-----

# num1 = float(input('Ingrese un numero real: '))

# parteDecimal =num1-(int(num1))
# parteEntera=num1-parteDecimal

# print('Parte entera: ',parteEntera, '\nParteDecimal: ', round(parteDecimal,2))

# 5----2.1

# def convertir(valorSeg):

#     segXdia =24*60*60  # hh*mm*ss -- cant. de seg x dia
#     segXhora=60*60     # mm*ss -- cant. de seg x hora
#     segXmin=60         # ss -- cant. de seg x min

#     dias = valorSeg // segXdia      # Dias que entran en valor segundos
#     valorSeg = valorSeg % segXdia   # valor segundos restantes por dia
#     horas = valorSeg // segXhora    # Horas que entran en valor segundos
#     valorSeg = valorSeg % segXhora  # valor segundos restantes por hora
#     minutos = valorSeg // segXmin   # Minutos que entran en valor segundos
#     valorSeg = valorSeg % segXmin   # valor segundos restantes por minuto
#     segundos = valorSeg

#     print(dias, 'dia(s)', horas, 'hora(s)', minutos, 'minuto(s)', segundos,'segundo(s)')

# def main():
#     print('Ingrese tiempo en segundos: ', end="")
#     valor = int(input())
#     convertir(valor)

# main()

# 6----


# def ingresarInt(msj):
#     print(msj,end="")
#     return int(input())

# def producto(num1,num2):
#     u = num2%10
#     d = (num2//10)%10
#     c = (num2//100)%10
#     prod = num1*num2

#     print("{:10d}".format(num1))
#     print("x{:>9d}".format(num2))
#     print("{:->10s}".format(""))
#     print("{:10d}".format(num1*u))
#     print("{:=+9d}{:->1}".format((num1*d),""))
#     print("{:>8d}{:->2}".format((num1*c),""))
#     print("{:->10s}".format(""))
#     print("{:10d}".format(prod,""))


# def main():
#     num1 = ingresarInt('Ingrese el multiplicando: ')
#     num2 = ingresarInt('Ingrese el multiplicando: ')
#     producto(num1,num2)


# main()

# 7---

# from math import pi

# def areaCirc(radio):
#     return pi*(radio**2)

# def areaCuad(lado):
#     return lado*lado

# def areaBlanca(lado):
#     radioChi = (lado/3)/2
#     radioGra = ((lado/3)*2)/2
#     aCirc = 2*(areaCirc(radioChi))+ areaCirc(radioGra)
#     return aCirc
# def areaNegra(lado):
#     aBlanca = areaBlanca-(lado)
#     aCuad = areaCuad(lado)
#     aNegra = areaCuad - aBlanca
#     return aNegra

# def main():
#     print('Ingrese el lado: ', end="")
#     lado = float(input())
#     aNegra = areaNegra(lado)
#     aBlanca = areaBlanca(lado)
#     aNegraPorc = (aNegra/(aBlanca+aNegra))*100

#     aNegraStr = "{:.2f}".format(aNegra)
#     aNegraPorcStr = "{:.2f}".format(aNegraPorc)
#     print("")
#     print("El area negra es: ", aNegraStr, end="")
#     print(" y es un " + aNegraPorcStr + "% del area total del cuadrado", end="")

# main()

# Dibujar----

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if f<=c and f+c>=b-5 or  f>=c and f+c<=b-1:
#                 print(con,end="")
#             else:
#                 print(esp,end="")
#         print()

# def main():
#     dibujar(7,'/','')

# main()


# cuadrado vacio

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if f==0 or f==b-1 or  c==0 or c==b-1:
#                 print(con,end="")
#             else:
#                 print(esp,end="")
#         print()
        


# cuadrado relleno

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if True:
#                 print(' '+ con,end="")
#             else:
#                 print(' ' +esp,end="")
#         print()


# escalera hacia abajo

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if f >= c :

#                 print(' ' + con,end="")
#             else:
#                 print(' '+esp,end="")
#         print()



# espejado

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if (f<=c and f+c <=b-1) or (f>=c and f+c >=b-1) :

#                 print(' ' + con,end="")
#             else:
#                 print(' '+esp,end="")
#         print()


# el hacha

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if c== b//2 or f==b//2 or (f<=c and f+c <=b-1):

#                 print(' ' + con,end="")
#             else:
#                 print(' '+esp,end="")
#         print()





# rombo completo

# def dibujar(b,con,esp):
#     for f in range(0,b):
#         for c in range(0,b):
#             if c<=f+(b//2) and c>=f-(b//2) and c+f<=b-1+(b//2) and c+f>=b-1-(b//2):

#                 print(' ' + con,end="")
#             else:
#                 print(' '+esp,end="")
#         print()


# rombo vacio

def dibujar(b,con,esp):
    for f in range(0,b):
        for c in range(0,b):
            if c==f+(b//2) or c==f-(b//2) or c+f==b-1+(b//2) or c+f==b-1-(b//2) :

                print(' ' + con,end="")
            else:
                print(' '+esp,end="")
        print()


def main():
    dibujar(9,'*',' ')

main()



