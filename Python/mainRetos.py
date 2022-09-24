
# Retos planteados en el módulo de Python del Máster de Data Analytics de la universidad de EDEM

#################################################
#######           NIVEL FÁCIL            ########
#################################################

#------------------------------------------------
# Reto 1
#------------------------------------------------

import retos.basico.reto1

#------------------------------------------------
# Reto 2
# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
#------------------------------------------------

""" # One line loop

numero_inicial = 2
numero_final = 8

limpar = [ i for i in range(numero_inicial,numero_final) if i%2 ]

print(limpar)

# Nested loop
limpar = list()
for i in range(numero_inicial,numero_final):
    if i%2 :
        limpar.append(i)

print(limpar) """

""" # One line loop function

def impares1line(a,b):
    return [ i for i in range(a,b) if i%2 ]

print(impares1line(2,8))


# Nested loop and condition function

def impares(a,b):
    limpar = list()
    for i in range(a,b):
        if i%2 :
            limpar.append(i)
    return(limpar)

print(impares(2,8)) """



#------------------------------------------------
# Reto 3
# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
#------------------------------------------------


""" # One line loop range 100 to 0
print([i for i in range(100,0,-1)])



# Nested loops range 1 to 100
rev = list()

for i in range(1, 101):
    rev.append(i)

rev.reverse()

print(rev) """



#------------------------------------------------
# Reto 4
# Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
# Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
#------------------------------------------------

""" # One line option

lista = [1,2,3,4,5]

print(lista[len(lista)::-1])

# Reverse option function reversed and method reverse()
print([*reversed(lista)])

lista.reverse()
print(lista) """


""" # One line option function
def invlist(lst):
    return lst[len(lst)::-1]
    
print(invlist([1,2,3,4,5,6]))


# Reverse option function reversed and method reverse() function

def invlist(lst):
    lst.reverse()
    return lst
    
print(invlist([1,2,3,4,5,6])) """



#------------------------------------------------
# Reto 5
# Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", 
# el programa seguirá pidiéndola. Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta 
# que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN"
# y luego terminar.
#
# NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')
#------------------------------------------------



""" while True:
    password = input('Introduce contraseña: ')
    
    if password == 'admin':
        break
    else:
        print('Contraseña incorrecta. Vuelva a intentarlo') """






#------------------------------------------------
# Reto 6
# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
#------------------------------------------------



""" age = int(input('Introduce tu edad: '))

if age >= 18:
    print('Eres mayor de edad')
else:
    print('Te quedan {} años para ser mayor de edad'.format(18-age)) """





#------------------------------------------------
# Reto 7
# Escribe un programa que contenga dos variables. 
# Una de ellas representa la contraseña de un usuario y la otra un texto introducido.
# El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
#------------------------------------------------


# With a program

""" password:str = 'asbcs322#@'
texto:str  = 'asbcs322#@'

if password.lower() == texto.lower():
    print('Ambas string son iguales')
else:
    print('Las dos string son diferentes') """
    
    
# With a function
""" def compara(password,texto):
    
    if password.lower() == texto.lower():
        print('Ambas string son iguales')
    else:
        print('Las dos string son diferentes')


compara('asbcs322#@','asbcs322#@') """


#------------------------------------------------
# Reto 8
# Escribe un programa que pueda decirte si un número (número entero) es primo o no
#------------------------------------------------


""" # With program

n:int = int(input('Introduce numero: '))

num = n
        
if n==1 or n==-1:
    print(f'{n} es primo')
    
elif n==0:
    print('0 no es ni primo ni no primo')
    
        
if n < 0: n*= -1
        
for i in range(2,n):
    
    if n%i == 0 :
        print(f'{num} no es primo')
        break
    else:    
        print(f'{num} es primo') """


""" # With function
 def primo(n):
    
    num = n
    
    if n==1 or n==-1:
        return print(f'{n} es primo')
    elif n==0:
        return print('0 no es ni primo ni no primo')
    
    if n < 0: n*= -1
    
    for i in range(2,n):
        
        if n%i == 0 :
            return print(f'{num} no es primo')
    
    return print(f'{num} es primo')
        

primo(4) """
        

#------------------------------------------------
# Reto 9
# Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
#------------------------------------------------


# Explanation of leap year:

# In the Gregorian calendar, a normal year consists of 365 days. Because the actual length of a sidereal year 
# (the time required for the Earth to revolve once about the Sun) is actually 365.2425 days, a "leap year" of 366 days
# is used once every four years to eliminate the error caused by three normal (but short) years. Any year that is evenly
# divisible by 4 is a leap year: for example, 1988, 1992, and 1996 are leap years.

# However, there is still a small error that must be accounted for. To eliminate this error, the Gregorian calendar stipulates
# that a year that is evenly divisible by 100 (for example, 1900) is a leap year only if it is also evenly divisible by 400.


""" # With program

year:int = int(input('Introduce un año: '))

if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(f'El año {year} es bisiesto')
    
else:
    print(f'El año {year} no es bisiesto')
 """


# With function

""" def bisiesto(year):
    
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    
    else:
        return False
    


bisiesto(1700)    
bisiesto(2000)
bisiesto(2022)
 """








#------------------------------------------------
# Reto 10
# Escribe un programa que guarde en una variable el siguiente contenido:
# {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
#------------------------------------------------

""" variable = {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
contenido = variable['titulo'] + ' ' + variable['aka'] + ' ' + variable['director'] + ' ' + str(variable['año']) + ' ' + variable['país']

print(contenido) """






#------------------------------------------------
# Reto 11
# Escribe un programa que pida al usuario los siguientes datos por consola:
# Título de la película
# Director
# Año
# País
# E introduzca esos valores en una variable GLOBAL llamada "pelicula"
#------------------------------------------------

""" titulo:str = input('Titulo de la película: ')
director:str = input('Director de la película: ')
year:int = int(input('Año de la película: '))
pais:str = input('País de la película: ')

pelicula = {'titulo':titulo, 'director':director, 'año':year, 'pais':pais}

print(pelicula) """




#------------------------------------------------
# Reto 12
# Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
#------------------------------------------------

""" nombres = list()
while True:  
    nombre = input('Introduce nombre alumno (escribe Fin para terminar): ')
    if nombre == 'Fin': 
        break      
    else:
        nombres.append(nombre)
        

print(nombres) """
    







#------------------------------------------------
# Reto 13
# Escribe una función que calcule el área de un triángulo, 
# recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
#------------------------------------------------


""" def areatri(b,h):
    return float(b)*float(h)/2


print(areatri(5.2,3.2))

def areacirc(r):
    import math
    return r**2*math.pi

print(areacirc(5.2)) """



#------------------------------------------------
# Reto 14
# Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
#------------------------------------------------


""" def areacirc(r):
    import math
    return r**2*math.pi


def volcil(r,h):
    return areacirc(r) * h

print(volcil(3.2,5))  """





#------------------------------------------------
# Reto 15
# Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
#------------------------------------------------

""" # One line loop
def nums(lst):
    return [i**2 for i in lst]

print(nums([2,4,5,2,1,2,2]))

# Nested loop
def nums(lst):
    sqlst = list()
    for i in lst:
        sqlst.append(i**2)
    
    return sqlst

print(nums([2,4,5,2,1,2,2])) """




#------------------------------------------------
# Reto 16
# Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
#------------------------------------------------

""" from datetime import date

d1 = date(2013,1,1)
d2 = date(2013,9,13)

print('La diferencia entre {} y {} es de {} días'.format(d2, d1, abs(d2-d1).days)) """





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


""" tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

# Encontrar los elementos de 3 a 5

print(tupla[3:6])

# Encontrar los 6 primeros elementos

print(tupla[:6])

# Muestra la tupla desde el 5 elemento hasta el final

print(tupla[5:])

# Muestra toda la tupla haciendo uso de [:]

print(tupla[:])

# Muestra todos los elementos desde la posición 2 a la 9 de dos en dos

print(tupla[2:10:2])

# Devuelve la tupla con un salto cada 4 elementos

print(tupla[::4])


# Usa un step negativo para mostrar la tupla desde la posición 9 a la 2

print(tupla[9:1:-1]) """


#------------------------------------------------
# Reto 18
# Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. La función debe tener la siguiente firma:
# def eliminar(str, n):
#     # TODO: Esto debes completarlo
#     # Pista, haz uso de [start:end:step]

# # De modo que:
# print(eliminar('Madrid', 0)) #adrid
# print(eliminar('Madrid', 3)) #Madid
# print(eliminar('Madrid', 5)) #Madri
#------------------------------------------------


""" def eliminar(str,n):
    return str[:n]+str[n+1:]


print(eliminar('Madrid', 0)) #adrid
print(eliminar('Madrid', 3)) #Madid
print(eliminar('Madrid', 5)) #Madri """
    
    







#################################################
#######       NIVEL MEDIO/AVANZADO       ########
#################################################





#-------------------------------------#
# Reto 1
# Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock almacenado durante meses, 
# se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.
# Cada disco (usa un diccionario para esto) tendrá:
# Nombre
# Artista
# Año
# Precio
# Género (solo pueden ser de los siguientes)
# Pop
# Electro
# Reggaeton
# Rock
# Metal
# Death Metal
# Black Metal
# Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.
# Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), 
# el dinero que se ahorra el usuario y el coste final de la compra.
#-------------------------------------#
























#-------------------------------------#
# Reto 2
# El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar
# ("Introducir otro elemento al carrito (Si / No)".
# Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.
#-------------------------------------#






















#-------------------------------------#
# Reto 3
# El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:
# si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
# En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
# Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
# Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
# si la persona es menor de 16 años, no tiene que pagar impuestos
# Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de personas** durante un año entero (12 meses)
#-------------------------------------#



















#-------------------------------------#
# Reto 4
# Escribe un programa que almacene lenguajes de programación en una lista.
# El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá responder "sí" o "no" y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la misma pregunta:
# ¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes de la lista.
# Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce o no. Algo así:
# JavaScript: no
# TypeScript: sí
# Python: sí
# Dart: no
#-------------------------------------#



















#-------------------------------------#
# Reto 5
# Escribe un programa que realice lo mismo que el programa del reto 4, pero que elimine de la lista aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce.
#-------------------------------------#


















#-------------------------------------#
# Reto 6
# Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo**
# ** Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda
#-------------------------------------#


















#-------------------------------------#
# Reto 7
# Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios. Al finalizar, deberá mostrar por consola la media de los precios introducidos.
#-------------------------------------#

















#-------------------------------------#
# Reto 8
# Escribe una función que reciba un número entero positivo y devuelva su factorial.
#-------------------------------------#

















#-------------------------------------#
# Reto 9
# Escribe una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
#-------------------------------------#

















#-------------------------------------#
# Reto 10
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
#-------------------------------------#















#-------------------------------------#
# Reto 11
# Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
# NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
# El programa debe mostrar las siguientes opciones para que escoja el usuario:
# (1) Añadir un cliente
# (2) Eliminar cliente por NIF
# (3) Mostrar Cliente por NIF
# (4) Listar TODOS os clientes
# (5) Mostrar ÚNICAMENTE los clientes preferentes
# (6) Finalizar Programa
#-------------------------------------#
















#-------------------------------------#
# Reto 12
# Escribe un script de código que haga al usuario introducir 8 alturas de edificios (deben ser float) y que saque por consola las 3 más altas (haz uso de sorted).
#-------------------------------------#














#-------------------------------------#
# Reto 13
# Escribe un programa que sea capaz de encontrar la diferencia completa entre dos fechas, mostrando días, horas, minutos y segundos.
#-------------------------------------#

















#-------------------------------------#
# Reto 14
# Partiendo de las siguientes cadenas de texto:
# miCodigo = 'print("Hola Mundo")'
# otroCodigo = """
# def multiplicar(x,y):
#     return x*y

# print('Multiplica: 2 * 4: ',multiplicar(2,4))
# """
# Haz uso de exec() para ejecutar ambas operaciones
#-------------------------------------#














#-------------------------------------#
# Reto 15
# Partiendo del siguiente snippet:
# numeros = [10,20,(1,3),30,50,69,(10,20),40]
# cantidad = 0
# Realiza un script que permita encontrar dentro de la lista aquellos elementos que sean tuplas. Cada vez que encuentre una tupla, deberá incrementarse la variable cantidad.
# *** Pista: Haz uso de isinstance()
#-------------------------------------#














#-------------------------------------#
# Reto 16
# Partiendo de la siguiente lista de tuplas:
# miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Actualiza la lista sin aquellas tuplas que estén vacías.
#-------------------------------------#



















#-------------------------------------#
# Reto 17
# Crea un script que pueda mostrar la hora actual en milisegundos
#-------------------------------------#




















#-------------------------------------#
# Reto 18
# A partir de la siguiente lista:
# colores = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# Crea un script que pueda almacenar cada uno de los elementos (tuplas) de la lista en variable1, variable2 y variable3 para después imprimirlas por consola.
#-------------------------------------#

















#-------------------------------------#
# Reto 19
# Escribe un programa capaz de imprimir los próximos tres días a partir de la fecha actual (haz uso de datetime.datetime.today() para obtener la fecha actual).
# Pista: investiga acerca de datetime.timedelta()
#-------------------------------------#

















#-------------------------------------#
# Reto 20
# Haciendo uso de enumerate() muestra por consola cada uno de los caracteres de la palabra Valencia junto al índice de su posición.
#-------------------------------------#


















#-------------------------------------#
# Reto 21
# Haciendo uso de:
# colores = ["Negro", "Rojo", "Marrón", "Amarillo"]
# representacion = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# e investigando acerca de zip() deberás entrelazar ambas listas para obtener un diccionario que tenga la clave color cuyos valores son los de la lista colores y otra clave code que tendrá como valor los datos de la lista representación.
#-------------------------------------#















#-------------------------------------#
# Reto 22
# A partir de:
# listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# miDiccionario = {}
# Realiza una iteración para poder pasar de una lista de tuplas a un diccionario llamado miDiccionario
#-------------------------------------#















#-------------------------------------#
# Reto 23
# Investiga acerca de Counter del módulo collections y haciendo uso del siguiente diccionario, encuentra la moda en las puntuaciones de películas:
# misPeliculas = {'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87}
#-------------------------------------#















#-------------------------------------#
# Reto 24
# Haciendo uso de {:.2%}
# Muestra por consola los valores 0.2564 y -0.253 como porcentajes de dos cifras.
#-------------------------------------#


















#-------------------------------------#
# Reto 25
# Partiendo de la lista:
# comunidades = ["Madrid", "Aragón",
#                     "Valencia", "Cataluña",
#                     "Extremadura", "Castilla y León",
#                     "Castilla La Mancha", "Asturias",
#                     "Murcia", "Cantabria", "País Vasco",
#                     "Andalucia"]
# Crea una función que sea capaz de devolver una lista ordenada según la longitud de su nombre.
#-------------------------------------#















#-------------------------------------#
# Reto 26
# Crea una función que reciba una palabra y sea capaz de devolver una palabra del revés.
#-------------------------------------#











#-------------------------------------#
# Reto 27
# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
#-------------------------------------#









#-------------------------------------#
# Reto 28
# Crea un script que solicite al usuario que escriba una frase que contenga las palabras Madrid y Valencia.
# Una vez lo haya introducido, se debe mostrar la frase, habiendo sustituido Madrid por Valencia y Valencia por Madrid.
# Por ejemplo: Si el usuario introduce Vivo en Madrid y viajo a Valencia la salida del programa debe ser Vivo en Valencia y viajo a Madrid.
#-------------------------------------#














#-------------------------------------#
# Reto 29
# Crea una función capaz de devolver el segundo valor numérico más pequeño de una lista de números
#-------------------------------------#












#-------------------------------------#
# Reto 30
# Investiga acerca de ast y convierte un String en una lista. Es decir, un string que representa una lista literalmente. Puedes usar este ejemplo:
# colores ="['Rojo', 'Verde', 'Blanco']"
# Se trata de una cadena de texto que dentro contiene una lista. La idea es que a través de ast lo conviertas en una lista como tal.
#-------------------------------------#
















##############################################################
####### Code to count the number of excercises done ##########
##############################################################

""" fp=open('EDEM2022\Python\mainRetos.py')
c = 0
nc = 0
for line in fp:
    if line.startswith('#------------------------------------------------'):
        c+=1
    elif line.startswith('#-------------------------------------#'):
        nc += 1
        
print('\nRetos superados:', int(c/2))
print('Retos incompletos: ', int(nc/2),'\n') """