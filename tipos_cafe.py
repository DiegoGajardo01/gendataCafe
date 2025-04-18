import random

# Definición de tipos de café y sus características
tipos_cafe = {
    "Arabica": {
        "descripcion": "La variedad mas cultivada en el mundo, con un sabor suave y dulce.",
        "origen": ["Colombia", "Etiopia", "Brasil"],
        'temporadas': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']

    },
    "Robusta": {
        "descripcion": "Mas fuerte y amargo, con un alto contenido de cafeina.",
        "origen": ["Vietnam", "Brasil", "Indonesia"],
        'temporadas': ['Julio', 'Agosto', 'Septiembre', 'Octubre']
    },
    "Excelsa": {
        "descripcion": "Una de las variedades de cafe, con un perfil de sabor unico.",
        "origen": ["Vietnam", "Indonesia"],
        'temporadas': ['Noviembre', 'Diciembre']
    },
    "Liberica": {
        "descripcion": "Una de las variedades de cafe, menos comun pero con un sabor distintivo.",
        "origen": ["Filipinas", "Malasia"],
        'temporadas': ['Enero', 'Febrero', 'Marzo']
    }
}

# Niveles de tueste
niveles_tueste = ['Claro', 'Medio', 'Oscuro']

# Notas de cata
notas_aroma = ['Frutales', 'Floral', 'Terroso', 'Especiadas', 'Avinado']
notas_sabor = ['Nuez/chocolate', 'Dulces', 'Salados', 'Acidos', 'Amargos']

# Generar tipos de café
tipos_cafe_generados = []
cafe_origen_generados = []
cafe_temporadas_generados = []

for _ in range(15):
    tipo = random.choice(list(tipos_cafe.keys()))
    detalles = tipos_cafe[tipo]
    origen = random.choice(detalles['origen'])
    nivel_tueste = random.choice(niveles_tueste)
    notas_cata = random.sample(notas_aroma, 2) + random.sample(notas_sabor, 2)
    precio = round(random.uniform(64000, 88000) / 1000, 2)
    tempActual = ["Marzo", "Abril", "Mayo"]
    if any(mes in tipos_cafe[tipo]["temporadas"] for mes in tempActual):
        disponible = True
    else:
        disponible = False

    cafe = {
        'nombre': tipo,
        'descripcion': detalles['descripcion'],
        'nivel_tueste': nivel_tueste,
        'notas_cata': ', '.join(notas_cata),
        'precio_base_kg': precio,
        'disponible': disponible
    }
    tipos_cafe_generados.append(cafe)

    # Generar datos para cafe_origen
    cafe_origen = {
        'id_tipo_cafe': len(tipos_cafe_generados),  # Asumimos que el ID es el índice + 1
        'pais': origen
    }
    cafe_origen_generados.append(cafe_origen)
    
    # Generar datos para cafe_temporadas
    for mes in detalles['temporadas']:
        cafe_temporada = {
            'id_tipo_cafe': len(tipos_cafe_generados),  # Asumimos que el ID es el índice + 1
            'mes': mes
        }
        cafe_temporadas_generados.append(cafe_temporada)

# Exportar a archivo SQL
with open('tipos_cafe.sql', 'w', encoding='utf-8') as f:
    f.write("INSERT INTO tipos_cafe (nombre, descripcion, nivel_tueste, notas_cata, precio_base_kg, disponible) VALUES\n")
    for cafe in tipos_cafe_generados:
        f.write(f"('{cafe['nombre']}', '{cafe['descripcion']}', '{cafe['nivel_tueste']}', "
                f"'{cafe['notas_cata']}', {cafe['precio_base_kg']}, {cafe['disponible']}),\n")
    f.write(";\n")  # Finaliza la instrucción SQL

with open('cafe_origen.sql', 'w', encoding='utf-8') as f:
    f.write("INSERT INTO cafe_origen (id_tipo_cafe, pais) VALUES\n")
    for origen in cafe_origen_generados:
        f.write(f"({origen['id_tipo_cafe']}, '{origen['pais']}'),\n")
    f.write(";\n")  # Finaliza la instrucción SQL

with open('cafe_temporadas.sql', 'w', encoding='utf-8') as f:
    f.write("INSERT INTO cafe_temporadas (id_tipo_cafe, mes) VALUES\n")
    for temporada in cafe_temporadas_generados:
        f.write(f"({temporada['id_tipo_cafe']}, '{temporada['mes']}'),\n")
    f.write(";\n")  # Finaliza la instrucción SQL

print("Datos exportados a tipos_cafe.sql, cafe_origen.sql y cafe_temporadas.sql")