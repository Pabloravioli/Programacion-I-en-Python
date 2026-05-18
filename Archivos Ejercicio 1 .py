"""
Generar un archivo donde cada registro sea:
legajo: nombre de alumnos.
Solicitar datos hasta que el legajo ingresado sea -1.

"""

import os



def cargar_alumno(archivo):
    
    bandera = True
    
    while bandera:
        legajo = int(input("Ingrese tu legajo"))
        
        if legajo != -1:
            
            nombreAlumno = input("Ingrese tu nombre")
            
            line = str(legajo)+";"+nombreAlumno+ "\n"
            
            archivo.write(line)
        else:
            bandera = False
            
            
            
            
def leerAlumnoMenor1000(ruta):
    
    
    try:
        
        with open(ruta, "r") as achivoAlumnos:
            for registro in archivoAlumnos:
                legajo,nombreAlumno = registro.split(";")
                
                if int(legajo) < 1000:
                    print(f"{legajo} \t {nombreAlumno}")
            
    except:
        print("Error")


def main():
    ruta_actual = os.path.dirname(__file__)
    ruta_file = os.path.join(ruta_actual, "alumnos.txt")
    try:
        
        
        with open(ruta_file,"w") as file:
            cargar_alumno(file)
    except Exception as e:

        print(f"El error es {e}")
    leerAlumnoMenor1000(ruta_file)
main()