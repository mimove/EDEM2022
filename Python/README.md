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

Con el siguiente código es como se puede dar formato e imprimir varias variables en Python
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


## _Clase 22/09/2022_



