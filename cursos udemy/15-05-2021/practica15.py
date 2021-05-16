'''
Desarrolla un programa que simule un traductor ingles-español.
Al iniciar el programa, aparecera un menu con las siguientes opciones.
1- Insertar palabra: Solicita al usuario una palabra en ingles y su traduccion en español y la añadira al diccionario.
2- Traducir texto: Solicitara al usuario un texto y mostrara por pantalla la traduccion del mismo.Las palabras que no se encuentren en el diccionario, las traducira como x.
3- Salir: La aplicacion finalizara.
'''

opcion = -1
diccionario = {}

while opcion != "3":
    opcion = input('Introduce alguna de las opciones\n1-Insertar palabra\n2-Traducir texto\n3-Salir\n')
    if opcion == "1":
        palabra = input('Introduce la palabra en ingles\n')
        traduccion = input(f'Introduce la traduccion a español de la palabra {palabra}\n')
        diccionario[palabra]= traduccion
    elif opcion == "2":
        texto = input('Introduce el texto que desea traducir')
        texto_traducido = ''
        lista_palabras = texto.split()
        for palabra in lista_palabras:
            if palabra in diccionario:
                traduccion = diccionario[palabra]
                texto_traducido += traduccion + ' '
            else:
                texto_traducido += 'X' + ' '
        print(texto_traducido)
    elif opcion != "1" and opcion != "2" and opcion != "3":
        print('Opcion incorrecta')
    
    
print('Traductor finalizado')
