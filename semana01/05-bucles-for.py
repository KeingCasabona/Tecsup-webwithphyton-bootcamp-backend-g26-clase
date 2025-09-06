alumnos=['Sebastian', 'Jose', 'Paolo', 'Eduardo','Keing','Luis']

# for> itera determinados pasos
# in en el bucle for sirve como asignacion

for nombre_alumno in alumnos:
    if nombre_alumno == 'Paolo':
        # Si quiero saltar la iteracion:
        continue
    print(nombre_alumno)

# Se puede iterar el texto
texto= 'Hoy es fin de mes'
for letra in texto:
    print(letra)

print('-------------------------------')

numero=[10,40,50,60]

for numero in numero:
    # pass indicar que aun no hay logica en este bloque de codigo
    # {}
    pass

print('-------------------------------')

#for tradicional
#desde el 0 hasta menor que 4
for numero in range(4):
    print(numero)

print('-------------------------------')

#range(n)> tope, hasta  que numero va a iterar
# range(n,m)> n numero_inicial
#             m tope
for numero in range(1,7):
    print(numero)

print('-------------------------------')

# range(n,m,i)> n numero_inicial
#               m tope
#               i incrementador o decrementador
for numero in range(5,10,3):
    print(numero)

#bandera: variable que sirve como incrementador para contar
veces_repetidas=0
for numero in range(1,100,2):
    if numero%3==0:
        # incrementando en uno la cantidad del valor que tenia las veces_repetidas
        # veces_repetidas++
        veces_repetidas += 1
        # veces_repetidas =

print('-------------------------------')

# Usando el siguiente texto
texto = 'Hola, mi nombre es Eduardo y me gustaria aprender backend'
# necesito sber cuantas vocales hay en el texto y cuantos espacios tengo
contador_vocales = 0
contador_espacios = 0

for caracter in texto.casefold():
    if caracter in 'aeiou':
        contador_vocales += 1
    elif caracter == " ":
        contador_espacios += 1

print("numero de vocales: ", contador_vocales)
print("numero de espacios: ", contador_espacios)