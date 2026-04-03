#Ejercicio 3: Dada la siguiente lista numeros=[3,7,10,15,20,25] crear una lista que contenga solo los números pares


def obtener_pares(numeros):


    pares = [numero for numero in numeros if numero % 2 == 0]

    
    return pares


def main():
    numeros = [3, 7, 10, 15, 20, 25]
    
    resultado = obtener_pares(numeros)
    
    print(resultado)


main()