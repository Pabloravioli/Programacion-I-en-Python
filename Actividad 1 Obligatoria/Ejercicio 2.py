#Ejercicio 2: Dada la siguiente lista numeros=[3,7,10,15,20,25]

#Crear una nueva lista que contenga el doble de cada número. Utilizar listas por comprension

def crear_nueva_lista(lista):

    

    nueva_lista = [numero*2 for numero in lista ]

    return nueva_lista

def main():
   
   lista_numeros=[3,7,10,15,20,25] 
   lista_nueva = crear_nueva_lista(lista_numeros)
   print(lista_nueva)
   
main()

