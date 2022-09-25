#------------------------------------------------
# Reto 11
# Escribe un programa que pida al usuario los siguientes datos por consola:
# Título de la película
# Director
# Año
# País
# E introduzca esos valores en una variable GLOBAL llamada "pelicula"
#------------------------------------------------


def filmData()->dict:
    title:str = input('Titulo de la película: ')
    director:str = input('Director de la película: ')
    year:int = int(input('Año de la película: '))
    country:str = input('País de la película: ')
    
    return title, director, year, country

    
