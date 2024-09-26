#Crear un diccionario de información personal ficticia.
informacion_personal = {"nombre":"José", "edad": 43, "ciudad":"Quito", "profesión":"Licenciado en Educación"}
informacion_personal["ciudad"] = "Guayaquil" #Se realiza el cambio de ciudad
informacion_personal["ocupación"] = "Docente" #Se agrega una nueva clave-valor para profesión
print(informacion_personal.get("teléfono", "No existe el valor teléfono")) #Se verifica que exista el valor "teléfono"
print("Se añade al diccionario el valor teléfono") #Escribo un mensaje que indique que se agregó dicho valor

#Agregar un número de teléfono ficticio
informacion_personal["teléfono"] = "0989875910"
del informacion_personal["edad"] #Se elimina el valor "edad" porque es irrelevante
print("El diccionario final es: ", informacion_personal) #Finalmente se imprime el diccionario resultante