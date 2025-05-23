# Generador de Datos de para Proyecto de Analisis de Datos

## Índice

1. [Clientes](#clientes)
2. [Tipos de Café](#tipos-de-café)

## Descripción del Script (Clientes)

Este script en Python genera datos ficticios de clientes para tres países: Chile, Argentina y Brasil. Utiliza la biblioteca `Faker` para crear nombres, apellidos, direcciones y otros datos relevantes. Los datos generados se exportan a un archivo SQL que puede ser utilizado para poblar una base de datos.


El script realiza las siguientes acciones:

1. **Importación de Bibliotecas**: Se importan las bibliotecas necesarias, incluyendo `random` y `faker`.

2. **Inicialización de Faker**: Se crean instancias de `Faker` para cada uno de los países (Chile, Argentina y Brasil) con sus respectivas configuraciones locales.

3. **Generación de Clientes**:
   - Se generan 1500 registros de clientes.
   - Cada cliente tiene un estado que puede ser 'activo' o 'inactivo', con un 27% de probabilidad de ser inactivo.
   - Se selecciona aleatoriamente un país y se generan los datos correspondientes (nombre, apellido, ciudad, teléfono, dirección y código postal) utilizando la instancia de `Faker` correspondiente.

4. **Formato de Datos**: Los datos generados se formatean para eliminar caracteres especiales y se preparan para la inserción en una base de datos.

5. **Exportación a SQL**: Los datos de los clientes se escriben en un archivo `clientes.sql` en formato SQL, listo para ser importado a una base de datos.

## Uso

Para ejecutar el script, asegúrate de tener Python y la biblioteca `Faker` instalados. Puedes instalar `Faker` usando pip:

```bash
pip install faker
```
Luego, ejecuta el script:

```bash
python datos2/clientes.py
```
Esto generará un archivo `clientes.sql` en el mismo directorio, que contendrá los datos de los clientes generados.

## Ejemplo de Salida

El archivo `clientes.sql` tendrá un formato similar al siguiente:
``` sql
INSERT INTO clientes (nombre, apellido, email, telefono, direccion, ciudad, codigo_postal, pais, estado) VALUES
('Juan', 'Pérez', 'juan_perez12@gmail.com', '123456789', 'Calle Falsa 123', 'Santiago', '12345', 'Chile', 'activo'),
('María', 'González', 'maria_gonzalez34@gmail.com', '987654321', 'Avenida Siempre Viva 742', 'Buenos Aires', '67890', 'Argentina', 'inactivo'),
...
;
```

## Tipos de Café

Este script en Python genera datos ficticios sobre diferentes tipos de café, incluyendo sus características, origen y temporadas de disponibilidad. Los datos generados se exportan a varios archivos SQL que pueden ser utilizados para poblar una base de datos relacionada con el café.

### Descripción del Script

El script realiza las siguientes acciones:

1. **Definición de Tipos de Café**: Se definen varios tipos de café con sus descripciones, orígenes y temporadas de cosecha.

2. **Generación de Datos**:
   - Se generan datos para 15 tipos de café, incluyendo su nivel de tueste, notas de cata y precio.
   - Se determina si cada tipo de café está disponible según la temporada actual.

3. **Exportación a SQL**: Los datos generados se escriben en tres archivos SQL: `tipos_cafe.sql`, `cafe_origen.sql` y `cafe_temporadas.sql`.

### Ejemplo de Salida

Los archivos SQL generados tendrán un formato similar al siguiente:

```sql
INSERT INTO tipos_cafe (nombre, descripcion, nivel_tueste, notas_cata, precio_base_kg, disponible) VALUES
('Arabica', 'La variedad mas cultivada en el mundo, con un sabor suave y dulce.', 'Medio', 'Frutales, Dulces', 75.00, True),
...
;
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.