from flask import Flask
from psycopg import connect
from dotenv import load_dotenv
from os import environ

# Lee el archivo .env dentro del proyecto y asigna las variables declaradas
# en ese archivo como variables de entorno:
load_dotenv()

app = Flask(__name__)
conn = connect(environ.get("DATABASE_URL"))


def creacionTablas():
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS canchas (
        id SERIAL PRIMARY KEY,
        nombre TEXT,
        disponible BOOLEAN DEFAULT TRUE)
    )
        """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS reservas(
        id SERIAL PRIMARY KEY,
        nombre TEXT NOT NULO,
        hora_inicio TIME NOT NULO,
        hora_fin TIME NOT NULO,
        adelanto FLOAT,
        total FLOAT NOT NULO,
        cancha_id INT NOT NULO,
        FOREIGN KEY (cancha_id) REFERENCES cancha(id)
    )
        """
    )

    cursor.execute()
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    app.run(debug=True)
