# Notas clases Python (** Utilizar codewars.com para practicar y w3schools.com para tutoriales)

## _Clase 17/09/2022_

En este curso aprendemos las bases de la programación en Python, que es el lenguaje en el que se está centrando todo el desarrollo de data analytics.

Una librería es un conjunto de códigos que ya han hecho otras personas y que tú puedes utilizar.

La importancia de la programación es entender muy bien los fundamentos para adaptarse a los cambios que ocurren cada 2 o 3 años.

Python tiene un tipado débil o inferido. Esto quiere decir que yo puedo cambiar el tipo de variable sin que se produzca un error.

Tipos de nombrar variables:
- Snake case: utilizando _ por ejemplo: new_user
- Camel case: utilizando mayus para cada nueva palabra por ejemplo newUser


Para tipar las variables se utiliza el siguiente comando newUser:str para definir un string. Esto no cambia nada de como se definen las variables en Python, ya que al intérprete le da igual. Para lo que se utiliza es para la documentación del código y que sea mucho más fácil de mantener a largo plazo.

Con el siguiente código es como se puede dar formato e imprimir varias variables en Python. A esto se le llama string template (print(f'..texto...{}'))
```py
user = 'Pepe'
edad = 25
print(f'{user} tiene {edad} años')
user = 'Pepe'
edad = 25
print(f'{user} tiene {edad} años)
```


Para dudas de programación en Python usar StackOverflow

## Tipos de datos en python

| Tipo de dato | Representación en Python |
| ------ | ------ |
| Cadena texto | str |
| Num entero | int |
| Numero decimal | float |
| Booleano | bool |
| Diccionario | {key:value, key:value, ...:...} |
| Tuplas | (..., ..., ...) |
| Listas |  [..., ..., ...] |

Según el estandar que todo el mundo sigue, una variable con todos los caracteres en mayúscula debería ser inmutable. Ejemplo:

```py
NUMERO_PI = 3.1415926
```

Se puede imprimir una lista sin necesidad de hacer un for loop. Esto es muy útil y se hace de la siguiente manera:

```py
miLista:[str] = ["Martin", "Juan", "Pablo"]
print(*miLista)
```


Otro tipo de dato de Python se llama "Iterable" que es cualquier dato que se puede utilizar para iterar. Los datos iterables se pueden utilizar dentro de la función set, que nos elimina los datos repetidos.

```py
misNumeros = [1,2,3,4,5,6,7,8,9,3,2,5,3]
misNumerosNoRepetidos = set(misNumeros)
print(*misNumerosNoRepetidos)
```

Los conceptos de paso por "Valor" y paso por "Referencia" son muy importantes. Por ejemplo, para ordenar una list yo podría hacer:

```py
misNumerosOrdenados = sorted(misNumeros)
```

Sería un paso por "Valor" y no me modifica la lista de misNumeros. Sin embargo, si yo aplico: 

```py
misNumeros.sort()
```

estoy haciendo un paso por "Referencia" y esto modificando mi lista de misNumeros 

<br />
<br />
<br />

## _Clase 22/09/2022_

Todos los lenguajes de programacion estan basados en 3 paradigmas:

 - Programacion estructurada
 - Programacion orientada a objetos
 - Programación funcional (no reutilización de variables)


Hay 2 tipos de condicionales en todo lenguaje de programación (while y if)

Python a nivel de ámbito funciona a través de la tabulación. 

Tipos de operaciones:

 - Asignación
 - Operadores numericos (suma +, resta -, mult *, division /, division entera //, exponente ** y modulo %)
 - Logicos
  



## PALABRAS RESERVADAS DE PYTHON

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

<br />
<br />
<br />


## _Clase 23/09/2022_


La programacion estructurada te permite dar saltos de código. De este modo, podemos cargar a tarvés de modulos otras carpetas de python para ejecutarlas en main.py. Concetpualmente, el software se construye en proyectos reales como si fuese una casa. La arquitectura software (distribución de carpetas) ha ido evolucionando a lo largo de los años. Esto facilita el mantenimiento del código.

Los condicionales if elif y else se utilizan conforme nos convenga. Por ejemplo, se puede usar solo if o solo if y elif:

```py
name = 'Martin'

if name == 'Martin : 
   print(f'Hola {name}')

if name == 'Pedro:
    print(f'Hola {name}')
else:
    print('No me se tu nombre')
```

Al utilizar los : se crea un nuevo ámbito. El código en dicho ámbito (variables, condiciones, etc), solo se ejecutan cuando estamos dentro de dicho ámbito.



While es un bucle que solo se ejecuta si se cumple una condición. Hay que poner cuidado para no crear bucles infinitos como el siguiente:

```py
a = 1

while a==1:
    print('Hello world')
```


Las condiciones tienen que ser suficientemente genéricas para que no dependan de valores individuales que defina el usuario.



<br/>

El condicional switch se utiliza para definir diferentes escenarios y ejecutar codigo en cada caso:

```py
swith(codigo):
    case '001':
        break
    case '010':
        break
    case '100':
        break
```

Esto es muy útil en muchos códigos. Sin embargo, en Python no existe esta logica y hay que reemplazarlos por un if elif else.


<br />

Al haber varios tipos de datos que son iterables, existe el bucle for para poder recorrer estos elementos mediante un numero de iteraciones cerradas. Los bucles for también se pueden detener con un break si se cumple cierta condición.


El bucle for tiene esta estructura:

```sh
for elemento in lista_elementos:
    # ejecuta alguna cosa
```


Las variables iterables del bucle for solo existen dentro del bucle. Por ejemplo:

```sh
listaCompra = ['agua', 'cafe', 'cerveza']


for producto in listaCompra:
  print(f'{producto}')
```

La variable producto al final del bucle tiene el valor de la posición final sobre la que ha iterado.


continue, pass y break son tres controladores de flujo del codigo. Continue hace que se salte al inicio del bucle for, pass haría que continuara con la siguiente linea del bucle, y break rompe el bucle.

Para debuguear se utilizan los puntos de ruptura. Eso quiere decir que el codigo se para en esa linea y no ejecuta más lineas.


<br/>
<br/>
<br/>


## Procedimientos, funciones y métodos
Sirven para implementar líneas de código y poder reutilizarlas a lo largo del programa main.py.

Esto ahorra trabajo, simplifica el codigo, reduce el num de lines y hace que el codigo sea mantenible y extensible (añadir nuevas funcionalidades).


Hay funciones nativas de Pyhton que ya están implementadas en el código.

La estructura para escribir  una función es:

```py
def nombreFuncion(parametros) -> tipo_retorno:
  #declaracion de variables
  #y ejecucion de codigo
```

El tipo_retorno no sirve para nada dentro del código ya que el tipado es inferido en Python. Sin embargo, sirve para documentar el código.


Dependiendo del tipo del dato, el parametro se va a pasar por valor o por referencia. Un entero, un float, un booleano se pasan por valor, es decir, se pasa la variable a la función y no se modifica. Si un parametro lo paso por referencia (lista, cadena, etc.), esto hace referencia a la posición de memoria donde está almacenada, y si que se modifica su valor. Por ejemplo:


```py
def encontrarYQuitar(lista):
    #codigo
    lista.pop()
```

Esto modificaría la variable original lista.


```py
def suma(a, b):
    a += 3
    b +=4

valor1 = 1
valor2 = 2

suma(valor1, valor2)
print(valor1, valor2)
```

En este caso valor1 y valor2 tienen el valor original.



Ejemplo de funcion con Parámetros no tipados:

```py
def miFuncionConParametros(a: str,b: str)->None:    
  print(f"¡{a}, {b}!")  
  
# llamando la función y pasándole algunos parámetros
miFuncionConParametros(a='Hola', b='Mundo')
```

Al indicar que a='Hola' tengo que indicar el resto de parámetros de la funcion con el nombre de las variables definidas en la función.



A una funcion se le puede poner un valor por defecto:

```py
def suma(a,b = 1)
    return a+b

suma(1) # Sumaría 1 + 1
suma(3,4) # Sumaría 3 + 4
suma(a=2) # Sumaría 2 + 1 y no daría error
```


Utilizando un asterísco antes del parámetro, puedo introducir en la funcion al llamarla tantos parametros como quiera:

```py
def miFuncionConMultiplesParametros(*elementos) :    
  for elemento in elementos:        
    print(f"Elemento: {elemento}") 

# llamando la función y pasándole una lista de parámetros
miFuncionConMultiplesParametros([1, 2, 3, 4, 5]) #Un parametro que es una lista
miFuncionConMultiplesParametros(1, 2, 3, 4, 5) #5 parametros valores 1 al 5
```


La funcion enumerate sirve para tratar los parametros de una funcion como una lista. 

```py
def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):       
    numeros[indice] *= 2

# definiendo una variable que se va a pasar por referencia
ns = [10,50,100]
doblar_valores(ns)

print(f"Lista Original Modificada: {ns}") # [20, 100, 200]
```

En el bucle, el valor indice indica la posición de cada numero en la lista números.


**Ofuscación de codigo hace referencia a programar el codigo con nombres de variables de manera que a otro programador le cueste entender.


Copia al vuelo: para evitar que al pasar una lista a una función me modifique la lista, puedo crear una copia previa.

```py
def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):       
    numeros[indice] *= 2
  return numeros

# definiendo una variable que se va a pasar por referencia
ns = [10,50,100]
nsmod = doblar_valores(ns[:])


print(f"Lista Original: {ns}") # [20, 100, 200]
print(f"Lista Modificada: {nsmod}") # [20, 100, 200]
```


En el caso de que no quiera hacer el paso por vuelo con la función, si no modificar la lista que le introduzco, no hace falta hacer un return:


```py
def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):       
    numeros[indice] *= 2


# definiendo una variable que se va a pasar por referencia
ns = [10,50,100]


print(f"Lista Modificada: {ns}") # [20, 100, 200]
```



Todos los codigos están yendo hacia la programación funcional. Esto quiere decir no utilizar variables para no ocupar espacio en memoria. Esto en Python se consigue con las funciones lambda:

```py
al_cuadrado = lambda a: a**2 

# llamando a la función lambda
print(al_cuadrado(2)) # imprimirá un 4
```


Hay métodos y librerias que ya están pre-instaladas en Python, como por ejemplo sys o math. Para instalar librerías que no estén instaladas por defecto, se puede utilizar  pip para instalar librerias. Las versiones de librerias se actualizan con tres números (Mayor, minor y micro). Por ejemplo, la 2.0.0 es una major de la 1.0.0 y la 1.1.0 es un minor de la 1.0.0. Es muy importante saber la version de cada programa/librería que estamos usando, ya que puede que tengamos código escrito que deje de funcionar al cambiar de versión.



Para importar una librería se puede ejecutar el siguiente codigo:

```py
import calendar

print(f'El año 2020 es bisiesto? {calendar.isleap(2020)}')
```

Pero esto importa toda la librería de calendar, lo cual puede no ser eficiente.

Para hacerlo más eficiente se pueden importar solo las funciones que se vaya a utilizar haciendo uso del siguiente codigo:

```py
from calendar import isleap

print(f'El año 2020 es bisiesto? {isleap(2020)}')
```

**Los import se colocan siempre arriba del todo.

<br/>
<br/>
<br/>

## Formatos de Fechas:

```py
import datetime
import calendar


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

print(calendar.month_name[1])
```