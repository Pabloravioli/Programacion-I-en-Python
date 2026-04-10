#Ejercicio 3 lambda,filter y map

"""5.   Utilizando map, crear un programa que cargue 10 notas de alumnos y, al finalizar,
genere una nueva lista indicando el estado de aprobación (reutilice lo creado en el punto 1 (ejercicio 2))."""

"""9.   Crea una función filtraMayores que acepte una
 lista de números como argumento y devuelva una nueva lista
   con los números mayores que 5. Utiliza la función filter para implementarla."""

 
"""10.  Crea una función dobleSiEsPar que acepte una
lista de números como argumento, devuelva una nueva
lista con cada número multiplicado por dos si es par, y elimine todos los números impares de la lista. Utiliza funciones lambda, map y filter para implementarla."""
def dobleSiEsPar(lista):
    pares = filter(lambda  numero: numero % 2 == 0, lista)
    return list(map(lambda par: par * 2, pares))


def main():
    numeros = [1, 2, 3, 4, 5, 6]
    
    resultado = dobleSiEsPar(numeros)
    
    print(resultado)


main()
 
"""12.  Crea una función ordenaPalabras que acepte
una lista de palabras como argumento, y devuelva
una nueva lista con las palabras ordenadas alfabéticamente en orden inverso. Utiliza funciones lambda, map y sorted para implementarla."""
 
 
"""13.  Crea una función productoPares que acepte
una lista de números como argumento y devuelva el producto
de todos los números pares de la lista. Utiliza la función
reduce y una función lambda para implementarla.
"""
