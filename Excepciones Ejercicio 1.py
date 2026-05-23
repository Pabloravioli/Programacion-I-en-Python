#Excepciones

"""
Desarrollar una funcion para ingresar a traves del teclado un numero.
La funcion rechazara cualquier ingreso invalido de datos utilizando excepciones y mostrara la razon exacta del error.
Devolver el valor ingresado cuando este sea correcto
Escribir tambien un programa que permita probasr el correcto funcionamiento de la misma.


"""


def cargarNumero():
    
    bandera = True
    
    while bandera:
        try:
            return int(input("Ingrese un numero"))
        
        except ValueError as e:
            
            print(e)
            
numero = cargarNumero()

print("El numero ingresado es ", numero)