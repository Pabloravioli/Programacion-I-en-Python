# #Matrices
# #Para recorrer una matriz
# 
# matriz = [[1,2,3],
#           [4,5,6],
#           [7,8,9],]
# 
# 
# print(matriz[1],[1])
# 
# for fila in range(len(matriz)):    #Esta es la manera de recorrer una lista
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna])
#         
#         
# #Ejercicio Ejemplo
# 
# datosAlumnos =[]
# 
# cantAlumnos = int(input("Ingrese la cantidad de alumnos a procesar"))
# 
# for fila in range(cantAlumnos):
#     alumnos = []
#     
#     nombre = input("Ingrese el nombre del alumno")
#     legajo = int(input("Ingrese el legajo del alumno"))
#     
#     alumnos.append(nombre)
#     alumnos.append(legajo)
#     
#     datosAlumnos.append(alumnos)
#     
# print(datosAlumnos)
# 
# #Manera mas prolija de printear
# #PARA USAR "\" es altGr + ? 
# 
# for fila in range(len(datosAlumnos)):
#     print("Nombre: ", datosAlumnos[fila][0], "Legajo: " , datosAlumnos[fila][1])
    

# #Ejercicio 1
# Sistemas de reservas de cine
# 
# Sala del cine es de 5x6
# 
# - Crear la sala
# 
# - Mostrar la sala
# 
# - Reservar un asiento
# 
# - Contar asientos libres


#Modularizar

# def crear_sala(filas, columnas):
#     cine = []
#     
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             fila.append(0)
#         cine.append(fila)
#         
#     return cine
# 
# def mostrar_sala(matriz):
#     for fila in matriz:
#         print(fila)
#         
# def reservar_asiento(fila,columna):
#     if matriz[fila][columna] == 0:
#         matriz[fila][columna]=1
#     else:
#         print("Ocupado")
# 
# def contar_asientos_libres(matriz):
#     asientosLibres=0
#     
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if matriz [i][j] ==0:
#                 asientosLibres = asientosLibres+1
#     return asientosLibres
# 
# def main():
#     cine = crear_sala(5,6)
# 
#     
#     fila = int(input("Ingrese la fila que desea reservar del 1 al 5"))
#     asiento = int(input("Ingrese el asiento de la fila que desea ocupar"))
#     reservar_asiento(cine, fila, asiento)
#     
#     mostrar_sala(cine)
#     
#     print("La cantidad de asientos libres es: ",contar_asientos_libres(cine))
#     
# main()

#Ejercicio 2
# - Crear matriz con números consecutivos (hecho)
# - Sumar diagonal (falta hacer)
# - Contar pares (falta hacer)

# def crear_matriz(filas,columnas):
#     matriz = []
#     contador = 0
#     
#     for i in range(filas):
#         fila = []
#         for j in range(columnas):
#             contador+=1
# 
#             fila.append(contador)
#         matriz.append(fila)
#         
#     return matriz
# 
# 
# def sumar_diagonal():   
#     
# matriz_numeros = crear_matriz(2,2)
# print(matriz)

# #Ejercicio 3 (Revisar y completar el ejercicio)
# #Mostrar las notas
# #Promedio por alumno
# #Promedio general de todos los alumnos
# #Contar la cantidad de aprobados 4 o mayor de cuatro
# 
# def cargar_matriz_alumnos(cantidadAlumnos, cantNotasxAlumno):
#     matrizNotas =[]
#     
#     for i in range(cantidadAlumnos):
#         notaAlumno =[]
#         for j in range(cantNotasxAlumno):
#             
#             notas = int(input("Ingrese la nota"))
#             notasAlumno.append(nota)
#         matrizNotas.append(notasAlumnos)
#     return matrizNotas
# 
# 
# def mostrar_matriz_notas():
#     
#     for i in range(len(matrizNotas)):
#         
#         for i in range(len(matrizNotas)):
#             print("Alumno" , i+1, ":", end=" ")
#             for j in range(len(matriz[i])):
#                 print(matrizNotas[i][j], end= " ")
#         print()
#         
# 
# def promedio_por_alumno(notasAlumno):
#     
#     suma = 0
#     for nota in notasAlumno:
#         suma+=nota
#         
#     return suma/len(notasAlumnos)
# 
# def promedio_general_comision(matrizNotas):
#     
# 
# 
# 
# def main():
#     cantAlumnos = int(input("Ingrese la cantidad de alumnos que desea procesar"))
#     cantNotasxAlumnos = int(input("Ingrese la cantidad de notas por alumno que desea procesar"))
#     
#     matrizNotas = cargar_matriz_alumnos(cantAlumnos, cantNotasxAlumnos)
#     
#     mostrar_matriz_notas(matrizNotas)
#     
#     
#     for i in range(len(matrizNotas)):
#         promedio = promedio_por_alumno(matrizNotas[i])
#         print("El promedio del alumno ", i+1, "es ", promedio)
#     
#Ejercicio 4

# Gestion de Stock
# Cada final va a represnetar el total de los prodctos en la sucursal. Es decir que cada columna representa un producto. Cantidad de productos pedirselo al usuario y la cantidad de sucusales tmb. 
# - Cantidad total de todos los productos por sucursal 
# - Cantidad total de producto sentre todas las sucursales 
# - Maximo stock de todos los productos
# (falta completar)

def crear_matriz_tiendas(cantTiendas,producto):
    matriz_tiendas =[]
     for i in range(cantTiendas):
        tienda = []
        for j in range(producto):
            tienda.append(producto)
        matriz_tiendas.append(tienda)
        
    return mamtriz_tiendas

    

