# crear una matriz tridimensional para la tarea.txt
matriz = [
    [4, 7, 5],
    [1, 10, 3],
    [8, 6, 2]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_file(fila):
    n = len(fila)
    for i in range(n-1):
        for j in range(n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1]=fila[j+1], fila[j] #intercambiar elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_file(fila)

# Mostrar la matriz ordenada
print("\nMatriz ordenada por fila:")
mostrar_matriz(matriz)

