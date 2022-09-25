#------------------------------------------------
# Reto 13
# Escribe una función que calcule el área de un triángulo, 
# recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
#------------------------------------------------


#The area of a triangle is base * height / 2
def areatri(b: float,h: float) -> float: return b*h/2


#The area of a circle is pi * radius squared
def areacirc(r: float) -> float:
    from math import pi
    return r**2*pi

