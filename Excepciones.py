#Excepciones 

"""
try:
    #Código que puede generar una excepción
except TipoDeExcepción:
    #Código para manejar la excepción
else:
    #Código que se ejecuta si no se genera ninguna excepción
finally:
    #Código que se ejecuta siempre, haya o no haya una excepción
"""

numero1 = 10
numero2 = 0
""""


try:
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

"""

try:
    resultado = numero1/numero2
except ZeroDivisionError as e:
    print(f"{e}")
else:
    print("Operacion Finalizada")
    
    
    
    
