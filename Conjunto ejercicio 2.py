import random
"""Crear tres conjuntos:
•  pares: valores pares entre 0 y 100
•  impares: valores impares entre 0 y 100
•  azar: 50 valores al azar entre 0 y 100
Una vez generados los tres conjuntos, deberá realizar
las siguientes acciones:
•  generar dos nuevos conjuntos:
uno con la intersección entre azar y pares;
y azar e impares.
Informe de cada uno de ellos: la cantidad, el valor máximo y mínimo."""




pares = set(range(0, 101, 2))

print(pares)

print()


impares = set(range(1, 101, 2))

print(impares)

conjuntoAzar =set()

while len(conjuntoAzar) < 50:
    conjuntoAzar.add(random.randint(0, 100))

azar_pares = set()
azar_impares = set()

for numero in conjuntoAzar:
    if numero in pares:
        azar_pares.add(numero)

    if numero in impares:
        azar_impares.add(numero)


print("AZAR Y PARES")
print("Cantidad:", len(azar_pares))
print("Máximo:", max(azar_pares))
print("Mínimo:", min(azar_pares))

print()

print("AZAR E IMPARES")
print("Cantidad:", len(azar_impares))
print("Máximo:", max(azar_impares))
print("Mínimo:", min(azar_impares))
