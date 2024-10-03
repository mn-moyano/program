#Abrir el archivo y escribir en él
nombre_archivo = "my_notes.txt"
archivo_escritura = open(nombre_archivo, "w")
archivo_escritura.write("Linea 1: Realizar tareas. \n")
archivo_escritura.write("Linea 2: Hacer evaluaciones. \n")
archivo_escritura.write("Linea 3: Tareas de casa. \n")

#Metodo writelines(): escribir una lista de lineas
lineas = ["Linea 4: Estamos realizando una prueba. \n", "Linea 5: Escribiendo en archivos con Python. \n"]
archivo_escritura.writelines(lineas)

#Cerrar el archivo
archivo_escritura.close()

#Abrir y leer el archivo read()
archivo_lectura = open("my_notes.txt", "r")
print("Método 1: read()")
print(archivo_lectura.read())
archivo_lectura.close() #No olvidar cerrar archivo

#Abrir y leer el archivo readlines()
archivo_lectura = open("my_notes.txt", "r")
print("Método 2: readlines()")
for linea in archivo_lectura.readlines():
    print(linea.rstrip("\n"))
archivo_lectura.close()

#Leemos y mostramos el contenido después de escribir
archivo_lectura = open("my_notes.txt", "r")
contenido = archivo_lectura.read()
print("\nContenido del archivo después de escribir:")
print(contenido)
archivo_lectura.close()


