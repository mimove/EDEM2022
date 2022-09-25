#------------------------------------------------
# Reto 12
# Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
#------------------------------------------------

def namesClass()->list:
    names: list = list()
    while 'Fin' not in names:  
        names.append(input('Introduce nombre alumno (escribe Fin para terminar): '))
    return names[:-1]
