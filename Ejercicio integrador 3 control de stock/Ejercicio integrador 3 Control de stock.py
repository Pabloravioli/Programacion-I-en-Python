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
    
    listaStock = {}
    listaVentas = {}
    
   
    
    for ingreso in ingresos:
        
        codigo, producto, cantidad = ingreso.strip().split(";")
        
        cantidad = int(cantidad)
        
        listaStock[codigo] = {
            
            "Codigo":codigo,
            "Producto":producto,
            "Cantidad":cantidad
            
            }
        
    
    for venta in ventas:
        codigo, producto, cantidad = venta.strip().split(";")
        
        cantidad = int(cantidad)
        
        if codigo not in listaVentas:
        
            listaVentas[codigo] = {
                
                "Codigo":codigo,
                "Producto":producto,
                "Cantidad":cantidad
                
                }
        
        else:
             listaVentas[codigo]["Cantidad"] += cantidad
            
    stockFinal = {}
   
    for dato, detalle in listaStock.items():
        stockFinal[dato] = {
            "Codigo":detalle["Codigo"],
            "Producto":detalle["Producto"],
            "Cantidad":detalle["Cantidad"],
            "Cantidad Final":detalle["Cantidad"]
            
                
                }
            
    for dato, detalle in listaVentas.items():
        
        if dato in stockFinal:
            
            stockFinal[dato]["Cantidad Final"] = stockFinal[dato]["Cantidad"] - detalle["Cantidad"]
            
                
    return list(stockFinal.values())
    
def informarStockNegativo(stockFinal):
    
    stockNegativo = list(filter(lambda stock: stock["Cantidad Final"] < 0, stockFinal))
    
    for stock in stockNegativo:
        
        print(stock)

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
        
        print("1",e)
    
        
        
    
    

def main():
    
    rutaActual = os.path.dirname(__file__)
    
    rutaIngresos = os.path.join(rutaActual,"ingresos.txt")
    
    rutaVentas = os.path.join(rutaActual,"ventas.txt")
    
    try:
        
        with open(rutaIngresos,"r",encoding = "utf-8") as archivoIngresos , open(rutaVentas,"r",encoding = "utf-8") as archivoVentas:
            
            listaStockFinal = generarDiccionarioStockFinal(archivoIngresos,archivoVentas)
        
    except Exception as e:
        
        print("2",e)
        
        
    informarStockNegativo(listaStockFinal)
        
    generarStockFinal(listaStockFinal)
    
    
main()