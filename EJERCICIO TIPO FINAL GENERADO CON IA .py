"""

EXAMEN FINAL – Sistema de Gestión de Biblioteca

Una biblioteca desea analizar los préstamos de libros realizados durante un año. Cada registro representa un préstamo individual. Un mismo libro puede aparecer varias veces en el archivo, ya que puede haber sido prestado en distintas ocasiones.

Cada registro tendrá el siguiente formato:

id_libro;categoria;dias_prestamo;socios;multa

Donde:

- id_libro: número entero que identifica al libro.
- categoria: cadena de texto ("Infantil", "Novela", "Historia" o "Tecnología").
- dias_prestamo: cantidad de días que el libro permaneció prestado.
- socios: cantidad de socios que participaron del préstamo.
- multa: importe abonado por demora (puede ser 0).

Ejemplo:

8;Novela;12;1;0
15;Tecnología;20;2;3500
8;Historia;15;1;500

En el ejemplo anterior, el libro 8 posee dos préstamos registrados, por lo que al procesar la información deberán considerarse ambos.

-------------------------------------------------------------
a) Generación del archivo (1 punto)
-------------------------------------------------------------

Generar automáticamente un archivo plano llamado:

prestamos_biblioteca.txt

con 1000 registros aleatorios, respetando los siguientes rangos:

- id_libro: entre 1 y 40
- categoria: elegir aleatoriamente entre:
    • Infantil
    • Novela
    • Historia
    • Tecnología
- dias_prestamo: entre 1 y 30
- socios: entre 1 y 5
- multa: entre 0 y 5000

-------------------------------------------------------------
b) Procesamiento por libro (4 puntos)
-------------------------------------------------------------

Procesar el archivo y obtener para cada libro:

- Cantidad total de préstamos.
- Cantidad total de días prestados.
- Total de socios que utilizaron el libro.
- Total de multas recaudadas.
- Promedio de días por préstamo.
- Promedio de socios por préstamo.
- Cantidad de préstamos correspondientes a la categoría "Tecnología".

-------------------------------------------------------------
c) Determinaciones globales (3 puntos)
-------------------------------------------------------------

A partir de los datos procesados, determinar:

- El libro que generó mayor recaudación por multas.
- El libro con mayor cantidad de días prestados.
- El libro con el promedio de socios por préstamo más alto.
- La cantidad de libros cuya recaudación total supera el promedio general de recaudación.
- El porcentaje que representa la recaudación de cada libro sobre el total general de multas de la biblioteca.
- La diferencia entre la recaudación del libro con mayor multa acumulada y el de menor multa acumulada.

-------------------------------------------------------------
d) Generación del archivo de reporte (2 puntos)
-------------------------------------------------------------

Generar un archivo plano llamado:

reporte_biblioteca.txt

que contenga una línea por cada libro con el siguiente formato:

id_libro;prestamos;dias_totales;socios_totales;multas_totales;promedio_dias;promedio_socios

-------------------------------------------------------------
e) Función recursiva (2 puntos)
-------------------------------------------------------------

Implementar una función recursiva que reciba como parámetro la estructura donde se almacenaron los datos procesados de los libros y devuelva:

La suma total de todas las multas recaudadas por la biblioteca.

La función debe cumplir las siguientes condiciones:

- No puede utilizar ciclos (for ni while).
- Debe recorrer la estructura únicamente mediante recursividad.
- Debe devolver el resultado para luego mostrarlo por pantalla.

-------------------------------------------------------------
Restricciones
-------------------------------------------------------------

- No se permite utilizar bibliotecas externas (excepto las necesarias para generar datos aleatorios).
- Toda la información debe obtenerse leyendo el archivo generado.
- Los cálculos deben realizarse utilizando estructuras de datos adecuadas (listas, diccionarios, etc.).
- El programa debe estar correctamente modularizado utilizando funciones.
- La función del punto e) debe resolverse exclusivamente mediante recursividad.

"""

"""
id_libro;categoria;dias_prestamo;socios;multa

Donde:

- id_libro: número entero que identifica al libro.
- categoria: cadena de texto ("Infantil", "Novela", "Historia" o "Tecnología").
- dias_prestamo: cantidad de días que el libro permaneció prestado.
- socios: cantidad de socios que participaron del préstamo.
- multa: importe abonado por demora (puede ser 0).

Ejemplo:

8;Novela;12;1;0
15;Tecnología;20;2;3500
8;Historia;15;1;500
"""
"""
-------------------------------------------------------------
a) Generación del archivo (1 punto)
-------------------------------------------------------------

Generar automáticamente un archivo plano llamado:

prestamos_biblioteca.txt

con 1000 registros aleatorios, respetando los siguientes rangos:

- id_libro: entre 1 y 40
- categoria: elegir aleatoriamente entre:
    • Infantil
    • Novela
    • Historia
    • Tecnología
- dias_prestamo: entre 1 y 30
- socios: entre 1 y 5
- multa: entre 0 y 5000
"""


import random 

def generarArchivo(nombreArchivo):
    
    cantidadDeRegistros = 10
    
    listaCategoria = ["Infantil", "Novela", "Historia", "Tecnologia"]
    
    try:
        with open(nombreArchivo, "w", encoding = "utf-8") as archivo:
            
            for registro in range(cantidadDeRegistros):
                
                idLibro = random.randint(1,40)
                
                categoria = listaCategoria[random.randint(0,len(listaCategoria)-1)] #EMPIEZA EN CERO LA LISTA NO EN 1 POR ESO DE 0 A LARGO DE LA LISTA PERO MENOS 1
                
                diasPrestamos = random.randint(1,30)
                
                socios = random.randint(1,5)
                
                multa = random.randint(0,5000)
                
                linea = f"{idLibro};{categoria};{diasPrestamos};{socios};{multa}\n"
                
                archivo.write(linea)
                
            
    except Exception as e:
        
        print(e)
        
"""
-------------------------------------------------------------
b) Procesamiento por libro (4 puntos)
-------------------------------------------------------------

Procesar el archivo y obtener para cada libro:

- Cantidad total de préstamos.
- Cantidad total de días prestados.
- Total de socios que utilizaron el libro.
- Total de multas recaudadas.
- Promedio de días por préstamo.
- Promedio de socios por préstamo.
- Cantidad de préstamos correspondientes a la categoría "Tecnología".
"""

def procesarArchivo(archivo):
    
    diccionarioLibros={}
    
    try:
        with open(archivo, "r", encoding="utf-8") as informacion:
            
            for linea in informacion:
                
                linea = linea.strip()
                
                if linea == "":
                    
                    print("Registro vacio")
                    
                else:
                    
                    partes = linea.split(";")
                    
                    if len(partes) != 5:
                        
                        print("Error en el registro")
                        
                    else:
                        
                        idLibros = partes[0]
                        
                        categoria = partes[1]
                        
                        diasPrestamos = int(partes[2])
                        
                        socios = int(partes[3])
                        
                        multa = int(partes[4])
                        
                        if idLibros not in diccionarioLibros:
                            
                            diccionarioLibros[idLibros]={
                                
                                "ID":idLibros,
                                "Categoria":categoria,
                                "Dias prestamos": diasPrestamos,
                                "Socios":socios,
                                "Multa":multa,
                                "Prestamos":1,
                                "Tecnologia": 1 if categoria == "Tecnologia" else 0
                                
                                }
                        else:
                            
                            diccionarioLibros[idLibros]["Prestamos"]+=1
                            diccionarioLibros[idLibros]["Dias prestamos"]+=diasPrestamos
                            diccionarioLibros[idLibros]["Socios"]+=socios
                            diccionarioLibros[idLibros]["Multa"]+=multa
                            if categoria == "Tecnologia":
                                
                                diccionarioLibros[idLibros]["Tecnologia"] += 1
                                
                
            for libro in diccionarioLibros.values():
                
                libro["Promedio dias"] = round(libro["Dias prestamos"]/libro["Prestamos"],2)
                libro["Promedio socios"] = round(libro["Socios"]/libro["Prestamos"],2)            
                            
                            
            
    except Exception as e:
        print(e)
        
    return diccionarioLibros

"""
-------------------------------------------------------------
c) Determinaciones globales (3 puntos)
-------------------------------------------------------------

A partir de los datos procesados, determinar:

- El libro que generó mayor recaudación por multas.
- El libro con mayor cantidad de días prestados.
- El libro con el promedio de socios por préstamo más alto.
- La cantidad de libros cuya recaudación total supera el promedio general de recaudación.
- El porcentaje que representa la recaudación de cada libro sobre el total general de multas de la biblioteca.
- La diferencia entre la recaudación del libro con mayor multa acumulada y el de menor multa acumulada.
"""
def determinar(diccionarioLibros):
    
    cantidad = 0
    
    libroConMasMultas = max(diccionarioLibros.values(), key=lambda libro: libro["Multa"])
    
    libroConMenosMultas = min(diccionarioLibros.values(), key=lambda libro: libro["Multa"])
    
    libroConMayorDias = max(diccionarioLibros.values(), key=lambda libro: libro["Dias prestamos"])
    
    libroConMayorPromedio = max(diccionarioLibros.values(), key=lambda libro: libro["Promedio socios"])
    
    recaudacionGeneral = sum(libro["Multa"] for libro in diccionarioLibros.values())
    
    promedioGeneral = round(recaudacionGeneral/len(diccionarioLibros),2)
    
    diferencia = libroConMasMultas["Multa"]-libroConMenosMultas["Multa"]
    
    for libro in diccionarioLibros.values():
        
        if libro["Multa"] > promedioGeneral:
            
            cantidad +=1
            
        libro["Porcentaje"] = round((libro["Multa"]/recaudacionGeneral)*100,2)
        
    return libroConMasMultas, libroConMayorDias, libroConMayorPromedio, cantidad, diferencia
        
"""
-------------------------------------------------------------
d) Generación del archivo de reporte (2 puntos)
-------------------------------------------------------------

Generar un archivo plano llamado:

reporte_biblioteca.txt

que contenga una línea por cada libro con el siguiente formato:

id_libro;prestamos;dias_totales;socios_totales;multas_totales;promedio_dias;promedio_socios
"""

def generarReporte(nombreReporte,diccionario):
    
    try:
        with open(nombreReporte, "w", encoding="utf-8") as reporte:
            
            for libro in diccionario.values():
                
                idLibro = libro["ID"]
                
                prestamos = libro["Prestamos"]
                
                diasTotales = libro["Dias prestamos"]
                
                sociosTotales = libro["Socios"]
                
                multaTotales = libro["Multa"]
                
                promedioDias = libro["Promedio dias"]
                
                promedioSocios = libro["Promedio socios"]
                
                linea = f"{idLibro};{prestamos};{diasTotales};{sociosTotales};{multaTotales};{promedioDias};{promedioSocios} \n"
                
                reporte.write(linea)
                
                
    except Exception as e:
        
        print(e)
    
"""
-------------------------------------------------------------
e) Función recursiva (2 puntos)
-------------------------------------------------------------

Implementar una función recursiva que reciba como parámetro la estructura donde se almacenaron los datos procesados de los libros y devuelva:

La suma total de todas las multas recaudadas por la biblioteca.

La función debe cumplir las siguientes condiciones:

- No puede utilizar ciclos (for ni while).
- Debe recorrer la estructura únicamente mediante recursividad.
- Debe devolver el resultado para luego mostrarlo por pantalla.

"""
    
def funcionRecursiva(lista,indice):
    
    if indice == len(lista):
        
        return 0
    else:
        
        
        return lista[indice]["Multa"] + funcionRecursiva(lista,indice+1)
    

    
    
    


def main():
    
    generarArchivo("prestamos_biblioteca.txt")
    
    diccionario = procesarArchivo("prestamos_biblioteca.txt")
    
    for libro in diccionario.values():
        
        print(f"id libro:{libro['ID']} cantidad de prestamos:{libro['Prestamos']} cantidad de socios:{libro['Socios']} multas recaudadas:{libro['Multa']} Promedio de dias por prestamo:{libro['Promedio dias']} Promedio de socios por prestamo:{libro['Promedio socios']}")
        
    libroMasMultas, libroMayorDias, libroPromedio, cantidad, diferencia = determinar(diccionario)
    
    print(f"libro con mas multas:{libroMasMultas['ID']} con una recaudacion de: {libroMasMultas['Multa']}")
    
    print(f"libro con mas dias: {libroMayorDias['ID']} con una cantidad de: {libroMayorDias['Dias prestamos']} dias")
    
    print(f"libro con mayor promedio : {libroPromedio['ID']} con una cantidad de: {libroPromedio['Promedio socios']} socios")
    
    print(f"La cantidad de libros que superan la recaudacion promedio general: {cantidad} ")
    
    print(f" La diferencia entre el libro con mas multa y con el que tiene menos multa es de: {diferencia}")
    
    for libro in diccionario.values():
        
        print(f"El porcentaje que representa cada libro ID: {libro['ID']} con un porcentaje de {libro['Porcentaje']}%")

    generarReporte("reporte_biblioteca.txt", diccionario)
    
    lista = list(diccionario.values())
    
    sumaTotal = funcionRecursiva(lista,0)
    
    print(sumaTotal)

main()

