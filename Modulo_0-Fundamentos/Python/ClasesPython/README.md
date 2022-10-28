# Notas clases Python 

(** Utilizar codewars.com para practicar y w3schools.com para tutoriales. Kaggle para obtener datos y practicar.)


<br/>
<br/>

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

<br/>

<br/>

<br/>

## _Clase 24/09/2022_


Existen librerías que contienen paquetes y estos a su vez contienen módulos con funciones. Esto nos sirve para poder organizar nuestro código.


Las librerías suelen ser externas a nuestro proyecto. La diferencia entre una librería y un framework es que la librería la instalas y te ofrece una serie de funcionalidades que antes no tenía, mientras que el framework hace lo mismo que la librería, pero te impone una forma de trabajar. Ejemplos de framework son Django o Flask. Sirven para utilizar Python en otro tipo de proyectos. Django se utiliza por ejemplo para construir páginas web.

<br />

## Buenas prácticas

Tener siempre los import en primber lugar, luego las funciones y luego el scripting. El orden de los import va de más genérico a menos genérico:

```py
import <nombre modulo1>
import <nombre modulo2>
.
.
.
from <nombre modulo3> import <nombre funcion1> <nombre funcion2>
from <nombre modulo4> import <nombre funcion>
.
.
.


def <nombre funcion1>(<variables>):
  .
  .
  .

  return <output>

def <nombre funcion2>(<variables>):
  .
  .
  .

  return <output>
.
.
.


# El resto del script aquí
.
.
.

```


Todo esto después se carga en main.py.


Uno de las librerías que más usaremos es request, que sirve para hacer peticiones a paginas http y https para obtener datos. Por ejemplo, utilizando la función get en la página [randomuser.me][df1]  puedo obtener datos de un usuario generado aleatoriamente.




Si quiero cargar todo un modulo puedo ejecutar lo siguiente:

```py
from <modulo> import*
```


Esto nos posibilita utilizar las funciones del modulo sin poner el nombre del modulo antes. Ejemplo

```py
import math as m

print(m.cos(2*m.pi))
```

```py
from math import*
print(cos(2*pi))
```

No obstante, esta manera de importar no está recomendada, ya que puede haber módulos que tengan los mismos nombres en las funciones.


Cuando tenemos un proyecto de cierto tamaño, se suele crear un archivo requirements.txt donde se encuentran todas las librerias que hay que instalar junto con la versión de las mismas que se utiliza. Después, el usuario simplemente tiene que hacer un pip install requirements.txt para installar esas librerías requeridas.







Los módulos se almacenan en archivos .py y los paquetes se organizan en carpetas. Los modulos pueden ir dentro de los paquetes. Los paquetes hay que inicializarlos utilizando un archivo que se llama `__init__.py` . Los `__init__` también se pueden utilizar en clases para inicializar funciones. Los archivos `__init__.py` pueden estar vacíos, pero lo normal es añadirles algunos import.

La forma de importar paquetes, subpaquetes y modulos es:



```py
# Este es el programa main.py
from utilidades.interacciones.cordialidad import saludar, despedida
from utilidades.kpis import puntuacion


#import utilidades.interacciones.cordialidad as ut

puntos = puntuacion(5)
 
print(f'{saludar("Pedro")} tu puntuación es de {puntos}')
print(f'{despedida("Pedro")}')
```

Esto lo que importa es las funciones saludar y despedida, del módulo cordialidad, del subpaquete (carpeta) interacciones que está dentro del paquete utilidades. Y también importa la función puntuación, que está dentro de módulos kpis del paquete utilidades.



<br>
<br>

## _Clase 30/09/2022_

<br>

## **Librerías externas**

Muchas de las librerías están centradas en estadística, matemáticas, tratamiento de datos big data o machine learning. TensorFlow por ejemplo está centrada en desarrollo de Machine Learning. Otro ejemplo es Scikit-Learn. En tercer lugar estarías Keras y en cuarto PyTorch. 


La librería requests es de las que más vamos a usar para obtener datos de url. Para obtener los datos se hace:

```py
import requests

requests.get('URL')
```

En Python esto se puede definir como:

```py
URL_BASE = 'https://api.chucknorris.io/'

endPoint = 'jokes/random'
```

Esta función devuelve un tipo de objeto que se llama Response, que se ha creado en una clase.

Las URLs continen una base y un endpoint. Por ejemplo, la URL <https://api.chucknorris.io/jokes/random> su base sería <https://api.chucknorris.io/> y el endpoint jokes/random.


<br>

## **Clases**

Las clases pueden tener métodos (funciones) que son propias de dicho objeto. Al crear objetos estoy "creando" un nuevo tipo de dato


En este ejemplo:

```py
import requests

def obtenerChiste():

  URL = 'https://api.chucknorris.io/jokes/random'
  
  respuesta = requests.get(url = URL)

  

  # Extraemos los datos en formato JSON

  datos = respuesta.json()
  
  # Obtenemos valor en la clave 'value' del JSON que nos interesa
  
  frase_chuck: str = datos['value']

  return frase_chuck
```

La clase Response se almacena en respuesta, y respuesta.json() es un método que nos devuelve un json de la URL. En el caso de Python los json son equivalentes a diccionarios, y por lo tanto se pueden acceder a sus valores haciendo uso de sus claves como en datos['value']


Para poder usar tipos de datos de clases y poder tipar mi código, necesito hacer uso de lo siguiente:

```py

from requests.models import Response

URL = 'https://api.chucknorris.io/jokes/random'
  
respuesta: Response = requests.get(url = URL)

```

Esto ayuda a documentar el código y poder utilizar funciones de editores como Visual Studio Code para autocompletar los parámetros que necesita la función.


<br>
<br>


## Creación de Objetos. Programación orientada a objetos

La programación orientada a objetos es uno de los tres paradigmas esenciales de la programación y está presente en todos los lenguajes modernos.

Se utiliza para estructurar nuestros datos y reutilizar el código que planteemos. Si necesitamos crear una variable más compleja que listas, diccionarios o tuplas crear clases es una de las mejores opciones.

Los objetos tiene atributos y métodos. Un ejemplo de ambos sería:

```py
respuesta = requests.get(url = URL)

respuesta.json() # Esto es un método (función) del objeto respuesta

respuesta.status_code # Esto es un atributo (variables) del objeto respuesta
```

Las esctructuras internas (atributos y métodos) de la clase pueden ser privadas (solo se puede hacer en el ámbito de la clase) o públicas (pueden verse desde dentro y fuera de la clase).

Un ejemplo podría ser un coche, que tiene como atributos marca, modelo, color, matricula, id del seguro, titular y velocidad, por ejemplo. En cuanto a los métodos, podrían ser arrancar, frenar o acelerar.

Al proceso de creación de clases se le llama modelado de datos y es una de las primeras fases imprescindibles cuando se plantea el diseño de una aplicación.

Antes de crear una clase, se suele hacer un gráfico para establecer el nombre, variables y métodos de la clase. Esto se crea utilizando una herramienta que se llama UML. 


Una clase solo hay que crearla si tiene tanto atributos como métodos, si solo tiene atributos no tiene sentido.

Ejemplo de objeto:

```py
# COCHE

# Atributos

marca: str
modelo: str
color: str
# .
# .
# .

# -------------------

# Métodos

arrancar(): None
frenar(): None
acelerar(): None
```



Cuando nosotros instanciamos una clase, estamos creando un objeto. Por ejemplo el objeto de tipo Coche se instanciaría así:

```py
coche1: Coche =
coche2: Coche =
```

A partir de este momento coche1 y coche2 no son una variable normal, son un objeto de una clase.


Al instanciar estamos reservando espación de memoria para gestionar los atributos y métodos de esa clase.


Las clases tienen un método constructor y un método destructor. El constructor otorga valores a los atributos de la clase e inicializarlo. La sintaxis es:

```py
class Nombre:
  atributo_1: tipo
  atributo_2: tipo

  def __init__(self, _propiedades):
    self_atributos = _propiedades

  def metodo_1(self):
    # codigo
  
  def metodo_2(self):
    # codigo
```


Las best practices es poner los atributos siempre arriba y los métodos debajo.


_Ejemplo clase Alumno_:

```py
class Alumno:
  nombre: str
  email: str

  def __init__(self, n, e): # Constructor
    self.nombre = n # Self hace referencia a acceder al atributo dentro del método
    self.email = e
  

  def asistir_clase(self,id): # (self) es necesario llamarlo para poder acceder a los atributos

    print(f'{self.nombre} ha asistido a clase') # Accedo al nombre del alumno con {self.nombre}
    #codigo

  
  def horas_perdidas(id):
    self.asistir_clase(1) # Los atributos (self) se pasan por defecto.
    #codigo
```

La palabra reservada self hace referencia al propio método (es una referencia a sí misma y se pone siempre al principio).


Para crear el objeto sería:

```py
alumno1: Alumno = new Alumno('Martin','___@___.com')
alumno1.asistir_clase(1)
```


La best practice es crear una clase por cada archivo de Python. Los nombres de las clases van en mayúscula


Cuando yo en una lista hago nombreLista.sort() puedo hacer esto porque el data structure list() es una clase propia de Python.





[df1]: <https://randomuser.me/>

