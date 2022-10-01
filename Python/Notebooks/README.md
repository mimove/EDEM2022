# Notas sobre Notebooks

<br>

## Metodología Agile
<br>

Hoy en día el desarrollo de software funciona con metodología [Agile][Agile]:

1. El Product Owner (PO) hace una petición sobre una nueva funcionalidad a implementar
   
2. La petición entra al Backlog y se hace un backlog refinement para ver a que peticiones darles prioridad. Se hace una estimación del numero de días (o complejidad) que van a requerir las peticiones del backlog.
3. Se prepara un Product Increment (PI) en el que se elige de la lista del backlog las funcionalidades que se van a implementar y se calculan los días que se va a tardar en hacerlo.
4. Se hace el Sprint Planning (SP) y se deciden cuantas tareas se van a hacer en 15 días.
5. Al final del Sprint se hace una Demo con el cliente para enseñarle lo conseguido.
6. Si al cliente le gusta entramos en una fase de test.
7. Fase de performance (en vez de probar para 1 pruebo para 100)
8. Go live

El ciclo desde que hay una petición hasta que va a producción tarda entre 2-3 meses.


La alternativa a Agile es usar la estrategia Waterfall en la que se decide lo que hacer desde entre el día 1 y el último día y no hay división de tareas tan segmentada como en el método Agile. En Waterfall el tiempo hasta producción es 6 meses a 1 año.

<br>
<br>




## Notebooks
<br>

Los Notebooks son una atajo que tienen los Data Scientist para desde el paso del Backlog ir directamente al paso Go Live. Esto se hace así porque en el mundo de los datos no se sabe si la petición que hay que implementar se puede llevar a cabo o no. Un Notebook es la herramienta principal de un Data Scientist.


Esto sucede porque no puedo ejecutar codigo Python directamente en el código de producción. En el de producción solo puedo ejecutar consultas SQL. Con Notebooks puedo ejecutar codigo Python como si estuviera usando el código producción para ver si seguimos con el desarrollo. Por ello, este Notebook es temporal y no entra en el ciclo Agile tracional.


Las partes que tiene un Notebook son: celda de texto, celda de código y un kernel. Las variables que se guardan en el Kernel son compartidas a nivel de todo el Notebook. Los Notebooks están pensados para ser leídos de manera natural, por ello las variables que declaro en párrafo al principio se pueden utilizar después en el código. Se pueden utilizar múltiples lenguajes en un solo Notebook.



La herramienta para desarrollar Notebooks de Google se llama [Colab][colab]. Cuando Colab podemos utilizar tanto aceleración de Hardware por CPU tanto como por GPU o TPU. 


Los archivos que se suben a Colab son volátiles, al borrar el kernel desaparecen.











[Agile]: <https://www.atlassian.com/agile#:~:text=Agile%20isn't%20defined%20by,feedback%20cycles%20and%20continuous%20improvement.>

[colab]: <https://colab.research.google.com/>