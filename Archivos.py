#Archivos


"""
Conjunto de elementos llamados registros

juan perez, 18, Boca Juniors

Camila Pereyra, 28, River Plate




Abrir archivo open

Tipos de apertura:

    r leer
    
        Si el archivo no existe al leerlo da error

    w escribir
    
        Si el archivo no existe al escribir crea uno y si existe lo destuye y crea uno nuevo

    a agregar
    
        Si el archivo existe agregar mas cosas alfinal


para escribir contrabarra (\) es alt + 92


IMPORTANTE Otra de las tantas maneras de acceder a la ruta del archivo

try:

import os   // es un modulo de bibliotecas que permite trabajar con archivos interactuar con el sistema operativo

ruta actual = os.path.dirname(__file__)  // obtengo la ruta actual

print(ruta_actual)

ruta_archivo = os.path.join(ruta_actual, "letras.txt") // Le agrega al nombre del archivo el .txt ejemplo letras.txt

whith open(ruta_archivo, "r" ) as archivo:    //  CON WITH OPEN EVITO DE USAR FINALLY
    registros = archivo read()   //NO USAR READ SI EL ARCHIVO ES GRANDE

archivo = open(ruta_archivo, "r")

archivo.write(string) - el salto de linea se añade manualmente

archivo.writeline(listaDeCadenas) -El salto de linea se tiene que agregar a cada elemento


except:
    print("Error")


Manipular archivo write print

cerrar archivo close 







"""


archivo = open("jugadores.txt","")