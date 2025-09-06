edad=32
# No renemos llaves para definir bloques de codigo
# Tenemos IDENTACION(espaciado) para indicar que ese codigo estara dentro de un bloque

if edad>18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

print('Finaliza del if')
print('-----------------------------------------')


edad=26
if edad >18 and edad>35:
    print('Puedes postular para la presidencia')
# Si queremos agregar una condicional intermedia antes que ingrese al else
elif edad>18:
    print('Eres mayor de edad pero aun no puedes postular a la presidencia')
else:
    print('Eres menor de edad')


#Como saber si un numero es positivo o negativo o si es cero
numero=0
if numero >0:
    print('El número es positivo')
elif numero <0:
    print('El número es negativo')
else:
    print('el número es 0')

print('-----------------------------------------')

# numero_ingresado=input('Ingresa tu numero favorito')

# print(numero_ingresado)
# print(type(numero_ingresado))

# #Para convertir un tipo de dato a otro
# numero_ingresado_int=int(numero_ingresado)
# print(type(numero_ingresado_int))
# print('-----------------------------------------')

#> , < , >= , <= , == (igual que ) , != (diferente que)

# Ingresando el pais indicar la nacionalidad
# Peru> Peruano
# Bolivia> Boliviano
# Holanda> Holandes
# Otro pais que no este registrado qindicar que es Latinoamericano

# Concatenacion de metodos:
pais= input('Ingresa la el pais de nacimiento: ').casefold()

if pais=='peru':
    print('Es peruano')
elif pais=='bolivia':
    print('Es boliviano')
elif pais=='holanda':
    print('Es holandes')
else:
    print('Es latinoamericano')
    
