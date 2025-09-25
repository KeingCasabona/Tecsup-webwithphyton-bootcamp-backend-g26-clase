from faker import Faker
from datetime import date

# Creamos una instancia de nuestra clase
# Instancia: copia de toda la configuracion de la clase que va a ser almacenada en la variable
creador = Faker()


def generar_data_profesores(cantidad):
    texto = "INSERT INTO profesores (nombre, apellidos, correo, correo_institucional, activo, fecha_contratacion) VALUES"

    for numero in range(cantidad):
        nombre = creador.first_name()
        apellidos = creador.last_name()
        correo = creador.email()
        correo_institucional = creador.email(True, "codigo.edu.pe")
        activo = creador.boolean()
        fecha_contratacion = creador.date_between(
            start_date=date(2022, 1, 15), end_date=date(2025, 8, 1)
        )
        data = "('{}','{}','{}','{}',{},'{}'),".format(
            nombre, apellidos, correo, correo_institucional, activo, fecha_contratacion
        )

        # Al ser string no se hara sumatoria sino se realizara una concatenacion
        texto += data
        # En el ultimo registro en vez de colocar na coma se coloque un punto y coma

    resultado = texto.rsplit(",", 1)[0] + ";"
    print(resultado)


# Ejemplo:
# generar_data_profesores(1000)


def generar_data_direcciones(cantidad):
    texto = "INSERT INTO direcciones (calle, numero, referencia, distrito, provincia, profesor_id) VALUES"

    distrito_disponible = [
        "Arequipa",
        "Lima",
        "Jesus Maria",
        "Cuzco",
        "Tacna",
        "Ite",
        "Ito",
        "Trujillo",
    ]
    provincias_disponibles = [
        "Aija",
        "Antonio Raimondi",
        "Asunción",
        "Bolognesi",
        "Carhuaz",
        "Casma",
        "Corongo",
        "Huarmey",
        "Huaylas",
        "Pallasca",
        "Pomabamba",
        "Recuay",
        "Santa",
        "Sihuas",
        "Yungay",
        "Cajamarca",
        "Cajabamba",
        "Celendín",
        "Chota",
        "Contumazá",
        "Cutervo",
        "Hualgayoc",
        "Jaén",
        "San Ignacio",
        "San Marcos",
        "San Miguel",
        "San Pablo",
        "Santa Cruz",
    ]

    for numero in range(cantidad):
        calle = creador.street_name()
        numero = creador.building_number()
        referencia = creador.word()
        distrito = creador.random_element(distrito_disponible)
        provincia = creador.random_element(provincias_disponibles)
        profesor_id = creador.random_int(1, 105)
        data = "('{}','{}','{}','{}','{}',{}),".format(
            calle, numero, referencia, distrito, provincia, profesor_id
        )
        texto += data

    resultado = texto.rsplit(",", 1)[0] + ";"
    print(resultado)


generar_data_direcciones(200)
# Agregando al comando ">" NOMBRE_ARCHIVO.EXT en vez de mostrarlo en la terminal las impresiones de pantalla lo
# guardará en ese archivo definido en la terminal.
# python3 04-generador_data.py > script_data_fake.sql

# Para leer este archivo en la terminal
# Mac | Powershell | GitBash : cat
# CMD (Windows): type
# cat ./script_data_fake.sql | psql -U postgres -d "colegio"
