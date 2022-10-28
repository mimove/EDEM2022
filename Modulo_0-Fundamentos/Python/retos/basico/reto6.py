#------------------------------------------------
# Reto 6
# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
#------------------------------------------------

def over18():
    age = int(input('Introduce tu edad: '))

    if age >= 18:
        print('Eres mayor de edad')
    else:
        print('Te quedan {} años para ser mayor de edad'.format(18-age))