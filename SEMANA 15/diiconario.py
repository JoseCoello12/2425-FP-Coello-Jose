# Crear un diccionario con información de una persona
informacion_personal = {
    "nombre": "Julia Gama",
    "edad": 25,
    "ciudad": "Santa Ana",
    "profesión": "Modelo"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Esmeraldas"

#Agregar una nueva clave-valor para "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0997493460"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

#Imprimir el diccionario final de pantalla
print("diccionario final:",informacion_personal)

