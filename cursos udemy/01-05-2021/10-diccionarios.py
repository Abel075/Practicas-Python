#Creando diccionarios

cancion = {

    'artista': 'Metallica', #llave y valor
    'cancion': 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3000
}

print(cancion['artista'])
print(cancion['lanzamiento'])

#mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

print(cancion)

#Agregar nuevos valores

cancion['playlist'] = 'Heavy Metal'
print(cancion)


#Reemplazar valor existente

cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#Eliminar un valor
del cancion['lanzamiento']
print(cancion)