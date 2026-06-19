"""

Empresa de transportes

Una empresa de transporte desea analizar los viajes realizados por sus conductores durante un mes.

Cada línea del archivo representa una carga de información independiente correspondiente a un determinado período de trabajo. 

Un mismo conductor puede aparecer varias veces en el archivo, ya que los viajes realizados se registran en distintos momentos del mes.

Cada registro deberá contener el siguiente formato:

id_conductor;cantidad_viajes;kilometros_recorridos

Ejemplo:

15;8;420

8;12;730

15;4;210

En el ejemplo anterior, el conductor 15 posee dos registros diferentes, por lo que al momento de procesar la información deberán considerarse ambos para obtener sus métricas finales.

Se solicita:

a) Generar automáticamente un archivo plano llamado viajes.txt con 1000 registros aleatorios.

El identificador del conductor deberá estar comprendido entre 1 y 50.

La cantidad de viajes deberá estar comprendida entre 1 y 20.

Los kilómetros recorridos deberán estar comprendidos entre 50 y 1500.

b) Procesar el archivo y obtener para cada conductor:

Total de viajes realizados

Total de kilómetros recorridos

Promedio de kilómetros por viaje

c) Determinar:

Conductor con mayor cantidad de kilómetros recorridos

Conductor con mayor promedio de kilómetros por viaje.

d) Generar un archivo plano llamado reporte_viajes.txt que contenga una línea por cada conductor con el siguiente formato:

id_conductor;viajes_totales;kilometros_totales;promedio_km_por_viaje

e) Implementar una función recursiva que reciba una colección con los kilómetros acumulados de los conductores y retorne la suma total de kilómetros recorridos.

"""

import random

def generarArchivo(nombreArchivo):
    try:
        with open(nombreArchivo, "w", encoding = "utf-8") as archivo:
            
            for registro in range(1,1001):
                
                identificador =  random.randint(1,50)
                
                cantidadViajes = random.randint(1,20)
                
                kilometrosRecorridos = random.randint(50,1500)
                
                linea = f"{identificador};{cantidadViajes};{kilometrosRecorridos}\n"
                
                archivo.write(linea)
            
    except Exception as e:
        
        print(e)
        
"""
b) Procesar el archivo y obtener para cada conductor:

Total de viajes realizados

Total de kilómetros recorridos

Promedio de kilómetros por viaje

"""

def procesarArchivo(archivo):
    
    diccionarioConductores ={}
    
    matrizConductores = []
    
    sumadorViajes = 0
    
    sumadorKilometros = 0
    
    try:
        with open(archivo, "r", encoding="utf-8") as texto:
            
            for linea in texto:
                
                linea = linea.strip()
                
                if linea == "":
                    
                    print("Informacion no encontrada")
                    
                else:
                    
                    partes = linea.split(";")
                    
                    if len(partes) != 3:
                        
                        print("Error al encontrar informacion del conductor")
                        
                    else:
                        
                        idConductor = partes[0]
                        
                        viajes = int(partes[1])
                        
                        kilometros = int(partes[2])
                    
                        conductor = [idConductor, viajes, kilometros]
                        
                        matrizConductores.append(conductor)
                        
            for chofer in matrizConductores:
                
                if chofer[0] not in diccionarioConductores:
                    
                    diccionarioConductores[chofer[0]] = {
                        
                        "ID": chofer[0],
                        "Viajes":chofer[1],
                        "Kilometros":chofer[2]
                         }
                else:
                    
                    diccionarioConductores[chofer[0]]["Viajes"] += chofer[1]
                    
                    diccionarioConductores[chofer[0]]["Kilometros"] += chofer[2]
                    
            for chofer in diccionarioConductores.values():
                
                chofer["Promedio"] = round(chofer["Kilometros"]/chofer["Viajes"], 2)
                
    except Exception as e:
        
        print(e)
        
    return diccionarioConductores
                    
                
"""
c) Determinar:

Conductor con mayor cantidad de kilómetros recorridos

Conductor con mayor promedio de kilómetros por viaje.

"""
                    
def determinarConductores(diccionario):
    
    conductorMayorKilometros = max(diccionario.values(), key=lambda conductor: conductor["Kilometros"])
    
    conductorMayorPromedio = max(diccionario.values(), key=lambda conductor: conductor["Promedio"])
    
    print(f"Conductor con mayor kilometros recorridos ID {conductorMayorKilometros['ID']} con un recorrido de {conductorMayorKilometros['Kilometros']}")
    
    print(f"Conductor con mayor promedio de kilometros por viaje ID {conductorMayorPromedio['ID']} con un recorrido de {conductorMayorPromedio['Promedio']}")
    
                
"""
d) Generar un archivo plano llamado reporte_viajes.txt que contenga una línea por cada conductor con el siguiente formato:

id_conductor;viajes_totales;kilometros_totales;promedio_km_por_viaje

"""


def generarArchivoReporte(nombreReporte,diccionario):
    
    """
    Aca es donde me percate que usando .values() es mas facil acceder a los valores

    """
    
    try:
        with open(nombreReporte, "w", encoding= "utf-8") as reporte:
            
            for conductor in diccionario.values():
                
                idConductor = conductor["ID"]
                
                viajesTotales = conductor["Viajes"]
                
                kilometrosTotales = conductor["Kilometros"]
                
                promedioKilometrosPorViajes = conductor["Promedio"]
                
                linea = f"{idConductor};{ viajesTotales};{kilometrosTotales} \n"
                
                reporte.write(linea)
                
    except Exception as e:
        
        print(e)
    
                    
    

def main():
    
    generarArchivo("viajes.txt")
    
    diccionario = procesarArchivo("viajes.txt")
    
    determinarConductores(diccionario)
    
    generarArchivoReporte("reporte_viajes.txt",diccionario)

main()
