#Este es mi primer programa de codigo

from audioop import reverse


print('Hola mundo')


'''
VARIABLES
'''

user = 'Miguel'

user = 200


print('Hola ', user)

newUser:str = "Pepe"

print(newUser[0:2])

newUser = 3


user = "Juan"


print(f"Hola {user}!")

user = 'Pepe'
edad = 25
print(f"{user} tiene {edad} años")

bienvenida = f"Hola {user}"

print(f"""{bienvenida},
tu edad es {edad}""")





'''
bool
int
float
complex
str
list [ ..., ... ]
tuple  (..., ...)
dict {key:value, key:value, ...:...}
range
set
frozenset
bytes

'''


'''
BOOL
'''

casado: bool = True

print(f'Casado? {casado}')



'''
LIST
'''

miLista = ["Martin", "Juan", "Pablo"]


print(*miLista[0:2])

#print(*miLista)


'''for nombre in range(len(miLista)):
  print(miLista[nombre])'''
  
  

#Lista de la compra con 5 elementos

listaCompra = ['pan', 'leche', 'huevos', 'pescado', 'tomates']


print(f'Los 2 últimos elementos de la lista son', *listaCompra[3:5])

print(f'Los 2 últimos elementos de la lista son 3', *listaCompra[len(listaCompra)-2:])


'''
RANGOS
'''


miRango = range(0,11,2)

print(*miRango)


'''
DICCIONARIO
'''
persona = {'nombre':'Martin', 
           'age':31, 
           'dni':'12345H',
           'casado':True} 


print(persona['dni'])

print(f'El dni de {persona["nombre"]} es {persona["dni"]}')  



'''
SET
'''

misNumeros = [1,2,3,4,5,6,7,8,9,3,2,5,3]

misNumerosNoRepetidos = set(misNumeros)

print(*misNumerosNoRepetidos)
  
  
miOtroSetDeDatos = ["b","a","a","a","b"]

miOtroSetDeDatosSet = set(miOtroSetDeDatos)

print(*miOtroSetDeDatosSet)


# Como ordenar listas

otrosDatosOrdenados = sorted(miOtroSetDeDatos)


print(*otrosDatosOrdenados)

# Como invertir

otrosDatosInvertidos = reversed(miOtroSetDeDatos)

print(*otrosDatosInvertidos)


'''
USER INPUTS
'''


name = input('Dime tu nombre: ')

print(f'Has escrito: {name}')


edad = int(input('¿Cuál es tu edad? '))

print(f'Hola: {name}, tienes {edad} años')



'''
EJERCICIO PARA JUEVES:

Hacer aplicación de consola que vaya pidiendo datos: Nombre, email, contraseña, edad y aceptar. Crear un diccionario del usuario con estos datos
'''


