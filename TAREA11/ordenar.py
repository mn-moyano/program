#Crear una matriz bidimensional (3x3) con valores numéricos
matriz = [
    [10, 40, 80],
    [50, 70, 20],
    [30, 60, 90]
]
#Ordenar la fila 1 de manera ascendente
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n-1):
        for j in range(n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
#Mostrar matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
#Mostrar matriz original
print("Matriz Original")
mostrar_matriz(matriz)
#Ordenar cada fila de la matriz utilizando bubble sort
for fila in matriz:
    bubble_sort_fila(fila)
#Mostrar matriz ordenada
print("\nMatriz Ordenada por Filas: ")
mostrar_matriz(matriz)



