
import random


#sorted genera una lista nueva

#ATENTO a la diferencias #####################

#sort modifica la lista


# lista1=[1,2,3,4,45,6]

#Metodo sort

# print(lista1)
# 
# lista1.sort()
# 
# print(lista1)
# 
# #Metodo sorted
# 
# print(lista1)
# 
# nuevaLista = list(sorted(lista1))  ##Aca lo convierte a lista con list
# 
# print(lista1)
# 
# print(nuevaLista) #Aca mostramos la nueva lista


#Rebanado o slicing

# lista=["a","e","i","o","u"]
# 
# #Inicio
# #Es inclusivo del principio y no inclusive en el fin 
# print(lista[1:4])
# 
# print(lista[:3])
# 
# 
# listaPrimerElemento = lista[:1]
# print(listaPrimerElemento)
# 
# print(lista[-2:])
# 
# print(lista[::-1])
# 
# print(lista[::2])
# 

#Reverse modifica la lista #############################################

# listaEjemplo = [77,66,55,34,23,129]
# 
# listaEjemplo.reverse()
# print(listaEjemplo)
# 
# #Reversed crea una nueva modificada ###############################################
# 
# listaInvertida = list(reversed(listaEjemplo))
# 
# print(listaEjemplo)
# print(listaInvertida)


#Ejercicio 1 ##################################################

# Dada la lista: numeros = [10, 20, 30, 40, 50, 60, 70, 80]
# Consigna
# Obtener los elementos desde el índice 2 al 5
# Obtener los primeros 3 elementos
# Obtener la lista al revés usando slicing

# numeros = [10, 20, 30, 40, 50, 60, 70, 80]
# 
# print(numeros[2:6])
# 
# print(numeros[:4])
# 
# print(numeros[::-1])

#Metodo insert

# listaVariable=[4,55,66,2]
# 
# print(listaVariable)
# listaVariable.insert(2, "Programacion") #insert permite insertar un elemento
# print(listaVariable)
# 
# lista1=["pepe","joaquin","jose"]
# lista2=["luciana", "julia", "analia"]
# 
# lista3 = lista1 + lista2
# print(lista3)
# 
# 
# lista1.extend(lista2) #Extend permite agregar un iterable a otro iterable
# 
# print(lista1)

#Tambien hay operadores sum, min y max

#Operador IN
# 
# frutas = ["peras","bananas","manzana"]
# 
# if "peras" not in frutas:
#     print("La verduleria NO tiene peras")
# else:
#     print("La verdulerioa tiene peras")

#for each
    
# for i in range(len(frutas)):  #Metodo anterior
#     print(frutas[i])
#     
# for fruta in frutas:   #Metodo nuevo dan el mismo resultado
#     print(fruta)
#     
#     
# #Listas por comprension
# 
# #[Expresion o transformacion del elemento for i in range condicion]
#     
# listaUnoalCien=[i**3 for i in range(0,101) if i%2==0] #Metodo por comprension

#Ejercicio 2

# Una escuela está desarrollando un sistema para generar reportes automáticos de desempeño.
# Cada alumno tiene una nota final en la materia.
# notas = [4, 7, 2, 9, 6, 10, 3]
#  
# El sistema necesita mostrar en el panel únicamente a los alumnos que aprobaron la materia (nota mayor o igual a 6), ya que estos serán incluidos en el cuadro de honor.
# Generar una nueva lista con las notas aprobadas.


# notas = [4, 7, 2, 9, 6, 10, 3]
# listaDeAprobados=[]
# 
# 
# listaDeAprobados = [i for i in notas if i >= 6 ]
#  
#     
# print(listaDeAprobados)


#Cadenas de caracteres

# saludoClase = "Estamos en clases de pyhton"
# 
# bienvenida = 'hola estamos en clase de pyhthon'
# 
# print(saludoClase)
# 
# bienvenidaTriplicado = bienvenida*3
# print(bienvenidaTriplicado)
# 
# print(saludoClase.upper()) #Lo pasa a mayusucula
# 
# print(saludoClase.lower()) #Lo pasa a miniscula
# 
# print(saludoClase.capatilize()) #Primer letra en mayuscula
# 
# print(saludoClase.title())
# 
# print(saludoClase.swapcase())
# 
# print(saludoClase.replace())
# 
# #split y join  ###########################################
# 
# nombre =["joaquin", "pedro","luis","andres"]
# 
# nombreString= ",".join(nombre)
# 
# print(nombreString)
# 
# nombrecitos = nombreString.split(",")
# print(nombrecitos)
# 
# 
# cuento ="   Habia una vez en una casa de perro         "
# print(cuento.strip()) #QUITA ESPACIO EN AMBOS LADOS
# print(cuento.lstrip()) #Quita espacio de izquierda
# print(cuento.rstrip()) #Quita espacio de derecha
# 
# #format String f-string ####################################
# 
# edad=18
# nombre="jullia"
# apellido = "monasterio"
# 
# print(f"Hola mi nombre es {nombre} y tengo {edad*2} años y mi apellido es {apellido}")

#Ejercicio 3 ########################################################## (Falta completar)
# Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos. Realice la composición de la lista por comprensión y de la forma habitual (tendrá dos funciones distintas).
# b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro. Utilice comprensión de listas para resolverlo.
# d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50,17,91,17,50].

def cargar_lista():
    lista=[]
    
    for numero in range(random.randint(10,11)):
        
        lista.append(random.randint(1000,9999))
        
    return lista

print(cargar_lista())

def cargar_lista2():
    lista2 =[]
    return[random.randint(1000,9999) for i in range (random.randint(10,11))]
    
    
    
    
        






