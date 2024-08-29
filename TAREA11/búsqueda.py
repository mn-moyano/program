#Crear una matriz bidimensional (3x3) con valores numéricos.
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#Búsqueda de un valor específico en la matriz.
valor_buscado = 5

#Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

#Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != -1:
        break
#Verificar
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}. ")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
