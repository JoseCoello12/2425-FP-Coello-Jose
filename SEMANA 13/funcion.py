def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario con el nombre de las ciudades y las temperaturas de las 4 semanas
ciudades_temperaturas = {
    "Baba": [75.29, 80.86, 82.86, 84],
    "Esmeraldas": [76.29, 78.42, 71.86, 69.43],
    "loja": [28.43, 24.71, 27, 22.71]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados finales
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")