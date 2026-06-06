"""

Sistema de Gestion de Vuelos
Descripcion general
Se desea construir un sistema para gestionar los vuelos de una aerolinea.
El archivo vuelos.txt contiene un vuelo por linea con el siguiente formato:
CODIGO;DESTINO;AEROLINEA;PASAJEROS;PRECIO_TICKET
 
Ejemplo:
AR1001;MIAMI;AEROLINEAS;180;85000
LA2050;MADRID;LATAM;210;120000
IB3300;ROMA;IBERIA;95;98000
 
Consideraciones:
•   Los pasajeros y el precio son numeros enteros.
•   La recaudacion de un vuelo se calcula como: PASAJEROS x PRECIO_TICKET.
•   Un vuelo esta lleno si tiene 200 o mas pasajeros.
Consignas
1.  Escribir la funcion cargar_vuelos(nombre_archivo) que lea el archivo y retorne una matriz donde cada fila representa un vuelo. La funcion debe manejar excepciones e ignorar las lineas vacias o mal formadas. Retornar la matriz completa.
2.  Escribir la funcion mostrar_tabla(matriz) que imprima los vuelos en formato tabla. Los textos deben mostrarse en mayusculas.
3.  Escribir la funcion buscar_vuelo(matriz, codigo) que reciba la matriz y un codigo de vuelo (sin importar mayusculas/minusculas) y retorne la fila del vuelo si existe, o None si no se encontro.
4.  Escribir la funcion calcular_recaudacion(pasajeros, precio_ticket) que calcule y retorne la recaudacion total del vuelo.
5.  Escribir la funcion agregar_vuelo(matriz, codigo, destino, aerolinea, pasajeros, precio_ticket) que incorpore un nuevo vuelo a la matriz y retorne la matriz actualizada.
6.  Escribir la funcion estadistica(matriz) que recorra la matriz y retorne un diccionario con la siguiente estructura:
{
"cantidad_total": int,
"vuelos_llenos": int,
"vuelos_con_lugar": int,
"recaudacion_total": float,
"vuelo_mas_caro": str,
"vuelo_mas_barato": str
}
Donde:
•   cantidad_total: total de vuelos cargados.
•   vuelos_llenos: vuelos con 200 o mas pasajeros.
•   vuelos_con_lugar: vuelos con menos de 200 pasajeros.
•   recaudacion_total: suma de (pasajeros x precio_ticket) de todos los vuelos.
•   vuelo_mas_caro: codigo del vuelo con mayor precio de ticket.
•   vuelo_mas_barato: codigo del vuelo con menor precio de ticket.
7.  Escribir la funcion recursiva suma_pasajeros(matriz, indice) que calcule la cantidad total de pasajeros en todos los vuelos usando recursion.
Caso base: si el indice es igual al largo de la matriz, retornar 0.
En cada llamada, sumar los pasajeros del vuelo en la posicion indice al resultado recursivo.
8.  Escribir la funcion guardar_reporte(matriz, nombre_archivo) que genere un archivo de texto con el siguiente formato por linea:
CODIGO;DESTINO;RECAUDACION;ESTADO
El estado puede ser LLENO o CON LUGAR.
 
 
"""

import os

AZUL    = "\033[34m"
VERDE   = "\033[32m"
AMARILLO= "\033[33m"
ROJO    = "\033[31m"
RESET   = "\033[0m"

def cargar_vuelos(nombre_archivo):
    
    matrizVuelos = []
    
    try:
        with open(nombre_archivo,"r",encoding = "utf-8") as archivo:
            
            for vuelo in archivo:
                
                linea = vuelo.strip()
                
                if linea == "":
                    
                    print(f"{ROJO} Informacion de vuelo inexistente {RESET}")
                    
                else:
                    
                    linea = linea.split(";")
                    
                    
                    if len(linea) < 5:
                        
                        print("Informacion de vuelo incompleta")
                        
                    elif len(linea) == 5:
                        
                        codigo = linea[0]
                        
                        destino = linea[1]
                        
                        aerolinea = linea[2]
                        
                        pasajeros = int(linea[3])
                        
                        precio = int(linea[4])
                        
                        vuelo = [codigo,destino, aerolinea, pasajeros, precio]
                        
                        matrizVuelos.append(vuelo)
                    
            
    except Exception as e:
        
        print(e)
        
    return matrizVuelos


def mostrar_tabla(matriz):
    
    print(f"{'CODIGO':<10} {'DESTINO':<15} {'AEROLINEA':<10} {'PASAJEROS':>15} {'PRECIO':>10}")
    
    print("-" * 64)
    
    for vuelo in matriz:
        
        print(f"{vuelo[0]:<10} {vuelo[1]:<15} {vuelo[2]:<10} {vuelo[3]:>15} {vuelo[4]:>10}")
        
    print("#" * 64 , "\n")
    
    
def buscar_vuelo(matriz, codigo):
    
    
    
    for vuelo in matriz:
        
        if codigo == vuelo[0]:
            
            return f"{vuelo[0]:<10} {vuelo[1]:<15} {vuelo[2]:<10} {vuelo[3]:>15} {vuelo[4]:>10}"
    return None
    
    
    
def calcular_recaudacion(pasajeros, precio_ticket):
    
    
    
    return pasajeros * precio_ticket
    
    
def agregar_vuelo(matriz, codigo, destino, aerolinea, pasajeros, precio_ticket):
    
    vueloNuevo = [codigo, destino, aerolinea, pasajeros, precio_ticket]
    
    matriz.append(vueloNuevo)
    

def estadistica(matriz):
    
    diccionarioVuelos ={}
    
    cantidadVuelos = len(matriz)
    
    vuelosLlenos = 0
    
    vuelosConLugar = 0
    
    recaudacionTotal = 0
    
    vueloMasCaro = max(matriz, key= lambda vuelo: vuelo[4])
    
    vueloMasBarato = min(matriz, key=lambda vuelo: vuelo[4])
    
    
    
    for vuelo in matriz:
        
        if vuelo[3] >= 200:
            
            vuelosLLenos +=1
        else:
            
            vuelosConLugar +=1
            
        recaudacionXVuelo = vuelo[3] * vuelo[4]
        
        recaudacionTotal += recaudacionXVuelo
            
        
            
        
            
        
    diccionarioVuelos = {
        "cantidad_total": int(cantidadVuelos),
        "vuelos_llenos": int(vuelosLLenos),
        "vuelos_con_lugar": int(vuelosConLugar),
        "recaudacion_total": round(float(recaudacionTotal),2),
        "vuelo_mas_caro": str(vueloMasCaro),
        "vuelo_mas_barato": str(vueloMasBarato)
        }
        

def suma_pasajeros(matriz, indice):
    
    if len(matriz) == indice:
        
        return 0
    
    return matriz[indice][3] + suma_pasajeros(matriz, indice+1)
"""
8.  Escribir la funcion guardar_reporte(matriz, nombre_archivo) que genere un archivo de texto con el siguiente formato por linea:
CODIGO;DESTINO;RECAUDACION;ESTADO
El estado puede ser LLENO o CON LUGAR.
"""

def guardar_reporte(matriz,nombre_archivo):
    
    try:
        with open(nombre_archivo, "w", encoding = "utf-8") as archivo:
            
            for vuelo in matriz:
                
                if vuelo[3] >= 200:
                    
                    estado = "LLENO"
                else:
                    
                    estado = "VACIO"
            
                linea = f"{vuelo[0]};{vuelo[1]};{vuelo[3] * vuelo[4]};{estado}"
                
                archivo.write(linea)
                
    except Exception as e:
        
        print(e)
        
        

def main():
    
    matrizVuelos = cargar_vuelos("vuelos.txt")
    
    mostrar_tabla(matrizVuelos)
    
    codigo = (input("Ingrese codigo del vuelo: ")).upper()
    
    vueloEncontrado = buscar_vuelo(matrizVuelos,codigo)
    
    if vueloEncontrado == None:
        
        print(f"{ROJO} Vuelo no encontrado {RESET}")
    else:
        
        print(f"{VERDE} Vuelo encontrado {RESET}")
        
        print(vueloEncontrado)
        
        print("#" * 64, "\n")
        
    print(f"{'RECAUDACION TOTAL POR VUELO':<10}")
    
    print("-" * 64)
    
    print(f"{'CODIGO':<10} {'DESTINO':<15} {'AEROLINEA':<10} {'PASAJEROS':>15} {'PRECIO':>10}")
    
    print("-" * 64)
    
    
        
    for vuelo in matrizVuelos:
        
        recaudacionXVuelo = calcular_recaudacion(vuelo[3], vuelo[4])
        
        print (f"{vuelo[0]:<10} {vuelo[1]:<15} {vuelo[2]:<10} {vuelo[3]:>15} {vuelo[4]:>10}")
        
        print(f"\n{VERDE} {recaudacionXVuelo} {RESET}")
        
        print("-" * 64)
        
    print("#" * 64 , "\n")
        
    
    agregar_vuelo(matrizVuelos, "78jh", "agartha", "blueWings" , 124 , 1000)    
        
    
    print(f"{'VUELOS ACTUALIZADOS':<10} \n")
    
    
    print(f"{'CODIGO':<10} {'DESTINO':<15} {'AEROLINEA':<10} {'PASAJEROS':>15} {'PRECIO':>10}")
     
    print("-" * 64)
    
    for vuelo in matrizVuelos:
        
         print (f"{vuelo[0]:<10} {vuelo[1]:<15} {vuelo[2]:<10} {vuelo[3]:>15} {vuelo[4]:>10}")
         print("-" * 64)
    print("#" * 64 , "\n")
        
        
    sumaDePasajeros = suma_pasajeros(matrizVuelos, 0)
    
    print(f"{'SUMA PASAJEROS EN TOTAL':<10}")
     
    print("-" * 64)
    
    print(f"{VERDE}{sumaDePasajeros:< 10} {RESET}")   
     
    print("#" * 64 , "\n")
    
    guardar_reporte(matrizVuelos,"reporte.txt")

main()


