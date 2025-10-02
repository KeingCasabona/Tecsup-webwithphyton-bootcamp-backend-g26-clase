from flask import Flask

# __name__ variable de python que sirve para indicar si el archivo que estamos utilizando es el
# archivo principal de nuestro proyecto, si lo es entonces el valor sera __main__ sino sera el nombre del
# archivo.
# Flask utiliza el __name__ para crear una sola instancia del servidor en todo el proyecto
# y evitar tener mas de uno por proyecto.
servidor = Flask(__name__)


# DECORADORES: La forma en la cual podemos agregar funcionamiento a un metodo sin la necesidad de modificar
# la clase como tal:
@servidor.route("/")
def bienvenida():
    return "Bienvenido a mi API de Flask"


# frontend 8080
# postgres 5432
# python(flask) 5000
# Tiene que ir al final porque es el encargado de levantar la aplicación y luego de esto se queda en espera
# de nuevas solicitudes:
# debug > Si esta habilitado cada vez que hagamos un cambio se reiniciará la aplicación de manera automática
servidor.run(port=5000, debug=True)
