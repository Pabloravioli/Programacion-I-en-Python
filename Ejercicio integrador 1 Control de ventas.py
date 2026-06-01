"""

EN ESTE EJERCICIO TUVE UN PEQUEÑO ERROR QUE JODIO TODO ESTABA PÁSANDO A INT EL PRECIO QUE VIENE CON DECIMAL POR LO

TANTO NO DEJO AVANZAR EL PROGRAMA CUANDO ALGO TIENE PRECIO TENGO QUE PASARLO A FLOAT

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
        
        precioUnitario = round(float(precioUnitario),2)
        
        producto = {
            
            "Codigo":codigo,
            
            "Descripcion":descripcion,
            
            "Cantidad":cantidad,
            
            "Precio unitario":precioUnitario
            
            }
        
        listaDeProductos.append(producto)
        
        
    return listaDeProductos
    

def calcularCantidadVendidaYRecaudacionTotalPorProducto(listaProductos):
    
    
    
    
    
    productosXVentas={}
    
    for producto in listaProductos:
        
        if producto["Codigo"] not in productosXVentas:
            
            productosXVentas[producto["Codigo"]] = {
                "Codigo":producto["Codigo"],
                "Descripcion":producto["Descripcion"],
                "Cantidad":producto["Cantidad"],
                "Precio Unitario":producto["Precio unitario"],
                "Cantidad total":producto["Cantidad"],
                "Recaudacion total":producto["Precio unitario"]*producto["Cantidad"],
                
                
                }
        
        else:
            
            productosXVentas[producto["Codigo"]]["Cantidad total"] += producto["Cantidad"]
            
            productosXVentas[producto["Codigo"]]["Recaudacion total"] += producto["Cantidad"] * producto["Precio unitario"]

       
       
        
    return list(productosXVentas.values())


def generarReporte(reporte):
    
    try:
        
        rutaActual = os.path.dirname(__file__)
        
        rutaArchivo = os.path.join(rutaActual,"reporte.txt")
        
    except Exception as e:
        
        print(e)
        
    try:
        with open(rutaArchivo,"w",encoding="utf-8") as reporteDeVentasTotal:
            
            for ventaTotal in reporte:
                
                codigo = str(ventaTotal["Codigo"])
                
                cantidad = str(ventaTotal["Cantidad total"])
                
                recaudacion =str(ventaTotal["Recaudacion total"])
                
                linea = f"{codigo};{cantidad};{recaudacion} \n"
                
                reporteDeVentasTotal.write(linea)
                
            
    except Exception as e:
        
        print(e)
        
        
def mostrarProductoConMasRecaudacion(reporte):
    
    print(max(reporte, key=lambda x: x["Recaudacion total"]))
    

        
        

    
def main():
    
    
    
    try:
    
        with open("ventas.txt", "r", encoding="utf-8") as archivo:
            
            productos = leerArchivo(archivo)
    
    except Exception as e:
        
         
        print(e)
        
    reporte = calcularCantidadVendidaYRecaudacionTotalPorProducto(productos)
    
    generarReporte(reporte)
    
    mostrarProductoConMasRecaudacion(reporte)
    
main()

