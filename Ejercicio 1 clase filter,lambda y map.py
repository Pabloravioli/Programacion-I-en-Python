#Ejercicio 1 clase filter,lambda y map

#Realizar una funcion que a partir de una lista de numeros en minuscula los devuelva en mayuscula. 
 
#Realicen una funcion que a la lista resultante del punto anterior a cada elemento le calcule la longitud y me devuelva una listas con las longitudes
 
#Realizar un afuncion que a partir de la lista de nombres original, me devuelva los nombres que tienen un largo superior a 5. 

#Falta completa punto 2 y 3
 
def pasaListaAMayuscula(lista):
     
     
     nuevaLista =[]
     nuevaLista = list(map(lambda letra: letra.upper(), lista))
        
     return nuevaLista
    
    
def main():
    palabras = ["a", "b", "c"]
    
    listaResultado = pasaListaAMayuscula(palabras)
    
    print(listaResultado)


main()
