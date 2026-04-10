#Funciones Map
#A cada objeto de un iterable lo pasa por la funcion osea el primer para metro y el segundo es el iterable
#Recibe dos parametros devuelve un objeto de tipo map

#map(funcion,lista)

numeritos = [44,11,22,9,7]
cuadradoNumeros = []

#Forma clasica

for numerito in numeritos:
    cuadradoNumeros.append(numerito**2)
    
print(cuadradoNumeros)

#Forma Map con lambda

cuadradoMap =list(map(lambda x: x**2, numeritos))

print(cuadradoMap)