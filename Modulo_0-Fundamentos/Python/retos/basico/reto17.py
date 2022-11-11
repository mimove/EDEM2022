
#------------------------------------------------
# Reto 17
# Partiendo de la siguiente tupla:
# tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# Realiza las siguientes operaciones
# Encontrar los elementos de 3 a 5
# Encontrar los 6 primeros elementos
# Muestra la tupla desde el 5 elemento hasta el final
# Muestra toda la tupla haciendo uso de [:]
# Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
# Devuelve la tupla con un salto cada 4 elementos
# Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
#------------------------------------------------


def operTuple():

    tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

    # Encontrar los elementos de 3 a 5

    print(tupla[2:5])

    # Encontrar los 6 primeros elementos

    print(tupla[:6])

    # Muestra la tupla desde el 5 elemento hasta el final

    print(tupla[4:])

    # Muestra toda la tupla haciendo uso de [:]

    print(tupla[:])

    # Muestra todos los elementos desde la posición 2 a la 9 de dos en dos

    print(tupla[2:10:2])

    # Devuelve la tupla con un salto cada 4 elementos

    print(tupla[::4])


    # Usa un step negativo para mostrar la tupla desde la posición 9 a la 2

    print(tupla[9:1:-1])