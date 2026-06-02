"""

Existen dos archivos: ingresos.txt y ventas.txt.

Formato: codigo;producto;cantidad

Se solicita:

1. Generar un diccionario con stock final.

2. Restar ventas.

3. Informar productos con stock negativo.

4. Generar stock_final.txt

"""

import os

def generarDiccionarioStockFinal(ingresos,ventas):
    
    listaStock = []
    
    listaVentas = []
    
   
    
    for ingreso in ingresos:
        
        codigo, producto, cantidad = ingreso.strip().split(";")
        
        cantidad = int(cantidad)
        
        inventario = {
            
            "Codigo":codigo,
            "Producto":producto,
            "Cantidad":cantidad
            
            }
        
        listaStock.append(inventario)
        
    
    for venta in ventas:
        codigo, producto, cantidad = venta.strip().split(";")
        
        cantidad = int(cantidad)
        
        listaVentas[codigo] = {
            
            "Codigo":codigo,
            "Producto":producto,
            "Cantidad":cantidad
            
            }
        
    for dato in listaStock:
        
        if dato not in listaVentas:
            
            stockFinal = {
                "Codigo":dato["Codigo"],
                "Producto":dato["Producto"],
                "Cantidad":dato["Cantidad"]
                
                }
            
        else:
            
           stockFinal[dato]["Cantidad FINAL"] -= listaVentas[dato]["Cantidad"]
            
                
    return list(stockFinal.values())
    
def informarStockNegativo(stockFinal):
    
    stockNegativo = list(filter(lambda stock: stock["Cantidad"] < 0, stockFinal))
    
    print(stockNegativo)

def generarStockFinal(informacionFinal):
    rutaActual = os.path.dirname(__file__)
    rutaStockFinal = os.path.join(rutaActual,"stock_final.txt")
    try:
        with open(rutaStockFinal, "w",encoding = "utf-8") as stockF:
            
            for stock in informacionFinal:
                
                codigo = stock["Codigo"]
                
                producto = stock["Producto"]
                
                cantidad = str(stock["Cantidad Final"])
                
                linea = f"{codigo};{producto};{cantidad} \n"
                
                stockF.write(linea)
                
    except Exception as e:
        
        print(e)
    
        
        
    
    

def main():
    
    rutaActual = os.path.dirname(__file__)
    
    rutaIngresos = os.path.join(rutaActual,"ingresos.txt")
    
    rutaVentas = os.path.join(rutaActual,"ventas.txt")
    
    try:
        
        with open(rutaIngresos,"r",encoding = "utf-8") as archivoIngresos , open(rutaVentas,"r",encoding = "utf-8") as archivoVentas:
            
            listaStockFinal = generarDiccionarioStockFinal(archivoIngresos,archivoVentas)
        
    except Exception as e:
        
        print(e)
        
        
    informarStockNegativo(listaStockFinal)
        
    generarStockFinal(listaStockFinal)
    
    
main()