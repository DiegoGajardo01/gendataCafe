import random

# Definición de tipos de café y sus características
tipos_cafe = {
    "Arabica": {
        "descripcion": "La variedad mas cultivada y apreciada a nivel mundial, con un sabor suave, dulce y notas afrutadas o florales. Ideal para quienes prefieren un cafe mas delicado y aromatico.",
        "origen": ["Colombia", "Etiopia", "Brasil"],
    },
    "Robusta": {
        "descripcion": "Con un sabor fuerte, terroso y amargo, esta variedad contiene el doble de cafeina que el Arabica. Es ideal para quienes buscan un cafe mas intenso y con cuerpo.",
        "origen": ["Vietnam", "Brasil", "Indonesia"],
    },
    "Excelsa": {
        "descripcion": "Una variedad exotica con un perfil de sabor complejo, que combina notas frutales, acidas y especiadas. Aporta profundidad y caracter a mezclas especiales.",
        "origen": ["Vietnam", "Indonesia"],
    },
    "Liberica": {
        "descripcion": "Poco comun y con granos de forma irregular, esta variedad se destaca por su sabor unico, con matices florales, ahumados y a veces lenosos. Muy apreciada por su rareza.",
        "origen": ["Filipinas", "Malasia"],
    }
}

# Niveles de tueste
niveles_tueste = ['Claro', 'Medio', 'Oscuro']

# Notas de cata
notas_aroma = ['Frutales', 'Floral', 'Terroso', 'Especiadas', 'Avinado']
notas_sabor = ['Nuez/chocolate', 'Dulces', 'Salados', 'Acidos', 'Amargos']

# Rango de precios base por kilogramo (en CLP)
precio_base_kg = random.randint(64000, 88000)  # 16,000 a 22,000 CLP por 250g

# Generar tipos de café
tipos_cafe_generados = []
for _ in range(15):
    tipo = random.choice(list(tipos_cafe.keys()))
    origen = random.choice(tipos_cafe[tipo]['origen'])
    nivel_tueste = random.choice(niveles_tueste)
    notas_cata = random.sample(notas_aroma, 2) + random.sample(notas_sabor, 2)  # Elegir 2 de cada
    precio = round(precio_base_kg / 1000, 2)  # Convertir a precio por kg

    cafe = {
        'nombre': tipo,
        'origen': origen,
        'descripcion': tipos_cafe[tipo]['descripcion'],
        'nivel_tueste': nivel_tueste,
        'notas_cata': ', '.join(notas_cata),
        'precio_base_kg': precio,
        'disponible': True
    }
    tipos_cafe_generados.append(cafe)

# Imprimir los tipos de café generados
for cafe in tipos_cafe_generados:
    print(cafe)
