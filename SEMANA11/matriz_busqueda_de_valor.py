# crear una matriz bidimensional (2x2) para la tarea.txt
matriz = [
    [8, 2, 7],
    [5, 3, 1],
    [4, 6, 10]
]

# busqueda de un valor especifico en la matriz
valor_buscado = 7
if any(valor_buscado in file for file in matriz):
    print(f"Se encontro {valor_buscado} en la matriz")
else:
    print(f"No se encontro {valor_buscado} no se encontro en la matriz.")
    