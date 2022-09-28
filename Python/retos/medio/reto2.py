#-------------------------------------#
# Reto 2
# El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar
# ("Introducir otro elemento al carrito (Si / No)".
# Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.
#-------------------------------------#


def reto2():
    
    dictGroceries: dict = {'producto': [], 'precio':[]}
    while True:
        
        item = input('¿Qué artículo quieres añadir? ')
        
        try:
            price = float(input('¿Qué precio tiene? '))
        except ValueError:
            print('Precio incorrecto, tienes que introducir el precio con decimales')
            continue
        
        
        dictGroceries['producto'].append(item)
        dictGroceries['precio'].append(price)
        
        
        finish = input('¿Quieres terminar? ')
        
        if finish == 'si':
            break
        
    print(dictGroceries)
        