"""

Realizar un programa que permite actualizar una lista de precios en forma masiva ingresando un porcentaje de incremento
Debera:
Mediante una funcion generarOriginal crear el archivo original se llama precios.csv y
fue generado utilizando el siguente diseño de registro:

Codigo(Entero de 4 digitos)
Precio (valor real)
Descripcion
Se dispone un registro por producto, y los campos son separados por ; .
Generar la cantidad de productos de forma aleatoria, y los valores tambien

"""

import os

import random


def generarOriginal(file):
    
    productos = random.randint(1, 8)  
    for i in range(productos):
        codigo = random.randint(1000, 9999)
        precio = round(random.uniform(1000, 9999), 2)
        descripcion = f"producto {i}"
        linea = f"{codigo};{precio};{descripcion}\n"
        file.write(linea)
            
      
      
    
def leerLista(file):
    
    
            
    for registro in file:
                
        codigo, precio, descripcion = registro.strip().split(";")
                
        print(f" {codigo} \t {precio} \t {descripcion}")
                
        
                
                
            
                    
    
        
def actualizarPrecio(preciosOriginales,porcentaje):
    
    try:
        rutaActual = os.path.dirname(__file__)
        rutaPreciosOriginales = os.path.join(rutaActual, preciosOriginales)
        rutaPreciosActualizados = os.path.join(rutaActual,"Precios_Actualizados.csv")
        
        with open(rutaPreciosOriginales,"r") as original, open(rutaPreciosActualizados,"w") as actualizado:
            
            for productos in original:
                
                prodcutos = productos.strip()
                
                codigo, precio, nombre = productos.split(";")
                
                try:
                    
                    precio = float(precio)
                    
                    precioActualizado = str(round((1+porcentaje / 100) * precio , 2))
                    
                    lineaNueva = f"{codigo};{precioActualizado};{nombre}\n"
                    
                    actualizado.write(lineaNueva)
                    
                except ValueError:
                    
                    print("Tipo de dato de precio es incorrecto")
                
                continue
        print("Actualizamos los precios con exito")
    
    except Exception as e:
        
        print("Error 1", e)
            
        
        
def main():
    
   
    numeroPorcentaje = 7
  
       
    ruta_actual = os.path.dirname(__file__)
    ruta_file = os.path.join(ruta_actual, "Lista_Precios.txt")
    
    try:
        with open(ruta_file,"w") as file:
            
            generarOriginal(file)
            
    except Exception as e:
        
        print(f"El error fue 3: {e}")
        
    try:
        with open(ruta_file,"r") as file:
            
            leerLista(file)
            
    except Exception as e:
        
        print(f"El error fue :4 {e}")
        
    
    actualizarPrecio(ruta_file,numeroPorcentaje)
    
    
main()    
        