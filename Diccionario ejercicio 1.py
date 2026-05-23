""" Desarrolle un programa que almacene datos de canciones en formato MP3: 

Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 

Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 

Debe interrumpirse la carga cuando el artista ingresado sea vacío. """

canciones = []

bandera = True

while bandera:
    artista = input("Ingrese el artista: ")

    if artista == "":
        bandera=False
    else:
        cancion = {}
        cancion["artista"] = artista
        cancion["titulo"]= input("Ingrese el titulo de la cancion: ")
        bandera2 = True
        while bandera2:
            duracion = input("Ingresar la duracion en segundos: ")
            try:
                esNumero = int(duracion)
                cancion["duracion"] = esNumero
                bandera2 = False
            except:
                print("La duracion tiene que ser en segundos")
        
        bandera3 = True
        while bandera3:
            tamanio = input("Ingresar el tamaño en kb de la cancion: ")
            try:
                esNumero = int(tamanio)
                cancion["tamanio"] = esNumero
                bandera3 = False
            except:
                print("El tamanio tiene que ser en kb")
        canciones.append(cancion)
        
for cancion in canciones:
    
    print(cancion)
    













