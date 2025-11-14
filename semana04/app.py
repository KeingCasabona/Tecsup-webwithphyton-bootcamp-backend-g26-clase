from flask import Flask, request
from psycopg import connect
from dotenv import load_dotenv
from os import environ
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

# Lee el archivo .env dentro del proyecto y asigna las variables declaradas
# en ese archivo como variables de entorno:
load_dotenv()


# Validador
class CanchasSchema(Schema):
    # La clase Schema es la encargada de hacer las validaciones de todas las
    # propiedades que definamos en esta clase
    id = fields.Int(load_only=True)
    nombre = fields.Str(required=True)
    disponible = fields.Bool(required=False)


app = Flask(__name__)
conn = connect(environ.get("DATABASE_URL"))


def creacionTablas():
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS canchas (
            id SERIAL PRIMARY KEY,
            nombre TEXT,
            disponible BOOLEAN DEFAULT TRUE
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS reservas(
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            hora_inicio TIME NOT NULL,
            hora_fin TIME NOT NULL,
            adelanto FLOAT,
            total FLOAT NOT NULL,
            cancha_id INT NOT NULL,
            FOREIGN KEY (cancha_id) REFERENCES canchas(id)
        );
        """
    )

    conn.commit()
    cursor.close()


creacionTablas()


@app.route("/canchas", methods=["POST", "GET"])
def gestionCanchas() -> tuple[dict, int]:
    if request.method == "POST":
        data = request.get_json()
        try:

            validador = CanchasSchema()
            dataValidada = validador.load(data)

            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO canchas (nombre, disponible) VALUES (%s, %s) RETURNING *",
                (dataValidada.get("nombre"), dataValidada.get("disponible", True)),
            )
            conn.commit()  # Guardar los cambios de manera permanente
            canchaCreada = cursor.fetchone()
            cursor.close()

            print(canchaCreada)

            return {"message": "Cancha creada exitosamente"}, 201  # Created
        except ValidationError as marshmallowError:
            return {
                "message": "Error al validar la data",
                "content": marshmallowError.args,
            }, 400  # Bad Request (mala solicitud)

    else:
        return {"content": ""}, 200  # Ok


if __name__ == "__main__":
    app.run(debug=True)
