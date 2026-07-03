"""

Archivo: ciudad;temperatura

Se solicita:

1. Guardar temperaturas por ciudad.

2. Calcular promedio.

3. Mostrar ciudad más calurosa.

4. Generar temperaturas_promedio.txt que contenga dos registros: ciudad; temperatura_maxima y ciudad;temperatura_minima

"""
import random

def leerArchivo(archivo):
    
    diccionarioCiudades = {}
    
    try:
        
        with open(archivo, "r", encoding = "utf-8") as registros:
            
            for registro in registros:
                
                registro = registro.strip()
                
                if registro == "":
                    
                    print("Error al encontrar registro")
                else:
                    
                    registro = registro.strip().split(";")
                    
                    if len(registro) != 2:
                        
                        print("Error encontrado en el registro")
                        
                    else:
                        
                        ciudad = registro[0]
                        
                        temperatura = int(registro[1])
                        
                        diccionarioCiudades[ciudad] ={
                            
                            "Ciudad": ciudad,
                            
                            "Temperatura": temperatura
                            
                            }                
        
    except Exception as e:
        
        print(e)
        
    return diccionarioCiudades

def calcularPromedio(diccionario):
    
    sumador = 0;
    
    for registro in diccionario.values():
        
        sumador += registro["Temperatura"]
        
    promedio = round(sumador/len(diccionario),2)
    
    return promedio


def mostrarCiuadadMasCalurosa(diccionario):
    
    ciudadMasCalurosa = max(diccionario.values(), key = lambda ciudad: ciudad["Temperatura"])
    
    return ciudadMasCalurosa


def generarReporte(archivo,diccionario):
    
    try:
        with open(archivo, "w", encoding = "utf-8") as reporte:
            
            masCalor = max(diccionario.values(), key=lambda ciudad: ciudad["Temperatura"])
            menosCalor = min(diccionario.values(), key=lambda ciudad: ciudad["Temperatura"])
            
            linea = f"{masCalor['Ciudad']};{masCalor['Temperatura']};{menosCalor['Ciudad']};{menosCalor['Temperatura']}"
            reporte.write(linea)
    except Exception as e:
        
        print(e)

def main():
    diccionario = leerArchivo("registro_de_temperaturas.txt")
    
    prom = calcularPromedio(diccionario)
    
    print(f"El promedio fue {prom} C°")
    
    ciudadConMasCalor =  mostrarCiuadadMasCalurosa(diccionario)
    
    print(f"La ciudad con mas calor fue {ciudadConMasCalor['Ciudad']} con una temperatura de {ciudadConMasCalor['Temperatura']}")
    
    generarReporte("temperaturas_promedio.txt",diccionario)
    
main()

