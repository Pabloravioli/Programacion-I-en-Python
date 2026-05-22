"""
Crear un programa que permita registrar la información de los libros de una biblioteca, utilizando un archivo para almacenar los datos. El registro de libros incluirá el título, el autor y la fecha de publicación.   
Adicionalmente, se deberá poder realizar la visualización de cada uno de los libros cargados. 
"""


"""
Para lograr el objetivo, deberá tener en cuenta los siguientes puntos:
"""

"""
Crea un archivo llamado libros.txt para almacenar los datos de los libros. Si el archivo ya existe, no se debe sobrescribir, sino agregar datos al final.
Crea una función llamada registrarLibro que reciba como parámetros el título del libro, el autor y la fecha de publicación, y guarde esta información en el archivo antes mencionado.
Se debe asegurar de que cada registro se almacene en una nueva línea del archivo y que los datos estén separados por el carácter ";" (punto y coma). Por ejemplo:

Ser feliz era esto;Eduardo Sacheri;2014 

Steve Jobs (La biografía);Walter Isaacson;2011 

Los años de peregrinación del chico sin color;Haruki Murakami;2013
"""

"""
Define una función llamada mostrarLibros, que lea el archivo libros.txt y muestre en pantalla la lista de libros.
"""

"""
Crea un bucle principal que permita al usuario seleccionar una opción: registrar un nuevo libro (solicitando el título, el autor y el año de publicación)
o mostrar el listado de libros.
El bucle debe repetirse hasta que el usuario decida salir (contemple agregar una nueva opción).
Utilizar excepciones para controlar que la carga y la generación de los archivos se realice correctamente.
Además, verifica que el título y el autor del libro sean cadenas de texto no vacías y el año de publicación un valor numérico (éste último utilizando excepciones)
"""
import os

def registrarLibro(titulo,autor,fechaDePublicacion,file):
    
    linea = f"{titulo};{autor};{fechaDePublicacion}\n"
    
    file.write(linea)
    
    
def mostrarLibros(file):
    
    for libro in file:
        
        titulo, autor, fecha = libro.strip().split(";")
        
        print(f" {titulo} \t {autor} \t {fecha}")
        
def main():
    
    respuesta = 0
    
    
    
    rutaActual = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaActual,"libros.txt")
    
    while respuesta !="-1":
        
        try:
        
            respuesta = input("Seleccione una opcion: 1 para registrar un libro, 2 para mostrar libros, -1 para salir: \n")
            
        except Exception as e:
            
            print("El error fue: " ,e)
            
        if respuesta == "1":
            
            seguir = "1"
            
            while seguir == "1":
                
                titulo = ""
                
                autor = ""
                
                fecha = 0
                
                while titulo == "":
            
                    titulo = input("Ingrese el titulo del libro:  ")
                
                    if titulo == "":
                    
                        print("Titulo invalido")
                        
                while autor == "":
                    
                    autor = input("Ingrese el autor del libro:  ")
                    
                    if autor == "":
                        print("Autor invalido")
                        
                try:
                
                    fecha = int(input("Ingrese la fecha de publicacion del libro:  "))
                    
                except Exception as e:
                    
                    print("La fecha tiene que ser de valor numerico unicamente \n")
                
                try:
                    with open (rutaArchivo, "a") as archivo:
                        
                        registrarLibro(titulo,autor,fecha,archivo)
                        
                        seguir = input("Seleccione 1  ingresar otro libro, -1 para salir: \n")
                 
                except Exception as e:
                     
                     print("El error es: 1",e)
                     
        
        elif respuesta == "2":
            
            try:
                
                with open (rutaArchivo, "r") as archivo:
                    
                    mostrarLibros(archivo)
                    
            except Exception as e:
                
                print("El erro  es: ",e)
                
        elif respuesta == "-1":
            
            print("Saliendo... \n")
            
            
        else:
            
            print("Opcion invalida")
                        
                        
            
            
        
          
main()