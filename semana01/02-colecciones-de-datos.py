# Variables que puedan almacenar diferente información

#Lista (Arreglo)
#Modificables y ordenadas
numeros_telefonicos=['104', '105', '974207075', '987453456',"123"]

# En la coleccion de datos  se puede agregar diferentes tipos de datos dentro de sus elementos
numeros_telefonicos.append(False)
numeros_telefonicos.append(10.5)

print(numeros_telefonicos)
print(numeros_telefonicos[0])
# print(numeros_telefonicos[10])
print(numeros_telefonicos[1:2])

#Elementos desde la posicion 2 en adelante
print(numeros_telefonicos[2:])

#Elementos hasta la posicion 2
print(numeros_telefonicos[:2])

#para optener el ultimo elemento usamos valores negativos y asi invierte la lista:
print(numeros_telefonicos[-1])
print('---------------------------------------------')

#Con el metodo pop retiramos el elemento de la lista y  lo podemos almacenar en otra variable
valor_eliminado= numeros_telefonicos.pop(0)
print(valor_eliminado)
print(numeros_telefonicos)
print('---------------------------------------------')

#del Sirve para eliminar variables (liberar espacio en memoria) y tambien se puede eliminar elementos de una list
del numeros_telefonicos[1]
print(numeros_telefonicos)
print('---------------------------------------------')

#Si se requiere limpiar completamente la lista 
numeros_telefonicos.clear()
print(numeros_telefonicos)
print('---------------------------------------------')


ejercicio_1= [1, 'Eduardo', 'de Rivero', False, 32 , 20.5, [4,8,12]]

#Como hago par obtener a 'de Rivero'
print(ejercicio_1[2])

#Como hago para obtener desde Eduardo hasta 32
print(ejercicio_1[1:5])

#Como hago para obtener la penultima posicion 20.5
print(ejercicio_1[-2])

#Como hago para obtener el valor 8
print(ejercicio_1[-1][1])
print(ejercicio_1[6][1])

