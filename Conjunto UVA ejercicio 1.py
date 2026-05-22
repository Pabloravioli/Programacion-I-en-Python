"""

 

En un sistema de administración de personal,
se tienen dos variables para realizar el control de asistencia de cada uno de los empleados de la empresa.
En una de ellas, se almacena en un conjunto la información de los empleados que trabajan en la empresa: 

 

empleados = { "Oliver", "Gabriela", "Irina"} 

 

En una segunda variable, se encuentran parametrizadas los días de la semana y quienes asistieron: 

 

semana = { 

    "lunes" : { "Oliver", "Gabriela", "Irina"}, 

    "martes" : { "Oliver", "Irina"}, 

    "miércoles" : { "Oliver" } 

} 

 

Conociendo dicha información, se deberán elaborar las siguientes funciones (que deben incluir dentro de la misma, operaciones de conjunto en su resolución):  

     

diasAsistenciaPerfecta(empleados, semana): Que retorne una lista con los días que hubo asistencia perfecta (que fueron todos los empleados).
Siguiendo el ejemplo, el resultado debería ser: 

['lunes'] 

 

diasAusencias(empleados, semana): Debe retornar un diccionario, combinando el día con la lista de quienes faltaron por cada día. Siguiendo el ejemplo, el resultado debería ser: 

{'lunes': [], 'martes': ['Gabriela'], 'miércoles': ['Irina', 'Gabriela']} 

    

"""