"""

Premisas

El código debe estar correctamente modularizado

Plataforma de videojuegos

Una plataforma online desea analizar la actividad de sus jugadores durante un mes.

Cada línea del archivo representa una sesión de juego independiente. Un mismo jugador puede aparecer varias veces en el archivo, ya que puede conectarse múltiples veces durante el período analizado.

Cada registro deberá contener el siguiente formato:

id_jugador;partidas_jugadas;puntos_obtenidos

Ejemplo:

25;4;850

18;2;300

25;3;620

En el ejemplo anterior, el jugador 25 posee dos registros diferentes, por lo que al momento de procesar la información deberán considerarse ambos para obtener sus métricas finales.

Se solicita

a) Generar automáticamente un archivo plano llamado partidas.txt con 1000 registros aleatorios.

El identificador del jugador deberá estar comprendido entre 1 y 100.

La cantidad de partidas deberá estar comprendida entre 1 y 20.

Los puntos obtenidos deberán estar comprendidos entre 50 y 5000.

b) Procesar el archivo y obtener para cada jugador:

Total de partidas jugadas.

Total de puntos obtenidos.

Promedio de puntos por partida.

c) Determinar:

Jugador con mayor cantidad de puntos acumulados.

Jugador con mayor promedio de puntos por partida.

d) Generar un archivo plano llamado reporte_jugadores.txt que contenga una línea por cada jugador con el siguiente formato:

id_jugador;partidas_totales;puntos_totales;promedio_puntos_por_partida

e) Implementar una función recursiva que reciba una colección con los puntos acumulados de los jugadores y retorne la suma total de puntos registrados en la plataforma.

"""
import random

def generarArchivo(archivo):
    
    cantidadDeRegistros = 11;
    
    try:
        
        with open (archivo, "w", encoding = "utf-8") as texto:
            
            for registro in range(cantidadDeRegistros):
                
                identificador = str(random.randint(1,100))
                
                cantidadDePartidas = random.randint(1,20)
                
                puntos = random.randint(50,5000)
                
                linea = f"{identificador};{cantidadDePartidas};{puntos}\n"
                
                texto.write(linea)
            
    except Exception as e:
        
        print(e)
"""
b) Procesar el archivo y obtener para cada jugador:

Total de partidas jugadas.

Total de puntos obtenidos.

Promedio de puntos por partida.

"""
        
        
def procesarArchivo(archivo):
    
    diccionarioJugadores={}
    
    try:
        with open(archivo, "r", encoding = "utf-8") as informacion:
            
            for linea in informacion:
                
                linea = linea.strip()
                
                if linea == "":
                    
                    print("Sin informacion del jugador")
                    
                else:
                    
                    partes = linea.strip().split(";")
                    
                    if len(partes) == 3:
                        
                        identificador = partes[0]
                        
                        cantidadDePartidas = int(partes[1])
                        
                        puntos = int(partes[2])
                        
                        if identificador in diccionarioJugadores:
                            
                            diccionarioJugadores[identificador]["Total de partidas"] += cantidadDePartidas
                            
                            diccionarioJugadores[identificador]["Total de puntos"] += puntos
                            
                            
                            
                        else:
                            
                            diccionarioJugadores[identificador]={
                                
                                "ID": identificador,
                                
                                "Total de partidas": cantidadDePartidas,
                                
                                "Total de puntos": puntos
                                }
                            
                            
                    else:
                        
                        print("Error al leer informacion del jugador")
                            
            for jugador in diccionarioJugadores.values():
                
                jugador["Promedio"] = round(jugador["Total de puntos"]/jugador["Total de partidas"],2)
            
            
    except Exception as e:
        
        print(e)
        
            
            
        
    return diccionarioJugadores



    
        
        
    



def main():
    
    generarArchivo("partidas.txt")
    
    diccionarioJugadores = procesarArchivo("partidas.txt")
    
    for jugador in diccionarioJugadores.values():
        
        print(f"{jugador['ID']};{jugador['Total de partidas']};{jugador['Total de puntos']}")
    

main()




