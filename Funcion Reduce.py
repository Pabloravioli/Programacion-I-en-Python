#Funcion Reduce
from functools import reduce

#Agarra un conjuntos valores lista, tupla etc objeto iteralbe y lo reduce a un objeto
#Osea devuelve una sola cosa 

#Tiene retriccion:

#SIEMPRE DEBE TENER 2 PARAMETRO
#Pertenece al modulo biblioteca osea importar functools

def suma(a,b):
    return a+b

lista = [6,7,8,9]

resultadoSuma = reduce(suma,lista)

print(resultadoSuma)



