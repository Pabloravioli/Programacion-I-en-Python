#Ejercicio 4: Dada la siguiente lista numeros=[3,7,10,15,20,25] crear una lista que contenga el número al cuadrado solo si es mayor a 10

def cuadrados_mayores_a_10(numeros):
    return [numero**2 for numero in numeros if numero > 10]


def main():
    numeros = [3, 7, 10, 15, 20, 25]
    
    resultado = cuadrados_mayores_a_10(numeros)
    
    print(resultado)


main()