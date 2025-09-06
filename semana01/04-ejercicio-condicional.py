# Tengo una tienda de ropa Eduardo's clothes
# Tengo ropa con las siguientes caracteristicas:
# Masculino en las tallas XL o L 
# Femenino con talla L o M

# Hacer un programa que recepcione el genero y la talla e indique si tiene o no tiene stock

genero=input('Ingreda el genero: ').casefold()
talla= input('Ingresa la talla: ').casefold()

if genero=='masculino' and talla=='xl':
    print('Hay stock')
elif genero=='masculino' and talla=='l':
    print('Hay stock')
elif genero=='femenino' and talla=='l':
    print('Hay stock')
elif genero=='femenino' and talla=='m':
    print('Hay stock')
else:
    print('No hay stock')

