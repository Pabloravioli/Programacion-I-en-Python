"""

Sistema de gestión de un complejo de cabañas (versión final, con más cálculos)
Un complejo de cabañas turístico desea analizar las reservas realizadas durante una temporada. Cada registro representa una reserva individual de una cabaña. Una misma cabaña puede aparecer múltiples veces en el archivo, ya que las reservas se registran de forma independiente.
Cada registro deberá contener el siguiente formato:
id_cabania;temporada;noches;huespedes;tarifa_total
Donde:
 
id_cabania: número entero que identifica la cabaña
temporada: cadena de texto ("Baja", "Media" o "Alta")
noches: cantidad de noches de la reserva
huespedes: cantidad de huéspedes alojados
tarifa_total: importe total cobrado por la reserva
 
Ejemplo:
3;Alta;5;4;120000
9;Baja;2;2;28000
3;Media;3;6;65000
En el ejemplo anterior, la cabaña 3 posee dos registros, por lo que al momento de procesar la información deberán considerarse ambos para obtener sus métricas finales.
a) Generación del archivo (1 punto)
Generar automáticamente un archivo plano llamado reservas_cabanias.txt con 800 registros aleatorios, respetando los siguientes rangos:
 
id_cabania: entre 1 y 25
temporada: elegir aleatoriamente entre: "Baja", "Media", "Alta"
noches: entre 1 y 10
huespedes: entre 1 y 8
tarifa_total: entre 8000 y 60000
 
b) Procesamiento por cabaña (4 puntos)
Procesar el archivo y obtener para cada cabaña:
 
Cantidad total de reservas
Noches totales ocupadas
Huéspedes totales alojados
Facturación total
Promedio de tarifa por reserva
Promedio de huéspedes por reserva
Cantidad de reservas correspondientes a temporada "Alta"
 
c) Determinaciones globales (3 puntos)
A partir de los datos procesados, determinar:
 
La cabaña con mayor facturación total
La cabaña con mayor cantidad de noches ocupadas
La cabaña con el promedio de huéspedes por reserva más alto
La cantidad de cabañas cuya facturación total supera el promedio general de facturación
El porcentaje que representa la facturación de cada cabaña sobre el total general del complejo
La diferencia entre la facturación de la cabaña más rentable y la menos rentable
 
d) Generación del archivo de reporte (2 puntos)
Generar un archivo plano llamado reporte_cabanias.txt que contenga una línea por cada cabaña con el siguiente formato:
id_cabania;reservas;noches_totales;huespedes_totales;facturacion_total;promedio_tarifa;promedio_huespedes

"""

import random

"""
Ejemplo:
3;Alta;5;4;120000
9;Baja;2;2;28000
3;Media;3;6;65000
En el ejemplo anterior, la cabaña 3 posee dos registros, por lo que al momento de procesar la información deberán considerarse ambos para obtener sus métricas finales.
a) Generación del archivo (1 punto)
Generar automáticamente un archivo plano llamado reservas_cabanias.txt con 800 registros aleatorios, respetando los siguientes rangos:
 
id_cabania: entre 1 y 25
temporada: elegir aleatoriamente entre: "Baja", "Media", "Alta"
noches: entre 1 y 10
huespedes: entre 1 y 8
tarifa_total: entre 8000 y 60000
"""



def generarArchivo(nombreArchivo):
    
    cantidadDeRegistros = 10
    
    listaDeTemporadas = ["Baja", "Media", "Alta"]
    
    try:
        with open(nombreArchivo, "w",encoding="utf-8") as archivo:
            
            for registro in range(cantidadDeRegistros): #FOR IN RANGE EXCLUYE AL ULTIMO POR QUE EMPIEZA DESDE EL 0 LO IMPORTANTE ES VER LA CANTIDAD DE VECES QUE LO HACE
            
                id_cabania = random.randint(1,25) #A RANDOM RANDINT SIEMPRE PASARLE DOS ARGUMENTOS (NO EXCLUYE NINGUNO)
                
                temporada = listaDeTemporadas[random.randint(0,len(listaDeTemporadas)-1)]
                
                noches = random.randint(1,10)
                
                huespedes = random.randint(1,8)
                
                tarifa_total = random.randint(8000,60000)
            
                linea = f"{id_cabania};{temporada};{noches};{huespedes};{tarifa_total}\n"
                
                archivo.write(linea)
          
    except Exception as e:
        
        print(e)
"""
b) Procesamiento por cabaña (4 puntos)
Procesar el archivo y obtener para cada cabaña:
 
Cantidad total de reservas
Noches totales ocupadas
Huéspedes totales alojados
Facturación total
Promedio de tarifa por reserva
Promedio de huéspedes por reserva
Cantidad de reservas correspondientes a temporada "Alta"

"""
def procesarArchivo(archivoCabania):
    
    diccionarioReservas={}
    
    try:
        with open(archivoCabania,"r",encoding="utf-8") as archivo:
            
            for linea in archivo:
                
                linea = linea.strip()
                
                if linea == "":
                    
                    print("Registro vacio")
                    
                else:
                    
                    partes = linea.split(";")
                    
                    if len(partes) != 5:
                        
                        print("Error en el registro")
                        
                    else:
                        
                        IdCabania = partes[0]
                        
                        temporada = partes[1]
                        
                        
                        noches = int(partes[2])
                        
                        huespedes = int(partes[3])
                        
                        tarifaTotal = int(partes[4])
                        
                        if IdCabania not in diccionarioReservas: #ACA NO USO VALUES.() POR QUE ESTOY PREGUNTANDO POR CLAVE GENERAL
                        
                            diccionarioReservas[IdCabania] ={
                                "ID":IdCabania,
                                "Temporada":temporada,
                                "Noches":noches,
                                "Huespedes":huespedes,
                                "Tarifa total":tarifaTotal,
                                "Cantidad de reserva": 1,
                                "Cantidad de altas": 1 if temporada == "Alta"else 0 #USE OPERADOR TERNARIO
                                
                                
                                }
                        else:
                            
                            diccionarioReservas[IdCabania]["Cantidad de reserva"] += 1
                            diccionarioReservas[IdCabania]["Noches"] += noches
                            diccionarioReservas[IdCabania]["Huespedes"] += huespedes
                            diccionarioReservas[IdCabania]["Tarifa total"] += tarifaTotal
                            if diccionarioReservas[IdCabania]["Temporada"] == "Alta":
                                
                                diccionarioReservas[IdCabania]["Cantidad de altas"] += 1
            
            for cabania in diccionarioReservas.values():#ATENTO A LA ENTRADA USE CABANIA[] NO DICCIONARIORESERVA[] POR QUE ESTOY USANDO EL .VALUES()
                
                cabania["Promedio de tarifas por reserva"] = round(cabania["Tarifa total"]/cabania["Cantidad de reserva"],2)
                cabania["Promedio de huespedes por reserva"] = round(cabania["Huespedes"]/cabania["Cantidad de reserva"],2)
            
    except Exception as e:
        print(e)
        
    return diccionarioReservas

def main():
    
    generarArchivo("reservas_cabanias.txt")
    
    diccionario=procesarArchivo("reservas_cabanias.txt")
    
    for cabania in diccionario.values():
        
        print(cabania)
    
    
    
main()