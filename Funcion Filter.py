#funcion Filter

#Filter

#Devuelve un objeto filter

#devuelve un booleano 

#Filter(funcion ,lista)

#Forma clasica

numeros = [1,2,3,4,5,6,7,8,9]

pares = []

for numero in numeros:
    if numero%2 == 0:
        pares.append(numeros)
print(pares)

parecitos = list(filter(lambda numerito : numerito%2 ==0, numeros))

print(parecitos)

edades = [7,88,76,56,44,33,99,22,17,18,19,16]

mayor18 = list(filter(lambda edad : edad >18,edades))

print(mayor18)









