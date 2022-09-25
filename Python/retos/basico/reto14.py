#------------------------------------------------
# Reto 14
# Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
#------------------------------------------------

def volcil(r: float,h: float) -> float:
    from retos.basico.reto13 import areacirc
    return areacirc(r) * h

 