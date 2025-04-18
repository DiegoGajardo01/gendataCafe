import random

# Definición de tipos de café y sus características
tipos_cafe = {
    "Arabica": {
        "descripcion": "La variedad mas cultivada en el mundo, con un sabor suave y dulce.",
        "origen": ["Colombia", "Etiopia", "Brasil"]
    },
    "Robusta": {
        "descripcion": "Mas fuerte y amargo, con un alto contenido de cafeina.",
        "origen": ["Vietnam", "Brasil", "Indonesia"]
    },
    "Excelsa": {
        "descripcion": "Una de las variedades de cafe, con un perfil de sabor unico.",
        "origen": ["Vietnam", "Indonesia"]
    },
    "Liberica": {
        "descripcion": "Una de las variedades de cafe, menos comun pero con un sabor distintivo.",
        "origen": ["Filipinas", "Malasia"]
    }
}

# Niveles de tueste
niveles_tueste = ['Claro', 'Medio', 'Oscuro']

# Notas de cata
notas_aroma = ['Frutales', 'Floral', 'Terroso', 'Especiadas', 'Avinado']
notas_sabor = ['Nuez/chocolate', 'Dulces', 'Salados', 'Acidos', 'Amargos']

# Generar tipos de café
tipos_cafe_generados = []
for _ in range(10):
    tipo = random.choice(list(tipos_cafe.keys()))
    origen = random.choice(tipos_cafe[tipo]['origen'])
    nivel_tueste = random.choice(niveles_tueste)
    notas_cata = random.sample(notas_aroma, 2) + random.sample(notas_sabor, 2)  # Elegir 2 de cada
    precio = round(random.uniform(64000, 88000) / 1000, 2)  # Precio base por kg entre 64,000 y 88,000 CLP

    cafe = {
        'nombre': tipo,
        'origen': origen,
        'descripcion': tipos_cafe[tipo]['descripcion'],
        'nivel_tueste': nivel_tueste,
        'notas_cata': ', '.join(notas_cata),
        'precio_base_kg': precio,
        'disponible': True,  # Asumimos que todos están disponibles
        'temporadas': tipos_cafe[tipo]['temporadas']  # Añadir temporadas
    }
    tipos_cafe_generados.append(cafe)

# Imprimir los tipos de café generados
for cafe in tipos_cafe_generados:
    print(cafe)
