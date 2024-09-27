#Crear un diccionario de información personal ficticia.
informacion_personal = {"nombre":"José Pérez", "edad": 43, "ciudad":"Quito", "profesión":"Licenciado en Educación"}

#Acceder a ciudad y modificarla
informacion_personal["ciudad"] = "Guayaquil" #Se realiza el cambio de ciudad

#Acceder a profesión y modificarla
informacion_personal["profesión"] = "Doctor" #Se agrega una nueva clave-valor para profesión

#Verificar que existe el valor "teléfono" y si no existe agregarlo
if "teléfono" not in informacion_personal: #Verificar si existe el valor teléfono
    informacion_personal["teléfono"] = "0989875910" #Agregar un teléfono ficticio

#Eliminar el valor edad porque es irrelevante
del informacion_personal["edad"] #Se elimina el valor "edad" porque es irrelevante

#Imprimir el diccionario final
print("El diccionario final es: ") #Finalmente se imprime el diccionario resultante
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")