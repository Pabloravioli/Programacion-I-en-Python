""" Se tienen las calificaciones de varios conductores:

calificaciones = [4.5, 3.2, 5.0, 2.8, 4.9, 3.5]

Consignas:

Crear una función que:
Use filter + lambda para obtener solo conductores con calificación mayor o igual a 4.

Crear otra función que:
Use map + lambda para convertir las calificaciones en etiquetas:
"Excelente" si ≥ 4.5
"Bueno" si ≥ 3
"Malo" si < 3

Crear otra función que:
Use reduce para calcular el promedio general.

Mostrar:
Lista filtrada
Lista de etiquetas
Promedio
"""

from functools import reduce



def obtener_calificaciones(lista):
    
    lista_de_calificaciones = list(filter(lambda calificacion: calificacion >= 4,lista)) 
    
    return lista_de_calificaciones

"""
    Como se que filter devuelve un objeto que no es lista le tuve que poner list al final y lo parametros que le pase a filter fue la funcion con lambda que tiene condicion
    calificacion mayor o igual a 4 y como segundo fue la lista de que se esta evaluando osea la de los coductores de uade
    
"""

def convertir_calificaciones_en_etiquetas(lista):
    
    lista_de_etiquetas = list(map(lambda calificacion: "Excelente" if calificacion >= 4.5 else "Bueno" if calificacion >= 3 else "Malo", lista))
    
    return lista_de_etiquetas

"""
    Para convertir las calificaciones tambien tuve que convertir en lista lo que devuelve y use map para que le aplique la condicion a cada elemento de la lista
"""    
    

def calcular_promedio_en_general(lista):
    
    
    resultado = reduce(lambda sumador, calificacion: sumador + calificacion, lista)
    
    promedio = resultado/len(lista)
    
    return promedio
    
"""
    Para sacar el promedio hice lambda con dos parametros el primero el sumador y el segundo la calificacion y para reduce
    use como primer para metro la funcion lambda y como segundo la lista para que devuelva solo la suma de lista
    para luego sacar el promedio con el resultado de la suma usando el largo de la lista
"""



def main():
    
    calificaciones = [4.5, 3.2, 5.0, 2.8, 4.9, 3.5]
    
    
    lista_conductores_mayor_o_igual_a_4 = obtener_calificaciones(calificaciones)
    
    print(f"Lista filtrada: \n {lista_conductores_mayor_o_igual_a_4} \n")
    
    
    
    
    lista_de_calificaciones = convertir_calificaciones_en_etiquetas(calificaciones)
    
    print(f"Lista de etiquetas: \n {lista_de_calificaciones} \n")
    
    
    
    promedio_general = calcular_promedio_en_general(calificaciones)
    
    print(f"El promedio general: \n {round(promedio_general,2)} \n")
    
    


main()
    