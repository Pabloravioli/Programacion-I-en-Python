""" Desarrolle un programa que almacene datos de canciones en formato MP3: 

Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 

Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 

Debe interrumpirse la carga cuando el artista ingresado sea vacío. """

canciones = []

bandera = True

while bandera:
    artista = input("Ingrese el artista")

    if artista == "":
        bandera=False
    else:
        cancion = {}
        cancion["artista"] = artista
        cancion["titulo"]= input("Ingrese el titulo de la cancion")
        cancion["duracion"] = input("Ingresar la duracion en segundos")
        cancion["tamanio"] = int(input("Ingresar el tamañño en kb de la cancion"))
        canciones.append(cancion)


for cancion in canciones:
    print(cancion["titulo"], "-",cancion["Artista"], ""


