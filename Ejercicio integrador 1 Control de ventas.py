"""

Una empresa posee un archivo ventas.txt con el siguiente formato:

codigo_producto;descripcion;cantidad;precio_unitario

Se solicita:

1. Leer el archivo.

2. Generar un diccionario donde la clave sea el código del producto.

3. Calcular la cantidad total vendida y la recaudación total por producto.

4. Generar un archivo reporte.txt.

5. Mostrar el producto con mayor recaudación.

"""

import os

def leerArchivo(file):
    
    listaDeProductos =[]
    
    for linea in file:
        
        codigo, descripcion, cantidad, precioUnitario = linea.strip().split(";")
        
        cantidad = int(cantidad)
        
        precioUnitario = int(precioUnitario)
        
        producto = {
            
            "Codigo":codigo,
            
            "Descripcion":descripcion,
            
            "Cantidad":cantidad,
            
            "Precio Unitario":precioUnitario
            
            }
        
        listaDeProductos.append(producto)
        
        
    return listaDeProductos
    

def calcularCantidadVendidaYRecaudacionTotalPorProducto(listaProductos):
    
    listaDeVentas = []
    
    for producto in listaProductos:
        
        productosXVentas={}
    

    
    
def main():
    
     try:
    
        with open("ventas.txt", "r", encoding="utf-8") as archivo:
        
        productos = leerArchivo(archivo)
    
    except Exception as e:
        
        print(e)
        
    calcularCantidadVendidaYRecaudacionTotalPorProducto(productos)
    
main()

