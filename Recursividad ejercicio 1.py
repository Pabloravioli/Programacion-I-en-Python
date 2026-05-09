"""Escribir una función que devuelva 
la cantidad de dígitos de un número entero, 
sin utilizar cadenas de caracteres."""


def cantidad_digitos(numero):


    if numero < 10:
        return 1
    else:
        return 1 + cantidad_digitos(numero // 10)
    


print(cantidad_digitos(10))