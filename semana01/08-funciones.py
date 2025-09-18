def calcular_igv():
    print("Calcular el igv")


# Se pueden agregar parametros y se puede poner valores predeterminados a los parametros,
# si se provee entonces se
# asigna y si no se usa entonces toma el valor predeterminado
def saludar(nombre, saludo="Buenos dias"):
    print(nombre, saludo)


saludar("Juan", "Buenas tardes")
saludar("Pedro")


# Las funciones mayormente se usan para retomar un resultado y este pueda ser almacenado en una variable
# A partir de Python3.12 se puede TIPAR los parametros de la funcion, este tipado
# es DEBIL, es decir, no obliga a pasar ese tipo de dato
def sumar(numero1: int, numero2: int) -> int:
    resultado = numero1 + numero2
    return resultado


# tipado debil
suma = sumar("s", "f")
print(suma)


# Podemos tener funciones que reciban parametros ilimitados
def sumatoria_infinita(*args) -> int:
    suma_total = 0
    for numero in args:
        suma_total += numero
    return suma_total


resultado = sumatoria_infinita(10, 20, 40, 50, 80, 100)

print(resultado)


# kwargs>keyboard arguments
def creacion_persona(**kwargs):
    if "nombre" in kwargs:
        # Podría validar si es que se esta proveyendo una llave incorrecta
        return "Error parametro incorrecto"
    return kwargs


resultado = creacion_persona(nombre="Keing", profesion="desarrollador", mes="Agosto")
print(resultado)
