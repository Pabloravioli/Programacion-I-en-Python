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
#1.  Escribir la funcion cargar_libros(nombre_archivo) que lea el archivo y retorne una matriz donde cada fila representa un libro. La funcion debe manejar excepciones e ignorar las lineas vacias o mal formadas. Retornar la matriz completa. 
#ISBN;TITULO;AUTOR;ANIO;COPIAS
"""
Consideraciones:

•   El año y las copias son numeros enteros.

•   Un libro es considerado clasico si fue publicado antes del anio 1980.

•   Un libro tiene alta demanda si tiene menos de 3 copias disponibles.
"""
def cargar_libros(nombre_archivo):

    matrizLibros = []
    
    try:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            
            for linea in archivo:
                
                linea = linea.strip()
                
                if linea =="":
                    
                    print("Libro no encontrado")
                    
                else:
                    
                    partes = linea.split(";")
                
                    if len(partes) < 5:
                    
                        print("Informacion de libro incompleta")
                    
                    elif len(partes) == 5:
                    
                        isbn = partes[0]
                    
                        titulo = partes[1]
                    
                        autor = partes[2]
                    
                        anio = int(partes[3])
                    
                        copias = int(partes[4])
                    
                        libro = [isbn,titulo,autor,anio,copias]
                    
                        matrizLibros.append(libro)                
            
    except Exception as e:
        
        print(e)
        
    return matrizLibros


#2.  Escribir la funcion mostrar_tabla(matriz) que imprima los libros en formato tabla. Los textos deben mostrarse en mayusculas.

def mostrar_tabla(matriz):
    
    print(f"{'ISBN':<25} {'TITULO':<15} {'AUTOR':<10} {'ANIO':>25} {'COPIAS':>10}")
    
    print("-"*64)
    
    for libro in matriz:
        
        print(f"{libro[0]:<25} {libro[1]:<15} {libro[2]:<10} {libro[3]:>25} {libro[4]:>10}")
        
    print("#" * 64, "\n")
    
    
#3.  Escribir la funcion buscar_libro(matriz, isbn) que reciba la matriz y un ISBN y retorne la fila del libro si existe, o None si no se encontro.
    
def buscar_libro(matriz, isbn):
    
    for libro in matriz:
        
        if libro[0] == isbn:
            
            return libro
        
    return None

#4.  Escribir la funcion es_clasico(anio) que reciba el anio de publicacion y retorne True si el libro es clasico (publicado antes de 1980) o False en caso contrario.

def es_clasico(anio):
    
    if anio < 1980:
        
        return True 
        
    return False
#5.  Escribir la funcion agregar_libro(matriz, isbn, titulo, autor, anio, copias) que incorpore un nuevo libro a la matriz y retorne la matriz actualizada.

def agregar_libro(matriz, isbn, titulo, autor, anio, copias):

    libroNuevo = [isbn, titulo, autor, anio, copias]
    
    matriz.append(libroNuevo)
    
    print("Libro agregado con exito")
    
    return matriz

"""
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
"""

def estadistica(matriz):
    
    diccionarioLibros={}
    
    cantidad = len(matriz)
    
    clasicos = 0
    
    modernos = 0
    
    copias = 0
    
    sumador = 0
    
    libroMasAntiguo = min(matriz, key=lambda libro: libro[3])
    
    for libro in matriz:
        
        if libro[3] < 1980:
            
            clasicos += 1
            
        else:
            
            modernos += 1
            
        if libro[4] < 3:
            
            copias += 1
            
        sumador += libro[4]
        
    promedio = sumador/cantidad
        
    diccionarioLibros={
        
        "cantidad_total": int(cantidad),

        "clasicos": int(clasicos),

        "modernos": int(modernos),

        "alta_demanda": int(copias),

        "promedio_copias": round(float(promedio),2),

        "libro_mas_antiguo": str(libroMasAntiguo)

        }
    
"""
7.  Escribir la funcion recursiva suma_copias(matriz, indice) que calcule la cantidad total de copias disponibles en la biblioteca usando recursion.

Caso base: si el indice es igual al largo de la matriz, retornar 0.

En cada llamada, sumar las copias del libro en la posicion indice al resultado recursivo.
"""
        
def suma_copias(matriz, indice):
    
    if indice == len(matriz):
        
        return 0
    
    return matriz[indice][4] + suma_copias(matriz, indice+1)


"""
8.  Escribir la funcion guardar_reporte(matriz, nombre_archivo) que genere un archivo de texto con el siguiente formato por linea:

ISBN;TITULO;COPIAS;ESTADO

El estado puede ser ALTA DEMANDA o DISPONIBLE
"""

def guardar_reporte(matriz, nombre_archivo):
    
    try:
        with open(nombre_archivo,"w",encoding = "utf") as archivo:
            
            for libro in matriz:
                
                if libro[4] < 3:
                    
                    estado = "ALTA DEMANDA"
                    
                else:
                    
                    estado = "DISPONIBLE"
                
                linea = f"{libro[0]};{libro[1]};{libro[4]};{estado} \n"
                
                archivo.write(linea)
    
    except Exception as e:
        
        print(e)



def main():
    
    matrizLibros = cargar_libros("libros.txt")
    
    for libro in matrizLibros:
        
        print(libro)
        
    mostrar_tabla(matrizLibros)
    
    isbn = input("Ingrese isbn del libro:")
    
    resultado = buscar_libro(matrizLibros, isbn)
    
    if resultado == None:
        
        print("Libro no encontrado")
        
    else:
        print("Libro encontrado! \n")
        print(f"{resultado[0]} {resultado[1]} {resultado[2]} {resultado[3]} {resultado[4]}")
        anio = int(resultado[3])
        clasicoONo = es_clasico(anio)
        
        if clasicoONo == True:
            
            print("Libro Clasico")
            
        else:
             print("Libro NO Clasico")
            
    print("#" * 64, "\n")
    
    matrizLibro = agregar_libro(matrizLibros,"978-950-731-300-7" , "ndeah", "ravioli", 2015, 3)
    
    for libro in matrizLibros:
        
        print(libro)
        
    print("\n")
        
    print("#" * 64, "\n")
    
    estadistica(matrizLibros)
    
    copiasTotales = suma_copias(matrizLibro, 0)
    
    print("Copias totales en la biblioteca: ",copiasTotales, "\n")
    
    print("#" * 64, "\n")
    
    guardar_reporte(matrizLibros,"reporte_libros.txt" )

main()
 
 
 
 
 
 
 