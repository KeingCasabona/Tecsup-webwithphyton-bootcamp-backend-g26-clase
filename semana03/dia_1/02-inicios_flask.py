from flask import Flask, request

# __name__ variable de python que sirve para indicar si el archivo que estamos utilizando es el
# archivo principal de nuestro proyecto, si lo es entonces el valor sera __main__ sino sera el nombre del
# archivo.
# Flask utiliza el __name__ para crear una sola instancia del servidor en todo el proyecto
# y evitar tener mas de uno por proyecto.
servidor = Flask(__name__)

usuarios = [
    {"nombre": "Gabriel", "correo": "gabi@gmail.com", "apellido": "Farick"},
    {"nombre": "Eliana", "apellido": "chira", "correo": "elinachira@gmail.com"},
]


# DECORADORES: La forma en la cual podemos agregar funcionamiento a un metodo sin la necesidad de modificar
# la clase como tal:
@servidor.route("/")
def bienvenida():
    return "Bienvenido a mi API de Flask"


@servidor.route("/crear-usuario", methods=["POST"])
def crearUsuario():
    # request es toda la informacion que me puede enviar el cliente:
    # get_json > convierte la información enviada en el body a un diccionario para que python la pueda entender:
    print(request.get_json())
    data = request.get_json()
    usuarios.append(data)
    # El formato que vamos a usar para retornar la información será un formato JSON (en python se usa un diccionario)
    return {"message": "Usuario creado exitosamente"}, 201  # Created (Recurso creado)


@servidor.route("/listar-usuarios", methods=["GET"])
def listarUsuarios():
    return {"message": "Los usuarios son", "content": usuarios}


# Tipos de datos de la url solamente se puede utilizar int o float, si es string es implicito, no se necesita
# declararlo: int:correo , float:correo
@servidor.route("/devolver-usuario/<correo>")
def devolverUsuario(correo):
    print(correo)

    # Buscar si el usuario existe con ese correo, si existe devolverlo, sino indicar que no se encontró:
    for usuario in usuarios:
        if usuario["correo"] == correo:
            return {"message": "Usuario encontrado", "content": usuario}

    return {"message": "Usuario no encontrado"}, 200  # ok(TODO BIEN)


@servidor.route("/usuario/<int:id>", methods=["PUT", "DELETE"])
def gestionarUsuario(id):
    request.method  # PUT | DELETE

    if request.method == "PUT":
        # El id va a ser la posicion de la lista -1 (las posiciones comienzan en 0)
        # El if se usa para evitar acceder a una posicion queno existe
        if len(usuarios) >= id:
            data = request.get_json()
            # le restamos 1 al id porque las posiciones empiezan en 0 en las listas
            usuarios[id - 1] = data
            usuario = usuarios[id - 1]
            return {
                "message": "Usuario actualizado exitosamente",
                "content": usuario,
            }, 201
        else:
            return {"message": "Usuario no encontrado"}, 404  # Not found

    elif request.method == "DELETE":

        if len(usuarios) >= id:

            usuario = usuarios.pop(id - 1)
            return {
                "message": "Usuario eliminado exitosamente",
                "content": usuario,
            }, 201
        else:
            return {"message": "Usuario no encontrado"}, 404  # Not found
        # Implementa el método delete reusando parte del codigo del put y eliminar el objeto de la lista


# frontend 8080
# postgres 5432
# python(flask) 5000
# Tiene que ir al final porque es el encargado de levantar la aplicación y luego de esto se queda en espera
# de nuevas solicitudes:
# debug > Si esta habilitado cada vez que hagamos un cambio se reiniciará la aplicación de manera automática
servidor.run(port=5000, debug=True)
