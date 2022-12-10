# Notas clase Spark

## _Clase 09/12/2022_

<br>

Antes de Apache Spark se intentaba que los ordenadores fueran muy potentes y con mucha RAM, lo cual es muy caro y no se puede escalar. Esto se conoce como computación monolítica. La alternativa es utilizar las arquitecturas en paralelo que hacen todo escalable y mucho más eficiente. 

Este tipo de arquitecturas aparece por primera vez en 2002 cuando Google tenía que indexar toda la información solo con una máquina. Google lo llamó MapReduce que consiste en mapear cada una de todas las particiones para después ralizar operaciones de transformación, posteriormente, dicha información procesada se reduce y se envía a almacentamiento. Además, con batches muy grandes es bastante lento. 

En 2014 aparece la primera release de Spark. Para utilizar Spark, se neceista un sistema de almacenamiento de archivo. En su caso es el HDFS en el que los datos se dividen en bloques y se guardan en particiones.


## Apache Spark

> Es un framework para trabajar con datos distribuidos que nos da APIs para trabajar con Machine Learning, queries interactivas con SQL, procesamiento en streaming y procesamiento de grafos.


Sus principales ventajas son:

- Alta velocidad de computación ya que todo se procesa a través de la RAM en vez de tener que escribir en disco.

- Es altamente accesible a través de APIs nativas en Java, Scala, Python, R o SQL

- Es compatible con todos los sistemas de Hadoop actuales.

- Tiene shells interactivas en Scala y Python

- Mejora la productividad al hacer que el desarrollador no tenga que concentrarse en trabajar con todo el código, y se puede enfocar en la lógica.


<p align="center">
<img src="https://www.oreilly.com/api/v2/epubs/9781492050032/files/assets/lesp_0102.png" width=400px>
</p>


Usos principales de Spark:

- Procesamiento de largos sets de datos distribuidos en paralelo a través de un cluster

- Realizar queries ad hoc para explorar y visualizar data sets.

- Para construir, entrenar y evaluar modelos de machine learning.

- Para implementer end-to-end de data pipelines variadas.


### **Arquitectura Spark**

<p align="center">
<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2020/11/spark_Architecture.png" width=500px>
</p>

Cada aplicación de Spark consiste en un programa Driver que define datasets distribuidos, un cluster que tiene los recursos y unos ejecutores que ejecutan el código.


<br>
<br>

## RDD

> Es la estructura básica de datos de Spark. Es una colección de datos distribuida e inmutable que es partitionada en todas las máquinas de un cluster. Fácilita 2 tipos de operaciones: transformaciones (e.g. filte(), map(), etc) y acciones (e.g. count(), first(), etc).

El driver recuerda las transformaciones aplicadas a un RDD, de manera que si una partición se pierde, esa partición se puede reconstruir fácilmente desde otro nodo del clúster.



Este tipo de estructura es algo compleja de utilizar, y por eso se utilizan Data Frames que son más sencillos. Los RDDs solo se suelen utilizar en los siguientes casos:

- Utilizando paquetes de terceros escritos en RDDs

- Para optimización de código

- Para dar una instrucción precisa a Spark de como hacer una query



<br>

<br>

## SparkSQL

> Es la principal librería que utilizaremos en el Máster. Es una interfaz para trabajar con datos estructurados y semi-estrcutrados. Utiliza DataFrames y DataSets y lenguaje SQL sobre el que se pueden ejecutar consultas




<br>
<br>

## _Clase 10/12/2012_

<br>

### **Joins**

Es una de las operaciones principales de SQL que se utiliza para juntar horizontalmente 2 tablas. Existen muchos tipos de joins: outter, inner, left-join, right-join, etc. 

<p align="center">
<img src="https://dataschool.com/assets/images/how-to-teach-people-sql/sqlJoins/sqlJoins_7.png" width=500px>
</p>


Los joins en Spark los hace de la siguientes 3 maneras:

- Broadcast: si tabla B < A se hace broadcast de B a las particiones donde está A y se hace el join en las particiones.

- Shuffled Hash: se juntan las tablas en todas las particiones y se hacen los joins en cada partición.

- Sort merge: en tablas grandes se ordena por key antes de meter las tablas en las particiones y luego se hace el join en cada partición.



<br>

### **Windows Partitioning**

Se utiliza para coger una tabla y dividirla en varias tablas que se llaman frames. La división la realiza en función a un parametro o condición que le digamos nosotros. Por ejemplo, podría sacar los 3 valores top de una lista (ej: precio de móviles top 3).

