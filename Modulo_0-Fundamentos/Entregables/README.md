

<p align="center">
<img src="https://cdn.glitch.com/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2Fsimpsons.PNG?1497481539770" width="250">
</p>

# Explicación del Caso

Para completar este caso debemos crear un código python que consuma datos de una api sobre los simpsons y guarde la información en ficheros csv y carpetas. 


<br>



<table class="noborder">

## **Maggie Level (Ejercicio_1 en mi repositorio)**

<tr class="noborder">
<td class="noborder">

En este ejercicio se piden realizar las siguientes tareas:

1. Usando google colab crear un notebook que consuma la api de los simpsons y haga una consulta cada 30seg a la API

2. El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).

3. Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de manera autónoma. El Docker debe tener el código en una carpeta app

4. El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger
citas de ellos dos.
  
</td>
<td class="noborder">



<p align="center">
<img width= 300px src=https://upload.wikimedia.org/wikipedia/en/9/9d/Maggie_Simpson.png>
</p>

  
</td>
</tr>

</table>

<style>
.noborder {border:none!important;}
</style>


<br>

Dentro de mi repositorio este directorio se organiza de la siguiente manera:

| Carpeta/Archivo | Contenido |
|---------------|---------------|
| Dockerfile | Contiene el codigo para construir el contenedor Docker que se pide en los puntos 3 y 4|
| Lisa | Contiene el archivo quotes_lisa.csv con todas las frases de Lisa|
| Homer | Contiene el archivo quotes_homer.csv con todas las frases de Homer|
| General | Contiene las frases de todos los personajes |
| main.py | Script de Python que ejecuta el paso 2 |
| requirements.txt | Archivo necesario para instalar los módulos que falten en el contenedor docker haciendo uso de ``` pip install -r requirements.txt```|
| simpsons.ipynb | Notebook generado con [Google Colab][googlecolab] (hacer click para acceder al Notebook) con el paso 1 |

<br>

Ejecutando los siguientes comandos se genera la imagen Docker a la que se le pone de nombre ```pythonsimpson```

```sh
docker build -t pythonsimpson .
```

Con el siguiente comando se levanta el contenedor:

```sh
docker run -it pythonsimpson
```

(Ejecutando ```docker run``` con el argumento ```-it``` se accede al contedor y muestra un print en la terminal con el nombre y frase de cada personaje. Si no queremos ver este print, hay que utilizar el argumento ```-d``` para levantar el contenedor en el background.)

<br>

Y haciendo uso de los siguientes comandos desde una terminal se puede comprobar que el programa está escribiendo las frases en alguna de las carpetas:

```sh
docker exec -it <conainer_id> bash

cd General/
tail -f quotes_general.csv
```



<br>

<br>





<table>



## **Lisa Level (Ejercicio_2 en mi repositorio)**

<tr>
<td>

En este ejercicio se piden realizar las siguientes tareas:

1. Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del mismo.

2. El código debe mantener un diccionario de palabras y escribir en cada iteración en un fichero el conteo de palabras que lleva.

    a. The;1

    b. Great;2


3. El código debe crear de manera dinámica las carpetas con nuevos personajes
  
</td>
<td>


<p align="center">
<img width= 200px src=https://cdn.glitch.me/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2FLisaSimpson.png>
</p>

  
</td>
</tr>

</table>


<br>

Dentro de mi repositorio este directorio se organiza de la siguiente manera:




| Carpeta/Archivo | Contenido |
|---------------|---------------|
| Dockerfile | Contiene el codigo para construir el contenedor Docker con el codigo para construir la imagen con el resultado de este ejercicio|
| main.py | Script de Python que ejecuta los pasos 1 a 3 |
| requirements.txt | Archivo necesario para instalar los módulos que falten en el contenedor docker haciendo uso de ``` pip install -r requirements.txt```|


<br>

Ejecutando los siguientes comandos se genera la imagen Docker a la que se le pone de nombre ```pythonsimpson2```

```sh
docker build -t pythonsimpson2 .
```

Con el siguiente comando se levanta el contenedor:

```sh
docker run -it pythonsimpson2
```

(Ejecutando ```docker run``` con el argumento ```-it``` se accede al contedor y muestra un print en la terminal con el nombre y frase de cada personaje. Si no queremos ver este print, hay que utilizar el argumento ```-d``` para levantar el contenedor en el background.)

<br>

Y haciendo uso de los siguientes comandos desde otra terminal se puede comprobar que el programa está escribiendo las palabras con el número de veces que aparecen en el archivo countedWords.csv

```sh
docker exec -it <conainer_id> bash

cd General/
tail -f countedWords.csv
```

<br>
<br>



<table>

## **Bart Level (Ejercicio_3 en mi repositorio)**

<tr>
<td>
En este ejercicio se piden realizar las siguientes tareas:

1. Construid un Docker-compose con una imagen de un contenedor de Jupyter

2. Dentro del Jupyter generad un notebook con una gráfica mostrando las
palabras más habituales en las quotes

3. Mostrar un listado de las carpetas y las fotos de los personajes en el jupyter

4. Docker-compose debe ser capaz de hacer build del contenedor original
</td>
<td>


<p align="center">
<img width= 200px src=https://cdn.glitch.me/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2FBartSimpson.png>
</p>

  
</td>
</tr>

</table>















<br>

Dentro de mi repositorio este directorio se organiza de la siguiente manera:

| Carpeta/Archivo | Contenido |
|---------------|---------------|
| python | Carpeta que contiene los archivos para contruir el contenedor Python |
| jupyter | Carpeta que contiene los archivos para contruir el contenedor Jupyter |
| docker-compose.yml | Código de docker-compose para levantar ambos contenedores |

Dentro de las carpetas "python" y "jupyter" los archivos se organizan de forma similar a como en los 2 anteriores niveles. La diferencia, es que existe una carpeta adicional llamada results, que es donde se monta el volumen para compartir datos entre los 2 contenedores. El código python está hecho para que los plots se generen 'on-the-fly' de manera que se pueda tanto borrar carpetas con imagenes de personajes, como resetear el servidor python sin que el Jupyter Notebook de un error. 

He hecho un intento de ejecutar en paralelo cada una de las celdas en un procesador distinto del ordenador para poder visualizar los 2 gráficos simultáneamente, pero no lo he terminado de conseguir.


<br>

Ejecutando los siguientes comandos se construyen y levantan a la vez los contenedores ```ejercicio_3-jupyter``` y ```ejercicio_3-srv-python```:


```sh
docker compose up
```


Para ejecutar el Notebook contenido en el contenedor Jupyter, se tiene que acceder a la siguiente dirección:

 
<http://localhost:10000/notebooks/simpsons_notebook.ipynb>



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[googlecolab]: <https://colab.research.google.com/drive/1drySStGjO6NYB1oliTiML2vnPxjl7O1J>