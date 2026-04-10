#Funciones Lambda

#Se usan para crear funciones pequeñas, simples y rapidas, sin nombre y que se usan en el momento

#No se usa cuando la funcion es compleja

#Como se escribe...

#lambda parametro1,p2,p3 pn : expresion

# def calcularDoble(numero):
#     return numero*2
# 
# doble = lambda numero: numero*2
# 
# print(type(doble))
# 
# print(doble(15))


#Comprobar si un numero es par

# esPar = lambda numero : numero%2==0
# 
# print(esPar(4))

#Reciba una cadena y la devuelve invertida

invertir = lambda cadena : cadena[::-1]

print(invertir("teclado"))


#Potencia de un numero. n elevado a m

potencia = lambda base, exponente : base ** exponente

print(potencia(9,9))



#Realizar funciones lambda con argumentos fijos

productosNumeros = (lambda num1, num2, num3 : num1*num2*num3) (14,88,55)

print(productosNumeros)



#Concatenar dos cadenas

cadenaResultante = (lambda cadena1, cadena2 : cadena1 + cadena2) ("todo", "noticias")

print(cadenaResultante)


#lambda con condiciones

mayor = (lambda m, n: m if m>n else n)(55,85)

print(mayor)




