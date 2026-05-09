#Recursividad 
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
numerito = int(input("Ingrese un numerito"))
print(f"El factorial de {numerito} es {factorial(numerito)}")