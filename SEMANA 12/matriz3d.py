# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Baba
        [   # Semana 1
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 90},
            {"day": "Jueves", "temp": 45},
            {"day": "Viernes", "temp": 90},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 68}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 66},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 86},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 94},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 90},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 90}
        ]
    ],
    [   # Esmeraldas
        [   # Semana 1
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 77}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 87},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 76},
            {"day": "Jueves", "temp": 75},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 71},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 71},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 65}
        ]
    ],
    [   # Loja
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 24}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Baba", "Esmeraldas", "Loja"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")