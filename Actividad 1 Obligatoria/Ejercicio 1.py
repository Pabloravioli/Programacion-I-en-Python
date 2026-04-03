
#Ejercicio 1:

#Una fábrica registra la cantidad de productos fabricados durante una semana.
#Cada fila representa un día y cada columna un turno (mañana, tarde, noche). La cantidad de días a procesar se le deben solicitar al usuario.

#Ejemplo de matriz:

#[
# [120, 150, 130],
# [110, 140, 125],
# [100, 135, 120]
#]
#Desarrollar los siguientes puntos:

#Crear una función para cargar la matriz con los datos de la producción
#Crear una función para mostrar la matriz 
#Crear una función para mostrar la producción total de la matriz. Es decir la suma de todos los elementos
#Crear una función que muestre la producción por turno. Es decir la cantidad total de elementos producidos en la mañana, en la tarde y en la noche. 
#Crear una función que informe el día de mayor producción
#El programa debe:

#Mostrar la matriz
#Calcular la producción total semanal
#Calcular la producción total por turno
#Determinar qué día tuvo mayor producción
#Mostrar el promedio de producción diaria

#Realice la funcion para cargar matriz y a tambien hice una matriz con turnos para que se muestre bien en el print a que dia corresponde cada fila
  
def cargar_Matriz(numero_de_dias):
    
    matriz_dxt = []
    
    turnos = 3
    
    matriz_turnos = ["Mañana", "Tarde", "Noche"]
    
    for i in range(numero_de_dias):
        
        lista_turnos = []
        
        for j in range(turnos):
            
            print(f"Ingrese la cantidad de productos fabricados en el turno {matriz_turnos[j]} del dia {i+1}: ")
            
            cantidad = int(input())
            
            lista_turnos.append(cantidad)
            
        matriz_dxt.append(lista_turnos)
        
    return matriz_dxt


    
def mostrar_matriz(matriz):
    print("Matriz de dias en filas y turnos en columnas: ")
    dia = 0
    for fila in matriz:
        dia+=1
        print(f" dia {dia} {fila}")
    
def calcular_produccion_semanal(matriz):
    
    suma_total = 0
    
    for fila in matriz:
        
       suma_total += sum(fila)
    
    return suma_total
    
def calcular_produccion_por_turno(matriz,numero_de_dias,turnos):
    
    
    
    lista_de_turnos= []
    
    for i in range(numero_de_dias):
        
        suma_por_turno = 0
        
        for j in range(turnos):
            
            suma_por_turno += matriz[j][i]
            
        lista_de_turnos.append(suma_por_turno)
    
    return lista_de_turnos
            



def calcular_dia_de_mas_produccion(matriz):
    
    lista_de_produccion =[]
    
    lista_de_produccion = [sum(dia) for dia in matriz]
    
    dia_maximo_de_produccion = lista_de_produccion.index(max(lista_de_produccion))
    
    return lista_de_produccion, dia_maximo_de_produccion
    
        
def obtener_promedio_produccion_diaria(matriz,dias):
    
     suma_de_dias = 0
    
     for dia in matriz:
         suma_de_dias += sum(dia)
         
     promedio = suma_de_dias/dias
     
     return promedio
    
    
def main():
        
     turnos = 3
     
     sumador=0
     
     matriz_turnos = ["Mañana", "Tarde", "Noche"]
     
     dias = int(input("Ingrese la cantidad de dias: "))
     
     matriz_semanal = cargar_Matriz(dias)
     
     mostrar_matriz(matriz_semanal)
     
     total_de_produccion = calcular_produccion_semanal(matriz_semanal)
     
     print("\nLa cantidad producida en total es de: " ,total_de_produccion)
     
     produccion_total_por_turno = calcular_produccion_por_turno(matriz_semanal,turnos,dias)
     
     print("\nLista de cada turno con la suma de produccion por turnos: ")
     
     print(produccion_total_por_turno,"\n")
     
     for turno in produccion_total_por_turno:
         
         print(f"El turno {matriz_turnos[sumador]} produjo un total de {turno} unidades")
         
         sumador += 1
         
     lista_dia_por_produccion,dia_con_mayor_produccion = calcular_dia_de_mas_produccion(matriz_semanal)
     
     print(f"\nEl dia de mayor produccion fue el dia {dia_con_mayor_produccion+1} y con una produccion total de {lista_dia_por_produccion[dia_con_mayor_produccion]} unidades ")
     
     
     promedio_diario = obtener_promedio_produccion_diaria(matriz_semanal,dias)
     
     print(f"\n El promedio diario de produccion es de {promedio_diario} unidades")
     
main()
     
     
    