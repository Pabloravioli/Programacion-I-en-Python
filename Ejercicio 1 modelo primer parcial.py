"""

Sistema de Gestion de Vuelos
Descripcion general
Se desea construir un sistema para gestionar los vuelos de una aerolinea.
El archivo vuelos.txt contiene un vuelo por linea con el siguiente formato:
CODIGO;DESTINO;AEROLINEA;PASAJEROS;PRECIO_TICKET
 
Ejemplo:
AR1001;MIAMI;AEROLINEAS;180;85000
LA2050;MADRID;LATAM;210;120000
IB3300;ROMA;IBERIA;95;98000
 
Consideraciones:
•   Los pasajeros y el precio son numeros enteros.
•   La recaudacion de un vuelo se calcula como: PASAJEROS x PRECIO_TICKET.
•   Un vuelo esta lleno si tiene 200 o mas pasajeros.
Consignas
1.  Escribir la funcion cargar_vuelos(nombre_archivo) que lea el archivo y retorne una matriz donde cada fila representa un vuelo. La funcion debe manejar excepciones e ignorar las lineas vacias o mal formadas. Retornar la matriz completa.
2.  Escribir la funcion mostrar_tabla(matriz) que imprima los vuelos en formato tabla. Los textos deben mostrarse en mayusculas.
3.  Escribir la funcion buscar_vuelo(matriz, codigo) que reciba la matriz y un codigo de vuelo (sin importar mayusculas/minusculas) y retorne la fila del vuelo si existe, o None si no se encontro.
4.  Escribir la funcion calcular_recaudacion(pasajeros, precio_ticket) que calcule y retorne la recaudacion total del vuelo.
5.  Escribir la funcion agregar_vuelo(matriz, codigo, destino, aerolinea, pasajeros, precio_ticket) que incorpore un nuevo vuelo a la matriz y retorne la matriz actualizada.
6.  Escribir la funcion estadistica(matriz) que recorra la matriz y retorne un diccionario con la siguiente estructura:
{
"cantidad_total": int,
"vuelos_llenos": int,
"vuelos_con_lugar": int,
"recaudacion_total": float,
"vuelo_mas_caro": str,
"vuelo_mas_barato": str
}
Donde:
•   cantidad_total: total de vuelos cargados.
•   vuelos_llenos: vuelos con 200 o mas pasajeros.
•   vuelos_con_lugar: vuelos con menos de 200 pasajeros.
•   recaudacion_total: suma de (pasajeros x precio_ticket) de todos los vuelos.
•   vuelo_mas_caro: codigo del vuelo con mayor precio de ticket.
•   vuelo_mas_barato: codigo del vuelo con menor precio de ticket.
7.  Escribir la funcion recursiva suma_pasajeros(matriz, indice) que calcule la cantidad total de pasajeros en todos los vuelos usando recursion.
Caso base: si el indice es igual al largo de la matriz, retornar 0.
En cada llamada, sumar los pasajeros del vuelo en la posicion indice al resultado recursivo.
8.  Escribir la funcion guardar_reporte(matriz, nombre_archivo) que genere un archivo de texto con el siguiente formato por linea:
CODIGO;DESTINO;RECAUDACION;ESTADO
El estado puede ser LLENO o CON LUGAR.
 
 

"""