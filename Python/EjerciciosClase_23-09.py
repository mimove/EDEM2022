 
# EJERCICIO 
#   - Por consola el usuario debe acertar un numero secreto
#   - Si acierta en el primer intento: Sus puntos se suman 5 puntos y se multiplica por 2
#   - Si acierta en el segundo intento: se suman 5 puntos
#   - Si acierta a la tercera se suma 2 puntos
#   - Si falla todas las veces se resta 2 puntos.
 

""" numeroBuscado = 300
intento = 3
puntos = 0

numeroElegido = int(input(f'Intentos restantes: {intento}. Elige un numero: '))

while (numeroElegido != numeroBuscado) and intento > 1:
  intento -= 1
  if numeroElegido > numeroBuscado : 
    numeroElegido = int(input(f'Intentos restantes: {intento}. Elige otro numero más pequeño: ')) 
  else:
    numeroElegido = int(input(f'Intentos restantes: {intento}. Elige otro numero más grande: '))
      

if numeroElegido != numeroBuscado:
  puntos -= 2
  print(f'Te has quedado sin intentos. Has conseguido {puntos} puntos')
elif intento >= 2:
  puntos +=5
  puntos *= intento - 1
  print(f'Has ganado, el numero era {numeroBuscado}. Has conseguido {puntos} puntos')
else:
  puntos += 2    
  print(f'Has ganado, el numero era {numeroBuscado}. Has conseguido {puntos} puntos') """
  
  
 
###################################



# En Python, la estructura es con "elif" y no con "else if

""" miEdad = 45
if (miEdad >= 60):    
  print('Apuntarse al gym')
elif (miEdad < 60 and miEdad > 30):    
  if miEdad == 45:
    print ('Adulto maduro')
  else:
    print('Otro texto')
elif (miEdad == 30):    
  print ('Adulto en su sweet moment')
elif (miEdad < 30 and miEdad >= 18):    
  print ('Adulto joven, todo en orden')
else:    print ('¡A clase!')  """


# Ejemplo de for loop 

""" listaCompra = ['agua', 'cafe', 'cerveza']


for producto in listaCompra:
  print(f'{producto}')
  




lista = [1,2,3,4,5,6,7,8] 
for elemento in lista:    
  if(elemento % 2 == 0):        
    print(f'{elemento} es par')    
  else: 
    continue       
    print(f'{elemento} es impar') """
   
   
""" 
lista = [1,2,3,4,5,6,7,8,9,10]

sumatorio = 0
iteraciones = 0

for numero in lista:
  sumatorio += numero
  iteraciones += 1

print(f'Suma total {sumatorio}. Iteraciones: {iteraciones}') """


""" 

lista = [1,2,3,4,5,6,7,8] 

print(lista)

while (len(lista) > 3):
  lista.pop()
  print(lista) """
  
  
# Función con Parámetros No Tipados

""" def miFuncionConParametros(a: str,b: str)->None:    
  print(f"¡{a}, {b}!")  
  
# llamando la función y pasándole algunos parámetros
miFuncionConParametros(a='Hola', b='Mundo')



# Función con muchos parámetros
def miFuncionConMultiplesParametros(*elementos) :    
  for elemento in elementos:        
    print(f"Elemento: {elemento}") 

# llamando la función y pasándole una lista de parámetros
lista = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(lista) """






# Solicitar por consola al usuario un número
# El programa debe pedir números hasta que el usuario introduzca 
# un año bisiesto


# With function

""" def bisiesto(year):
    
    if year%100 == 0 and year%400 != 0:
        return False
    
    elif year%4 == 0 or year%400 == 0:
        return True
    
    else:
        return False """
    



# Lara, Miguel y Julio

""" def anioBisiesto(year:int)->bool:
  if (year%4 == 0 and year%100!=0) or year%400 == 0: return True
    

anioUsuario = int(input('Introduce un año para saber si es bisiesto: '))


while anioBisiesto(anioUsuario) == None :  anioUsuario = int(input(f'El año {anioUsuario} no es bisiesto, prueba otra vez: '))
  

print(f'El año {anioUsuario} es bisiesto')
 """




# Best practice

""" def leap_year(year: int):  return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

while not leap_year(int(input('introduce año: '))):   print('ese año no es bisiesto')

print('has acertado') """





# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen 
""" def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):   # La funcion enumerate sirve para tratar los parametros de una funcion como una lista.      
    numeros[indice] *= 2 
  return numeros
    

# definiendo una variable que se va a pasar por referencia
ns = [10,50,100]
doblar_valores(ns)

print(f"Lista Original Modificada: {ns}") 
# [20, 100, 200]




nsmod = doblar_valores(ns[:])
print(f"Lista Modificada: {nsmod}") # [20, 100, 200] """




# Para aquellos tipos de datos simples, si queremos el mismo comportamiento# de paso por referencia podemos: 
# SOBRESCRIBIR EL VALOR ORIGINAL CON EL VALOR DE RETURN DE LA FUNCIÓN
""" def doblar_valor(numero):    
  return numero * 2

n = 10
  
n = doblar_valor(n)
print(f"Valor original Modificado: {n}") """





# FUNCIONES LAMBDA: 
# Las funciones Lambda de Python son bastante habituales. 


""" al_cuadrado = lambda a: a**2 

# llamando a la función lambda
print(al_cuadrado(2)) # imprimirá un 4 """



import time

import datetime

import calendar

'''
 - Sacar fecha y hora actual 
 - El día actual
 - El año actual
 - Mes actual
 - Número del mes actual
 - Número de la semana actual
 - Día del año
 - Día del mes
 - Día de la semana
'''


# - Sacar fecha y hora actual 
print(datetime.datetime.today())

print(datetime.datetime.today().strftime('%Y'))

#  - El día actual

print(datetime.datetime.today().day)


#  - Mes actual

print(datetime.datetime.today().strftime('%B'))
print(datetime.datetime.today().strftime('%m'))
print(datetime.datetime.today().month)


# - Número de la semana actual

print(datetime.datetime.today().strftime('%W'))


#  - Día del año

print(datetime.datetime.today().strftime('%j'))

# - Día del mes

print(datetime.datetime.today().strftime('%d'))


# - Día de la semana

print(datetime.datetime.today().strftime('%A'))


# - Nombre dia de la semana
print(calendar.day_name[0])


# - Nombre mes 

print(calendar.month_name[9])


miFecha = '23/09/2022'

print(f'Fecha legible {datetime.datetime.strptime(miFecha,"%d/%m/%Y").timetuple()}')