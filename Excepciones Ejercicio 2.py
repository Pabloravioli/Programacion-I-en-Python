#Excepciones

"""
Realizar una funcion que reciba como parametros dos cadenas de caracteres conteniendo numeros reales,
sume ambos valores y devuelva el resultado como un numero real.
Devolver None si alguna de las cadenas no contiene un numero valido,
Utilizando manejo de excepciones para detectar el error.

"""


def sumarCadenas(cadena1,cadena2):
    
    try:
        return int(cadena1) + int(cadena2)
        
    
    except:
        
        return None
    
    
        


def main():
    
    
    primeraCadena = input("Ingrese la primera cadena: ")
    
    segundaCadena = input("Ingrese la segunda cadena: ")
    
    sumaDeCadenas = sumarCadenas(primeraCadena,segundaCadena)
    
    if sumaDeCadenas is None:
        
        print(sumaDeCadenas)
        
        print("Error : ambas cadenas deben ser numero entero!")
        
    else:
        print(sumaDeCadenas)
    
    
    
    
    
main()