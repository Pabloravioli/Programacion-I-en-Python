"""

Un archivo notas.txt contiene:

legajo;nombre;nota1;nota2;nota3

Se solicita:

1. Leer el archivo.

2. Guardar en un diccionario el nombre y la lista de notas.

3. Calcular promedio por alumno.

4. Generar promedios.txt.

5. Mostrar alumnos aprobados.

"""

import os

def leerArchivo(notas):
    
    listaAlumnos = []
    
    
    for nota in notas:
        
        legajo, nombre, nota1, nota2, nota3 = nota.strip().split(";")

        nota1 = int(nota1)
        nota2 = int(nota2)
        nota3 = int(nota3)
        
        alumno = {
            "nombre":nombre,
            
            "lista de notas":[nota1,nota2,nota3]
            }
        listaAlumnos.append(alumno)
        
    return listaAlumnos


    
    
def calcularPromedioPorAlumnos(alumnosYNotas):
    
    listaPromedio = []
    
    for alumnos in alumnosYNotas:
        
        promedios = {
            
            "Alumno": alumnos["nombre"],
            
            "Promedio": round(sum(alumnos["lista de notas"])/len(alumnos["lista de notas"]),2)
                  
            }
        listaPromedio.append(promedios)
        
    return listaPromedio
    

def generarPromedios(promediosCalculados):
    
    try:
    
        rutaActual = os.path.dirname(__file__)
    
        rutaArchivo = os.path.join(rutaActual,"promedios.txt")
        
    except Exception as e:
        
        print(e)
        
    try:
        
        with open(rutaArchivo, "w",encoding="utf-8") as promedios:
            
            
            for alumnos in promediosCalculados:
        
                str(alumnos['Promedio'])
        
                linea = f"{alumnos['Alumno']};{alumnos['Promedio']} \n"
        
                promedios.write(linea)
                       
    except Exception as e:
        
        print(e)
        
   
        
        
def mostrarAprobados(promedios):
    
    print("Alumnos aprobados: ")
    
    for promedio in promedios:
        
        if promedio["Promedio"] >= 4:
            
            print(f"{promedio['Alumno']} con una nota de {promedio['Promedio']}")
    
    
    
    
def main():
    
    try:
        with open("notas.txt","r",encoding="utf-8") as file:
            
            nombreYNotas = leerArchivo(file)
            
    except Exception as e:
        
        print(e)
        
    promediosCalculados = calcularPromedioPorAlumnos(nombreYNotas)
    
    
    generarPromedios(promediosCalculados)
    
    mostrarAprobados(promediosCalculados)
    
    
    
    
            
main()