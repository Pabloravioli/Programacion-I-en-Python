#Los diccionarios no son ordenados
#Clave: valor


alumno ={
    "nombre":"Arnoldo",
    "apellido": "Sanchez",
    "edad":36,
    "esPolicia":False,
    "hobbies": ["Tocar la guitarra","ir al bar", "comer empanadas"]

}
print(alumno)
alumno["universidad"] = "UADE"
alumno["edad"] = 37

print(alumno)

print(len(alumno))

perro = {
    "nombre" :"bobi",
    "raza" : "chihuahua",
    "edad" : 3
}

perro1 = {
    "nombre" :"bobi",
    "raza":"chihuahua",
    "edad": 3,
    

}

if perro==perro1:
    print("Diccionario iguales")

print(perro1["nombre"])


print(perro1.get("Origen","Alemania"))

print(perro1)

print(perro1.items())

for clave , valor in perro1.items():
    print(clave, "-->",valor)

for clave in perro1.keys():
    print(clave)

for clave in perro1.values():
    print(valor)


if("edad" in perro1):
    del perro1["edad"]
    print(perro1)





