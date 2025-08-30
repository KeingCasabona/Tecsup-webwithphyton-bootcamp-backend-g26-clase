saludo='Bienvenidos al curso de Backend'
print(saludo)
print(type(saludo))

# En python se puede cambiar el contenido de una variable
saludo=20
print(saludo)
print(type(saludo))

# Se puede utilizar comillas simples o dobles como mejor lo desee PERO 
# Se DEBE usar comillas simples cuando dentro hay comillas dobles y viceversa
texto= "Buenos dias con todos! 'Aleluya'"
texto = 'Buenos dias "Juan"'


# Si queremos tener un texto con saltos de lineas entonces usaremos la triple comilla simple o triple comilla doble
dialogo= ''' Ahora, les contare un ejemplo de salto de linea
    esta es una nueva linea
y esta es otra linea
y una ultima más'''
print(dialogo)

curso, mes , dia, habilitado, nota= "Backend","Agosto", 30, True, 14.5
print(curso)

# Str | Int | Float |Boolean
print(type(curso))
print(type(dia))
print(type(habilitado))
print(type(nota))