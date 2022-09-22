
#------------------------------------------------

# EJERCICIO PARA JUEVES:

# Hacer aplicación de consola que vaya pidiendo datos: Nombre, email, contraseña, edad y aceptar. Crear un diccionario del usuario con estos datos

#------------------------------------------------


################################################
#  función para comprobar si contraseña valida #
################################################

def is_valid(password):
    import string
    alpha = set(string.ascii_lowercase + string.ascii_uppercase)
    digits = set(string.digits)
    non_alpha = set('#@%.?!')
    password_chars = set(password)

    # We substract the set of letters (resp. digits, non_alpha)
    # from the set of chars used in password
    # If any of the letters is used in password, this should be
    # smaller than the original set 
    all_classes_used = all([len(password_chars - char_class) != len(password_chars) 
                            for char_class in [alpha, digits, non_alpha] ])

    # We remove all letters, digits and non_alpha from the
    # set of chars composing the password, nothing should be left.
    all_chars_valid = len(password_chars - alpha - digits - non_alpha) == 0

    return all_classes_used and all_chars_valid

################################################

while True:

    name = input('Dime tu nombre: ')

    email = input('Introduce email: ')

    while '@' not in email or '.' not in email:
        print('Email introducido incorrecto: ')
        email = input('Introduce email: ')
        
    from getpass import getpass

    password = getpass(prompt='Introduce contraseña: ')
    
    

    while len(password) < 8 or is_valid(password) == False:
        print('La contraseña tiene que tener al menos 8 caracteres, 1 minúscula, 1 mayúscula, 1 número y un caracter especial')
        password = getpass(prompt='Introduce contraseña: ')
    
    passhow = ''
    for i in range(len(password)):
        if i > 1 and i < len(password) - 2:
            passhow += '*' 
        else:
            passhow += password[i]

    age = 0

    while True: 
        try:
            age = int(input('Introduce tu edad: '))
        except:
            print('Introduce un número')
            continue
        else:
            if age > 5 and age < 100:
                break
            else:
                print('Edad introducida fuera de rango (5 a 100 años)')
            
    
    check = input('¿Estás seguro que los datos son correctos? (Si/No): ')
   
    
    while check.lower() != 'si' and check.lower() != 'no':
        print('Responde con Si o No')
        check = input('¿Estás seguro de que los datos son correctos? (Si/No): ')
        
    if check.lower() == 'si':
        break 
    elif check.lower() == 'no':
        continue
          



datos = {'nombre':name.capitalize(), 'email':email, 'contraseña': passhow, 'edad':age}
        
        

print(f'''Los datos introducidos son:
      Nombre: {datos["nombre"]}
      Email: {datos["email"]}
      Contraseña: {datos["contraseña"]}
      Edad: {datos["edad"]}''')







#  Operadores, condiciones y bucles



'''
PALABRAS RESERVADAS DE PYTHON

- and (operador logico para concatenar condiciones)
- as ()
- assert
- break (para salir de un loop)
- class (para definir un tipo propio. Por ejemplo tipo persona con atributos nombre, apellidos, email, etc. Además tiene unas acciones (o métodos) como comer, caminar, etc.)
- continue (para salir de un bucle)
- def (para definir funciones)
- del
- elif (comprobar otra condición despues de un if)
- else (si ninguna condición se cumple realizar lo siguiente a else)
- except (si falla el codigo de try hacer lo de except)
- exec
- finally (si queremos que si o si se ejecute algo cuando acaba el codigo)
- for (para empezar un bucle)
- global (para definir una variable global para todos los ámbitos)
- if (para definir una condicion)
- import (para importar modulos que se exportan de una libreria)
- in (quiere decir dentro de algo que es iterable)
- is (sirve para saber si un valor es de un tipo u otro)
- lambda 
- nonlocal
- not (para negar una condición)
- or (operador logico para definir que se cumplan una condición u otra)
- pass (para que se salte una iteración)
- raise
- return (para definir lo que queremos que sea el output de una función)
- try (prueba a ejecutar lineas de codigo y ver si da error)
- while (ejecuta el bucle mientras se cumpla cierta condición)
- with 
- yield
- True
- False
- None

'''



a = 0 
b = 1
c = 3


if (a == 0 or b == 1) and c == 3:
  nombre = "martin"

print(nombre)



def suma(a,b):
  return a + b

valor1 = suma(5,2)
valor2 = suma(3,2)

print(f'La suma es {valor1} {valor2}')


a = 1
while a == 1:
  print('yeah')
  a = 2


numeroElegido = int(input('Elige un numero: '))
numeroBuscado = 300
intento = 3

while (numeroElegido != numeroBuscado) and intento > 1:
  if numeroElegido > numeroBuscado :
    intento -= 1
    if intento == 1:
       numeroElegido = int(input(f'Elige otro numero más pequeño, te queda {intento} intento : '))
    else:
      numeroElegido = int(input(f'Elige otro numero más pequeño, te quedan {intento} intentos : '))
    
  elif numeroElegido < numeroBuscado :
    intento -= 1
    if intento == 1:
       numeroElegido = int(input(f'Elige otro numero más grande, te queda {intento} intento : '))
    else:
      numeroElegido = int(input(f'Elige otro numero más grande, te quedan {intento} intentos : '))
    
if intento < 0:
  print('Te has quedado sin intentos')
else:    
  print(f'Has ganado, el numero era {numeroBuscado}')
  
  
operacion_compleja = 33 * 10 + 2 / 5 ** 2
print(f"> Operación 33*10+2/5**2 = {operacion_compleja}")


nombre: str = "Martín"
apellidos: str = "San José de Vicente"

# Concatenación
nombre_completo: str = nombre + " " + apellidos
print(f"> Nombre completo: {nombre_completo}")  

# Repetición
nombre_x5: str = nombre*5
print(f"> Nombre 5 veces: {nombre_x5}")

c: int = 3
d: int = 3
e: int = 4

# Igualdad - Nos devolverá True o False
print(f"> ¿3 y 3 son iguales? {c is d}")
# Operador Identidad
print(f"> ¿3 y 3 son iguales? {c == d}")
print(f"> ¿3 y 4 son iguales? {c is e}") # Operador Identidad


print(f"¿3 mayor que 2? {3 > 2}")



print(f"Verdadero y Verdadero = {True and True}")
print(f"Verdadero y 1 = {True and 1}")
print(f"> Falso y 0 = {False and 0}")


print(f"Not Verdadero = {not True}")
print(f"Not Falso = {not False}")
print(f"Not Falso o Verdadero = {not (False or True)}")

mi_texto:str = "Lorem ipsum dolor sit amet consectetur adipiscing elit dui odio"
mi_sub_texto: str = "amet"
mi_otro_sub_texto: str = "pepito"

print(f"> ¿amet está dentro del mi_texto?: {mi_sub_texto in mi_texto}")
print(f"> ¿pepito no está dentro de mi_texto?: {mi_otro_sub_texto not in mi_texto}")

edad = 30
edad += 1


puntos_obtenidos: int = 0
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
puntos_obtenidos = puntos_obtenidos + 1
print(f"> Los puntos obtenidos actuales son: {puntos_obtenidos}")
puntos_obtenidos += 1
print(f"> Has conseguido otro punto. Ahora tienes: {puntos_obtenidos}")

  
  
  
'''
EJERCICIO 
  - Por consola el usuario debe acertar un numero secreto
  - Si acierta en el primer intento: Sus puntos se suman 5 puntos y se multiplica por 2
  - Si acierta en el segundo intento: se suman 5 puntos
  - Si acierta a la tercera se suma 2 puntos
  - Si falla todas las veces se resta 2 puntos.
'''

