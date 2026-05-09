"""Definir un conjunto con números enteros entre 0 y 9. 
Luego solicitar valores al usuario y eliminarlos 
del conjunto mediante el método remove, 
mostrando el contenido del conjunto luego de cada eliminación. 
Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar 
errores al intentar quitar elementos inexistentes."""


conjunto = {i for i in range(0,10)}

bandera = True

print(conjunto)

while bandera:

    numeroAeliminar = int(input("Ingrese el numero que desea eliminar"))

    if numeroAeliminar == -1:

        bandera = False
    else:
        try:
            conjunto.remove(numeroAeliminar)
            print("Valor eliminado con exito")
            print(conjunto)
        except KeyError:
            print("Valor no existente")
print("Conjuntoi modificado", conjunto)