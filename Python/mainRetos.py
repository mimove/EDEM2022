
# Retos planteados en el módulo de Python del Máster de Data Analytics de la universidad de EDEM

#################################################
#######           NIVEL BÁSICO           ########
#################################################

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

from retos.basico.reto1 import contact
 
contact()

#------------------------------------------------
# Reto 2
# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
#------------------------------------------------

""" from retos.basico.reto2 import odd1line

print(odd1line(2,8)) """



#------------------------------------------------
# Reto 3
# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
#------------------------------------------------

""" from retos.basico.reto3 import show100to1

print(show100to1()) """



#------------------------------------------------
# Reto 4
# Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
# Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
#------------------------------------------------

""" from retos.basico.reto4 import invList, invListMethod, invListFunction

print(invList([1,2,3,4,5,6]))

print(invListMethod([1,2,3,4,5,6])) 

print([*invListFunction([1,2,3,4,5,6])])  """

#------------------------------------------------
# Reto 5
# Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", 
# el programa seguirá pidiéndola. Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta 
# que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN"
# y luego terminar.
#
# NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')
#------------------------------------------------

""" from retos.basico.reto5 import correctPass

correctPass() """




#------------------------------------------------
# Reto 6
# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
#------------------------------------------------


""" from retos.basico.reto6 import over18

over18()
 """

#------------------------------------------------
# Reto 7
# Escribe un programa que contenga dos variables. 
# Una de ellas representa la contraseña de un usuario y la otra un texto introducido.
# El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
#------------------------------------------------


""" from retos.basico.reto7 import compare

compare('asbcs322#@','AsBcS322#@')  """


#------------------------------------------------
# Reto 8
# Escribe un programa que pueda decirte si un número (número entero) es primo o no
#------------------------------------------------

""" from retos.basico.reto8 import prime
       

prime(4) 
prime(1) 
prime(0) 
prime(-4)  """


        

#------------------------------------------------
# Reto 9
# Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
#------------------------------------------------


""" from retos.basico.reto9 import leapYear


leapYear(1700)
leapYear(2000)
leapYear(2020)
leapYear(2022)
 """








#------------------------------------------------
# Reto 10
# Escribe un programa que guarde en una variable el siguiente contenido:
# {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
#------------------------------------------------

""" from retos.basico.reto10 import printContent

printContent() """




#------------------------------------------------
# Reto 11
# Escribe un programa que pida al usuario los siguientes datos por consola:
# Título de la película
# Director
# Año
# País
# E introduzca esos valores en una variable GLOBAL llamada "pelicula"
#------------------------------------------------

""" from retos.basico.reto11 import filmData

global pelicula

datos = list(filmData())

pelicula = {'titulo': datos[0], 'director': datos[1], 'año': datos[2], 'país': datos[3] }

print(pelicula) """




#------------------------------------------------
# Reto 12
# Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
#------------------------------------------------

""" from retos.basico.reto12 import namesClass

print(namesClass()) """
    







#------------------------------------------------
# Reto 13
# Escribe una función que calcule el área de un triángulo, 
# recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
#------------------------------------------------


""" from retos.basico.reto13 import areacirc, areatri

b: float = 5.2
h: float = 4.0

print('El área del de base {}cm y altura {}cm es {}cm cuadrados'.format(b, h, areaTri(b,h)))

r: float = 5.2
print(f'El área de un círculo de radio {r}cm es aproximada a 2 decimales {round(areaCirc(r),2)}cm cuadrados')  """




#------------------------------------------------
# Reto 14
# Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
#------------------------------------------------


""" from retos.basico.reto14 import volCil

r: float = 5.2
h: float = 10.0

print('El volumen de un cilindro de radio {}cm y altura {}cm es aproximando con dos decimales {}cm cúbicos'.format(r, h, round(volCil(r,h),2))) """





#------------------------------------------------
# Reto 15
# Escribe una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
#------------------------------------------------

""" from retos.basico.reto15 import nums

print(nums([2,4,5,2,1,2,2])) """




#------------------------------------------------
# Reto 16
# Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
#------------------------------------------------

""" from datetime import date
from retos.basico.reto16 import diffDates

d1 = date(2013,1,1)
d2 = date(2013,9,13)


print('La diferencia entre {} y {} es de {} días'.format(d2, d1, diffDates(d2,d1)))   """





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


""" from retos.basico.reto17 import operTuple

operTuple() """


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

""" from retos.basico.reto18 import eliminate

print(eliminate('Madrid', 0)) #adrid
print(eliminate('Madrid', 3)) #Madid
print(eliminate('Madrid', 5)) #Madri  """
    
    







#################################################
#######       NIVEL MEDIO/AVANZADO       ########
#################################################





#------------------------------------------------
# Reto 1 ****OBLIGATORIO****
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
#------------------------------------------------

""" import pandas as pd
from retos.medio.reto1 import buyMusic
from random import shuffle


df = pd.read_csv('./medio/files_reto1/discos_short.csv')
shortListDiscs = df.to_dict('records') # En el reto11 resuelvo la creación de la lista de diccionarios de otra manera.

shuffle(shortListDiscs)

buyMusic(shortListDiscs) """




#------------------------------------------------
# Reto 2
# El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar
# ("Introducir otro elemento al carrito (Si / No)".
# Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.
#------------------------------------------------

""" from retos.medio.reto2 import reto2

reto2() """


#------------------------------------------------
# Reto 3
# El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:
# si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
# En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
# Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
# Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
# si la persona es menor de 16 años, no tiene que pagar impuestos
# Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de personas** durante un año entero (12 meses)
#------------------------------------------------



""" from retos.medio.reto3 import payTax



listaContribuyentes = [{'edad': 15, 'salario': 7000},
                       {'edad': 72, 'salario': 22000},
                       {'edad': 23, 'salario': 11000},
                       {'edad': 27, 'salario': 15000},
                       {'edad': 34, 'salario': 27000},
                       {'edad': 22, 'salario': 55000},
                       {'edad': 21, 'salario': 48000},
                       {'edad': 56, 'salario': 120000},
                       {'edad': 44, 'salario': 19000},
                       {'edad': 32, 'salario': 14000},
                       {'edad': 27, 'salario': 9000},
                       {'edad': 47, 'salario': 38000},
                       {'edad': 55, 'salario': 48000}]

payTax(listaContribuyentes)


print('\n€€€€€€€€€€€€€€€€€€€€€€€€€€')
print('€€ LISTA CONTRIBUYENTES €€')
print('€€€€€€€€€€€€€€€€€€€€€€€€€€\n')
for i in range(len(listaContribuyentes)):
    print(f'Persona {i}: Edad: {listaContribuyentes[i]["edad"]} Sueldo anual: {listaContribuyentes[i]["salario"]}€ (Salario mensual: {round(listaContribuyentes[i]["salario"]/12,2)}€)  Impuestos a pagar: {listaContribuyentes[i]["impuestos"]}€\n') """



#------------------------------------------------
# Reto 4
# Escribe un programa que almacene lenguajes de programación en una lista.
# El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá responder "sí" o "no" y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la misma pregunta:
# ¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes de la lista.
# Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce o no. Algo así:
# JavaScript: no
# TypeScript: sí
# Python: sí
# Dart: no
#------------------------------------------------

""" from retos.medio.reto4 import programLanguage

languages: list = ['JavaScript', 'TypeScript', 'Python', 'Dart', 'Go', 'React']


print(programLanguage(languages)) """




#------------------------------------------------
# Reto 5
# Escribe un programa que realice lo mismo que el programa del reto 4, pero que elimine de la lista aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce.
#------------------------------------------------

""" 
from retos.medio.reto4 import programLanguage
from retos.medio.reto5 import languageUnknown

languages: list = ['JavaScript', 'TypeScript', 'Python', 'Dart', 'Go', 'React']

userLanguage = programLanguage(languages)

print(languageUnknown(userLanguage)) """





#------------------------------------------------
# Reto 6
# Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo**
# ** Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda
#------------------------------------------------


""" from retos.medio.reto6 import palindrome


print(palindrome()) """




#------------------------------------------------
# Reto 7
# Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios. Al finalizar, deberá mostrar por consola la media de los precios introducidos.
#------------------------------------------------

""" from retos.medio.reto7 import averagePrices


listUser, meanList = averagePrices()


print(f'La lista es: {listUser}. La media de los precios de la lista es: {meanList}€') """









#------------------------------------------------
# Reto 8
# Escribe una función que reciba un número entero positivo y devuelva su factorial.
#------------------------------------------------

# from math import factorial # Already implemented in Python print(factorial(12))

""" from retos.medio.reto8 import factorialNumber

print(factorialNumber(12)) """









#------------------------------------------------
# Reto 9
# Escribe una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
#------------------------------------------------


""" from retos.medio.reto9 import decToBin, binToDec


print(decToBin(25121))





print(binToDec('10001011100111010111010011110000')) """





#------------------------------------------------
# Reto 10
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
#------------------------------------------------



""" from retos.medio.reto10 import maxDiv, minMult


# Web to check result http://www.alcula.com/calculators/math/gcd/#gsc.tab=0


a = 234

b = 0

print('El máximo común divisor entre {} y {} es {}'.format(a, b, maxDiv(a,b)))

print('El mínimo común múltiplo entre {} y {} es {}'.format(a, b, minMult(a,b))) """

#------------------------------------------------
# Reto 11  ****OBLIGATORIO****
# Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
# NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
# El programa debe mostrar las siguientes opciones para que escoja el usuario:
# (1) Añadir un cliente
# (2) Eliminar cliente por NIF
# (3) Mostrar Cliente por NIF
# (4) Listar TODOS os clientes
# (5) Mostrar ÚNICAMENTE los clientes preferentes
# (6) Finalizar Programa
#------------------------------------------------

##########################################################
#################   WITH A MODULE  #######################
##########################################################



""" from retos.medio.reto11 import addCustomer, removeCustomer, showCustomerNIF, showAll, preferCustomer
from time import sleep # Using of sleep to give some time to the user for reading the data

#Creating list of customers to test the program

listCustomers: list = [{'NIF': '55597586P', 'nombre': 'Francisco-Jose', 'apellidos': 'Costas Chaparro', 'telefono': '618-492-937', 'email':'fj.costas@gmail.com','preferente': False},
                 {'NIF': '80325916A', 'nombre': 'Elisabet', 'apellidos': 'Serra Mas', 'telefono': '692-442-735', 'email':'eli-serra@hotmail.com','preferente': True},
                 {'NIF': '76426557H', 'nombre': 'Mirian', 'apellidos': 'Plaza Romero', 'telefono': '625-774-905', 'email':'mirian.plaza@gmail.com','preferente': False},
                 {'NIF': '42158567G', 'nombre': 'Octavio', 'apellidos': 'Enriquez Carrero', 'telefono': '652-954-474', 'email':'ocenca@icloud.com','preferente': False},
                 {'NIF': '01375122K', 'nombre': 'Iago', 'apellidos': 'Mosquera Cabello', 'telefono': '664-969-306', 'email':'iagomosquera96@gmail.com','preferente': True}]

#listCustomers= list()
#Main console of the program

while True:
    try:
        print('\n###############################################')
        print('##          OPCIONES DISPONIBLES             ##')
        print('###############################################')
        print('##                                           ##')
        print('## (1) Añadir un cliente                     ##')
        print('##                                           ##')
        print('## (2) Eliminar cliente por NIF              ##')
        print('##                                           ##')
        print('## (3) Mostrar Cliente por NIF               ##')
        print('##                                           ##')
        print('## (4) Listar TODOS los clientes             ##')
        print('##                                           ##')
        print('## (5) Mostrar los clientes preferentes      ##')
        print('##                                           ##')
        print('## (6) Finalizar Programa                    ##')
        print('##                                           ##')
        print('###############################################\n')
        
        option = int(input('Introduzca el número de la opción: '))
        
        # Conditions depending on user option
        
        if option < 1 or option > 6:
            print('La opción introducida no existe. Vuelva a intentarlo')
            continue
        elif option == 1:
            addCustomer(listCustomers)
            sleep(1)
        elif option == 2:
            removeCustomer(listCustomers)
            sleep(1)
        elif option == 3:
            showCustomerNIF(listCustomers)
            sleep(1)
        elif option == 4:
            showAll(listCustomers)
        elif option == 5:
            preferCustomer(listCustomers)
        elif option == 6:
            print('Programa cerrado correctamente')
            quit()

    except ValueError:
        print('Lo siento, no ha introducido un número')
        continue  """

    

##########################################################
#################   WITH A CLASS  ########################
##########################################################

""" import pandas as pd
from time import sleep # Using of sleep to give some time to the user for reading the data
from retos.medio.models.Clients import Clients



#Creating list of customers to test the program from an existing csv file

listCustomers_df = pd.read_csv('./medio/files_reto11/customers.csv')

customers=list()

keys = list(listCustomers_df.columns) #List with the names of the keys for the dictionary.


for i in range(len(listCustomers_df)):
    
    customers.append(vars(Clients(listCustomers_df[keys[0]][i], listCustomers_df[keys[1]][i], listCustomers_df[keys[2]][i], listCustomers_df[keys[3]][i], listCustomers_df[keys[4]][i] , listCustomers_df[keys[5]][i])))



#Main console of the program

while True:
    try:
        print('\n###############################################')
        print('##          OPCIONES DISPONIBLES             ##')
        print('###############################################')
        print('##                                           ##')
        print('## (1) Añadir un cliente                     ##')
        print('##                                           ##')
        print('## (2) Eliminar cliente por NIF              ##')
        print('##                                           ##')
        print('## (3) Mostrar Cliente por NIF               ##')
        print('##                                           ##')
        print('## (4) Listar TODOS los clientes             ##')
        print('##                                           ##')
        print('## (5) Mostrar los clientes preferentes      ##')
        print('##                                           ##')
        print('## (6) Finalizar Programa                    ##')
        print('##                                           ##')
        print('###############################################\n')
        
        option = int(input('Introduzca el número de la opción: '))
        
        # Conditions depending on user option
        
        if option < 1 or option > 6:
            print('La opción introducida no existe. Vuelva a intentarlo')
            continue
        elif option == 1:
            Clients.addCustomer(customers) 
            newList = pd.json_normalize(customers)
            newList.to_csv('./medio/files_reto11/customers_modified.csv',index=False)   
            sleep(1)
        elif option == 2:
            Clients.removeCustomer(customers)
            newList = pd.json_normalize(customers)
            newList.to_csv('./medio/files_reto11/customers_modified.csv',index=False)
            sleep(1)
        elif option == 3:
            Clients.showCustomerNIF(customers)
            sleep(1)
        elif option == 4:
            Clients.showAll(customers)
        elif option == 5:
            Clients.preferCustomer(customers)
        elif option == 6:          
            print('Programa cerrado correctamente')
            quit()

    except ValueError:
        print('Lo siento, no ha introducido un número')
        continue  """







    


#------------------------------------------------
# Reto 12
# Escribe un script de código que haga al usuario introducir 8 alturas de edificios (deben ser float) y que saque por consola las 3 más altas (haz uso de sorted).
#------------------------------------------------

""" 
import retos.medio.reto12  """







#------------------------------------------------
# Reto 13
# Escribe un programa que sea capaz de encontrar la diferencia completa entre dos fechas, mostrando días, horas, minutos y segundos.
#------------------------------------------------

""" from retos.medio.reto13 import diffDateTime

from datetime import datetime

#######################
# Option 1

date1 = datetime(2017, 12, 28, 23, 14, 55) # Start date before end date
date2 = datetime(2018, 8, 5, 1, 5, 0)

#######################

#######################
# Option 2
#######################

date1 = datetime(2019, 1, 23, 5, 20, 0) # Start date after than end date
date2 = datetime(2015, 8, 30, 20, 55, 55)

#######################

dDays, dHours, dMinutes, dSeconds = diffDateTime(date1, date2)


print(f'La diferencia entre las fechas es de: {dDays} días, {dHours} horas, {dMinutes} minutos y {dSeconds} segundos') """









#------------------------------------------------
# Reto 14
# Partiendo de las siguientes cadenas de texto:
# miCodigo = 'print("Hola Mundo")'
# otroCodigo = """
# def multiplicar(x,y):
#     return x*y

# print('Multiplica: 2 * 4: ',multiplicar(2,4))
# """
# Haz uso de exec() para ejecutar ambas operaciones
#------------------------------------------------


""" import retos.medio.reto14 """





#------------------------------------------------
# Reto 15
# Partiendo del siguiente snippet:
# numeros = [10,20,(1,3),30,50,69,(10,20),40]
# cantidad = 0
# Realiza un script que permita encontrar dentro de la lista aquellos elementos que sean tuplas. Cada vez que encuentre una tupla, deberá incrementarse la variable cantidad.
# *** Pista: Haz uso de isinstance()
#------------------------------------------------


""" import retos.medio.reto15 """












#------------------------------------------------
# Reto 16
# Partiendo de la siguiente lista de tuplas:
# miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Actualiza la lista sin aquellas tuplas que estén vacías.
#------------------------------------------------


""" import retos.medio.reto16 """





#------------------------------------------------
# Reto 17
# Crea un script que pueda mostrar la hora actual en milisegundos
#------------------------------------------------


""" import retos.medio.reto17 """




#------------------------------------------------
# Reto 18
# A partir de la siguiente lista:
# colores = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# Crea un script que pueda almacenar cada uno de los elementos (tuplas) de la lista en variable1, variable2 y variable3 para después imprimirlas por consola.
#------------------------------------------------

""" import retos.medio.reto18 """







#------------------------------------------------
# Reto 19
# Escribe un programa capaz de imprimir los próximos tres días a partir de la fecha actual (haz uso de datetime.datetime.today() para obtener la fecha actual).
# Pista: investiga acerca de datetime.timedelta()
#------------------------------------------------

""" import retos.medio.reto19 """






#------------------------------------------------
# Reto 20
# Haciendo uso de enumerate() muestra por consola cada uno de los caracteres de la palabra Valencia junto al índice de su posición.
#------------------------------------------------



""" import retos.medio.reto20 """





#------------------------------------------------
# Reto 21
# Haciendo uso de:
# colores = ["Negro", "Rojo", "Marrón", "Amarillo"]
# representacion = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# e investigando acerca de zip() deberás entrelazar ambas listas para obtener un diccionario que tenga la clave color cuyos valores son los de la lista colores y otra clave code que tendrá como valor los datos de la lista representación.
#------------------------------------------------


""" import retos.medio.reto21 """







#------------------------------------------------
# Reto 22
# A partir de:
# listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# miDiccionario = {}
# Realiza una iteración para poder pasar de una lista de tuplas a un diccionario llamado miDiccionario
#------------------------------------------------

""" import retos.medio.reto22 """







#------------------------------------------------
# Reto 23
# Investiga acerca de Counter del módulo collections y haciendo uso del siguiente diccionario, encuentra la moda en las puntuaciones de películas:
# misPeliculas = {'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87}
#------------------------------------------------

""" import retos.medio.reto23 """






#------------------------------------------------
# Reto 24
# Haciendo uso de {:.2%}
# Muestra por consola los valores 0.2564 y -0.253 como porcentajes de dos cifras.
#------------------------------------------------


""" import retos.medio.reto24 """





#------------------------------------------------
# Reto 25
# Partiendo de la lista:
# comunidades = ["Madrid", "Aragón",
#                     "Valencia", "Cataluña",
#                     "Extremadura", "Castilla y León",
#                     "Castilla La Mancha", "Asturias",
#                     "Murcia", "Cantabria", "País Vasco",
#                     "Andalucia"]
# Crea una función que sea capaz de devolver una lista ordenada según la longitud de su nombre.
#------------------------------------------------

""" from retos.medio.reto25 import sortLenList, sortLenList1line


comunidades = ["Madrid", "Aragón",
                    "Valencia", "Cataluña",
                    "Extremadura", "Castilla y León",
                    "Castilla La Mancha", "Asturias",
                    "Murcia", "Cantabria", "País Vasco",
                    "Andalucia"]



print(sortLenList(comunidades))

print(sortLenList1line(comunidades)) """






#------------------------------------------------
# Reto 26
# Crea una función que reciba una palabra y sea capaz de devolver una palabra del revés.
#------------------------------------------------

""" from retos.medio.reto26 import wordReverse

print(wordReverse('Hola')) """




#------------------------------------------------
# Reto 27
# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
#------------------------------------------------

""" import retos.medio.reto27 """







#------------------------------------------------
# Reto 28
# Crea un script que solicite al usuario que escriba una frase que contenga las palabras Madrid y Valencia.
# Una vez lo haya introducido, se debe mostrar la frase, habiendo sustituido Madrid por Valencia y Valencia por Madrid.
# Por ejemplo: Si el usuario introduce Vivo en Madrid y viajo a Valencia la salida del programa debe ser Vivo en Valencia y viajo a Madrid.
#------------------------------------------------

""" import retos.medio.reto28 """





#------------------------------------------------
# Reto 29
# Crea una función capaz de devolver el segundo valor numérico más pequeño de una lista de números
#------------------------------------------------


""" from retos.medio.reto29 import secondSmaller

print(secondSmaller([5,2,3,1,5,7,8,9,3,3,1,6,5])) """








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
