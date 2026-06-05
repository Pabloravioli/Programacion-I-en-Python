"""

Ejercicio 2: Sistema de Gestion de Biblioteca

Se desea construir un sistema para gestionar el catalogo de libros de una biblioteca. El archivo libros.txt contiene un libro por linea con el siguiente formato:

ISBN;TITULO;AUTOR;ANIO;COPIAS

Ejemplo:

978-0-7432-7356-5;EL ALEPH;BORGES;1949;4

978-0-06-112008-4;CIEN ANIOS;GARCIA MARQUEZ;1967;2

978-950-731-300-7;FICCIONES;BORGES;1944;6
 
Consideraciones:

•   El año y las copias son numeros enteros.

•   Un libro es considerado clasico si fue publicado antes del anio 1980.

•   Un libro tiene alta demanda si tiene menos de 3 copias disponibles.
 
Consignas

1.  Escribir la funcion cargar_libros(nombre_archivo) que lea el archivo y retorne una matriz donde cada fila representa un libro. La funcion debe manejar excepciones e ignorar las lineas vacias o mal formadas. Retornar la matriz completa.

2.  Escribir la funcion mostrar_tabla(matriz) que imprima los libros en formato tabla. Los textos deben mostrarse en mayusculas.

3.  Escribir la funcion buscar_libro(matriz, isbn) que reciba la matriz y un ISBN y retorne la fila del libro si existe, o None si no se encontro.

4.  Escribir la funcion es_clasico(anio) que reciba el anio de publicacion y retorne True si el libro es clasico (publicado antes de 1980) o False en caso contrario.

5.  Escribir la funcion agregar_libro(matriz, isbn, titulo, autor, anio, copias) que incorpore un nuevo libro a la matriz y retorne la matriz actualizada.

6.  Escribir la funcion estadistica(matriz) que recorra la matriz y retorne un diccionario con la siguiente estructura:

{

"cantidad_total": int,

"clasicos": int,

"modernos": int,

"alta_demanda": int,

"promedio_copias": float,

"libro_mas_antiguo": str

}

Donde:

•   cantidad_total: total de libros cargados.

•   clasicos: libros publicados antes de 1980.

•   modernos: libros publicados desde 1980 en adelante.

•   alta_demanda: libros con menos de 3 copias disponibles.

•   promedio_copias: promedio de copias disponibles del catalogo.

•   libro_mas_antiguo: titulo del libro con el menor anio de publicacion.

7.  Escribir la funcion recursiva suma_copias(matriz, indice) que calcule la cantidad total de copias disponibles en la biblioteca usando recursion.

Caso base: si el indice es igual al largo de la matriz, retornar 0.

En cada llamada, sumar las copias del libro en la posicion indice al resultado recursivo.

8.  Escribir la funcion guardar_reporte(matriz, nombre_archivo) que genere un archivo de texto con el siguiente formato por linea:

ISBN;TITULO;COPIAS;ESTADO

El estado puede ser ALTA DEMANDA o DISPONIBLE.

"""
 