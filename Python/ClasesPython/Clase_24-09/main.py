
# Ejercicios con librería math

""" import math as m

print(m.cos(2*m.pi))


numero :int = 16

print(f'la raíz cuadrada de {numero} es {m.sqrt(numero)}')
#imprime 4.0

print(f'la raíz cuadrada de {numero} es {m.isqrt(numero)}')
#imprime 4 """



""" from math import sqrt as raiz, isqrt as raiz_entera, cos as coseno, sin, tan


numero :int = 16

print(f'la raíz cuadrada de {numero} es {raiz(numero)}')
#imprime 4.0

from math import*
print(cos(2*pi)) """



# Ejercicios creación de librerías propias


from utilidades.interacciones.cordialidad import saludar, despedida
from utilidades.kpis import puntuacion


import utilidades.interacciones.cordialidad as frases



puntos = puntuacion(5)
 
print(f'{saludar("Pedro")} tu puntuación es de {puntos}')
print(f'{despedida("Pedro")}')








