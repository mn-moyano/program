#Crear una matriz 3D con datos diarios del clima de diferentes ciudades
#Primera dimensión: Ciudades (3 ciudades)
#Segunda dimensión: Semanas (4 semanas)
#Tercera dimensión: Días de la semana (7 días)

temperaturas = [
    [ #Ciudad 1
        [ # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 37},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 21}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 41},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 37},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 43},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 46},
            {"day": "Martes", "temp": 47},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 41}
        ]
    ]
]

#Calcular el promedio de temperaturas por semana
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas) :
    for semana_idx, semana in enumerate(ciudad) :
        suma_temperaturas  = sum([dia["temp"] for dia in semana])
        promedio = round(suma_temperaturas/len(semana),2)
        print(f"El promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: es {promedio} ")

