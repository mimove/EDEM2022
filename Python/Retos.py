
#------------------------------------------------
# Reto 1
# Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro del archivo main.py crea variables que representen los siguientes datos de un contacto:
# Nombre
# Apellidos
# Edad
# Email
# Teléfono
# Casado (verdadero o falso)
# Con Hijos (verdadero o falso)
# Lista de amigos
# Películas vistas (diccionario con clave y valor. El valor será el título de la película)
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print()
#------------------------------------------------


''' name:str = 'Manuel'
surname:str = 'Lopez'
age:int = 22
email:str = 'manuel.lopez@gmail.com'
phone:int = 666111222
married:bool = False
kids:bool = False
amigos:list = ['Juan', 'Pepe', 'Jose', 'Paco', 'Javi']
films:dict = {'film1':'El señor de los anillos', 'film2':'Harry Potter', 'film3':'Inside Out', 'film4':'Toy Story'}

print(f"""Los datos del contacto son
Nombre: {name}
Apellido: {surname}
Edad: {age}
Email: {email}
Tlf: {phone}
¿Casado?: {married}
¿Hijos?: {kids}
Lista amigos: {amigos}
Películas: {films}""") '''


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

if year%100 == 0 and year%400 != 0:
    print(f'El año {year} no es bisiesto')
    
elif year%4 == 0 or (year%100 == 0 and year%400 == 0):
    print(f'El año {year} es bisiesto')
    
else:
    print(f'El año {year} no es bisiesto')
 """


""" # With function

 def bisiesto(year):
    
    if year%100 == 0 and year%400 != 0:
        return print(f'El año {year} no es bisiesto')
    
    elif year%4 == 0 or (year%100 == 0 and year%400 == 0):
        return print(f'El año {year} es bisiesto')
    
    else:
        return print(f'El año {year} no es bisiesto')
    

    
bisiesto(1700)    
bisiesto(2000)
bisiesto(2022) """









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




#-------------------------------------#
# Reto 12
# Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
#-------------------------------------#

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




#-------------------------------------#
# Reto 16
# Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
#-------------------------------------#






#-------------------------------------#
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
#-------------------------------------#








#-------------------------------------#
# Reto 18
# Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto. La función debe tener la siguiente firma:
# def eliminar(str, n):
#     # TODO: Esto debes completarlo
#     # Pista, haz uso de [start:end:step]

# # De modo que:
# print(eliminar('Madrid', 0)) #adrid
# print(eliminar('Madrid', 3)) #Madid
# print(eliminar('Madrid', 5)) #Madri
#-------------------------------------#













##############################################################
####### Code to count the number of excercises done ##########
##############################################################

fp=open('Python\Retos.py')
c = 0
nc = 0
for line in fp:
    if line.startswith('#------------------------------------------------'):
        c+=1
    elif line.startswith('#-------------------------------------#'):
        nc += 1
        
print('\nRetos superados:', int(c/2))
print('Retos incompletos: ', int(nc/2),'\n')