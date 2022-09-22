# Notas clases Python (** Utilizar codewars.com para practicar)

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
```sh
user = 'Pepe'
edad = 25
print(f'{user} tiene {edad} años')
user = 'Pepe'
edad = 25
print(f'{user} tiene {edad} años)
```


Para dudas de programación en Python usar StackOverflow

Tipos de datos en python

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

```sh
NUMERO_PI = 3.1415926
```

Se puede imprimir una lista sin necesidad de hacer un for loop. Esto es muy útil y se hace de la siguiente manera:

```sh
miLista:[str] = ["Martin", "Juan", "Pablo"]
print(*miLista)
```


Otro tipo de dato de Python se llama "Iterable" que es cualquier dato que se puede utilizar para iterar. Los datos iterables se pueden utilizar dentro de la función set, que nos elimina los datos repetidos.

```sh
misNumeros = [1,2,3,4,5,6,7,8,9,3,2,5,3]
misNumerosNoRepetidos = set(misNumeros)
print(*misNumerosNoRepetidos)
```

Los conceptos de paso por "Valor" y paso por "Referencia" son muy importantes. Por ejemplo, para ordenar una list yo podría hacer:

```sh
misNumerosOrdenados = sorted(misNumeros)
```

Sería un paso por "Valor" y no me modifica la lista de misNumeros. Sin embargo, si yo aplico: 

```sh
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
