import random
import faker

# Inicializar Faker
fakeCL = faker.Faker('es_CL')
fakeAr = faker.Faker('es_AR')
fakerBr = faker.Faker('pt_BR')

# Generar clientes
clientes = []
for _ in range(1500):
    if random.random() < 0.27:  # 27% inactivos
        estado = 'inactivo'
    else:
        estado = 'activo'

    # Seleccionar país y generar datos
    pais = random.choice(['Chile', 'Argentina', 'Brasil'])
    
    if pais == 'Chile':
        nombre = fakeCL.first_name().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        apellido = fakeCL.last_name().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        ciudad = fakeCL.city().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N').replace("'", '')
        telefono = fakeCL.phone_number()
        direccion = fakeCL.street_address().replace("\n", ", ").replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        codigo_postal = fakeCL.postcode()
    elif pais == 'Argentina':
        nombre = fakeAr.first_name().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        apellido = fakeAr.last_name().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        ciudad = fakeAr.city().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        telefono = fakeAr.phone_number()
        direccion = fakeAr.address().replace("\n", ", ").replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        codigo_postal = fakeAr.postcode()
    else:  # Brasil
        nombre = fakerBr.first_name().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        apellido = fakerBr.last_name().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        ciudad = fakerBr.city().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        telefono = fakerBr.phone_number()
        direccion = fakerBr.address().replace("\n", ", ").replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n').replace('Ñ', 'N')
        codigo_postal = fakerBr.postcode()

    email = f"{nombre.lower()}_{apellido.lower()}{random.randint(0, 99)}@gmail.com"

    cliente = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'telefono': telefono,
        'direccion': direccion,
        'ciudad': ciudad,
        'codigo_postal': codigo_postal,
        'pais': pais,
        'estado': estado
    }
    clientes.append(cliente)

with open('clientes.sql', 'w', encoding='utf-8') as f:
    f.write("INSERT INTO clientes (nombre, apellido, email, telefono, direccion, ciudad, codigo_postal, pais, estado) VALUES\n")
    for cliente in clientes:
        f.write(f"('{cliente['nombre']}', '{cliente['apellido']}', '{cliente['email']}', '{cliente['telefono']}', "
                f"'{cliente['direccion']}', '{cliente['ciudad']}', '{cliente['codigo_postal']}', "
                f"'{cliente['pais']}', '{cliente['estado']}'),\n")  # Finaliza la instrucción SQL
    f.write(";")

print("Datos exportados a clientes.sql")