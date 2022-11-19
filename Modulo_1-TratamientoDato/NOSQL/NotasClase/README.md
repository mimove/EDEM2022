# Notas Clase NOSQL

## _Clase 19/11/2022_

Las bases de datos SQL tienen algunas limitaciones, siendo una de las más importantes la limitación volumen, ya que escalan de forma vertical. Por ello, surgen las bases de datos NOSQL para Big Data, las cuales escalan horizontalmente (a más máquinas que le ponga mucho mayor la velocidad). La ventaja de una NOSQL vs SQL es por tanto su escalabilidad, pero son menos versátiles que una base de datos SQL.

Las formas de guardar datos en NOSQL son:

- Archivos

- Key-Value

- Documentos

- Gráficos

- En memoria

- Indexadas



## File storage

Definición:

> Es un almacenamiento de archivos distribuido, tolerante a fallos y normalmente compatible con POSIX. Se comporta de forma similar a un sistema de archivos normal y puede almacenar grandes conjuntos de datos, que se dividen en bloques y se replican.

Aspectos claves:

- La forma más facil y barata de almacenar datos

- Muy útil para lectura secuencial

- El almacenamiento puede ser en texto o binario, estrurado o no estructurado y orientado en columnas

Tecnologías: Amazon S3

<p align="center">
<img src="https://www.datanami.com/wp-content/uploads/2018/05/Nexla-File-Format.png" width=600px>

</p>

<br>

## Key-Value Store

Definición:

>El almacén de clave-valor (o bases de datos orientadas a columnas) es un paradigma de almacenamiento de datos diseñado para almacenar, recuperar y gestionar matrices asociativas, una estructura de datos más conocida hoy en día como diccionario o tabla de hash

Aspectos clave:

- Útil para patrones de acceso muy bien definidos, acceso aleatorio de lectura o escritura

- Escala muy bien

- Columnas dinámicas


- Schema en lectura

Tecnologías: HADOOP

<br>

## Document Store

Descripción

>Un almacén de documentos (o base de datos orientada a documentos) es un programa informático diseñado para almacenar, recuperar y gestionar información orientada a documentos, también conocida como datos semiestructurados (por ejemplo, JSON o XML).

Aspectos claves:

- Lenguaje query propio

- Facil de almacenar y recuperar documentos

- REST APIs (for JSON stores)

Tecnologías: MONGODB

<br>

## Graph Database

Descripción:

>Una base de datos gráfica es una base de datos que utiliza estructuras gráficas para realizar consultas semánticas con nodos, aristas y propiedades para representar y almacenar datos.

Aspectos claves:

- Buena para representar relaciones (networks)

- Tiene lenguaje query propio

- No escala demasiado bien


Tecnologías: NEO4J



<p align="center">
<img src="https://dist.neo4j.com/wp-content/uploads/20160415155725/graph-database-rules-engine.png" width=500px>

</p>


<br>

## In-Memory Database

Descripción:

>Una base de datos en memoria (IMDB, también sistema de base de datos en memoria principal o MMDB o base de datos residente en memoria) es un sistema de gestión de bases de datos que se basa principalmente en la memoria principal para el almacenamiento de datos del ordenador. Se contrapone a los sistemas de gestión de bases de datos que emplean un mecanismo de almacenamiento en disco.

Aspectos clave:

- Gran rendimiento

- Dificil de manejar: estabilidad de los datos y escalabilidad

- Útil para cache y almacenamiento de datos para aplicaciones en streaming



<br>

## Indexed

Descripción:

>Una base de datos indexada puede considerarse como un subtipo de almacén de documentos, que proporciona un motor de búsqueda distribuido y con capacidad para múltiples usuarios, con una interfaz web HTTP y documentos JSON sin esquema.

Aspectos clave:

- Comparte muchas características con el almacenamiento de archivos (own QL, almacenamiento de documentos, REST API)

- Herramientas de búsquedas de texto como: faceting, búsqueda de texto libre, sinónimos, autocompletado

- Lectura muy rápido, escritura muy lenta

Tecnologías: ELASTICSEARCH


DB-ENGINES RANKING

<p align="center">
<img src="https://img.inotgo.com/imagesLocal/202203/20/202203201531214475_7.jpg" width=600px>

</p>

<br>

<br>


## Teorema CAP

Todas las bases de datos tienen que cumplir 2 de las siguientes tres características:

- Consistencia

- Disponibilidad

- Particionamiento

<p align="center">
<img src="https://static001.geekbang.org/infoq/34/34c67b5892998ce4dc3c4a33db6dde8f.png" width=500px>

</p>


La única base de datos que dice que cumple las tres características a día de hoy es Google Spanner.



<br>

<br>


## CASSANDRA

### **Introducción a base de datos columnar**

- Son conocidas como key-value stroes

- Las filas son auto contenidas (incluyen tanto el nombre de la columna como el valor y la fecha cuando se creó)

- Las columnas se pueden añadir o quitar por filas

- Puede haber miles de columnas por tabla


**Diferencias entre SQL y NOSQL**

<p align="center">
<img src="https://miro.medium.com/max/700/1*CeQrHqjVIesDYAH99fFvOg.png" width=700px>

</p>



Definición Cassandra

>Apacha Cassandra es un sistema de gestión de bases de datos NOSQL distribuido, de código abierto y con un amplio almacén de columnas, diseñado para manejar grandes cantidades de datos en muchos servidores básicos, proporcionando una alta disponibilidad sin ningún punto de fallo. 

>Cassandra ofrece un robusto soporte para clusters que abarcan múltiples centros de datos, con replicación asíncrona sin maestro que permite operaciones de baja latencia para todos los clientes.



Características

- Muy alto rendimiento

- Alta escalabilidad

- Es elástica (muy fácil añadir y quitar nodos)

- Se pueden controlar muchas características

- Es descentralizada lo que minimiza los puntos de fallo

- Es totalmente tolerante a fallos (no importa que se caigan varios nodos porque tiene autobalance)




**Cuando usamos Cassandra**

La aplicación ideal de Cassandra se da cuando se cumplen las siguientes características:

- Escritura sobrepasa a lectura por un gran margen

- Los datos rara vez se actualizan

- El acceso a lectura se hace a través de una primary key conocida

- Los datos se pueden particionar a través de una key que permite que la base de datos sea distrubuida de forma equitativa

- No hace falta el uso de joins o aggregates



Los casos tipicos de uso de Cassandra son:

- Logs de transacciones: compras, test scores, etc

- Almacenamiento de time series data

- Tracking de pedidos, packages, etc

- Health tracker data

- Weather service history

- Aplicaciones IoT


### **Conceptos básicos de Cassandra**

<p align="center">
<img src="https://miro.medium.com/max/1248/1*Yiq6XbFEuZiyyJ36sSTTLg.png" width=500px>

</p>


**Primary Keys**

Los conceptos clave en Cassandra son diferentes a los de las bases de datos relacionales.

- Clave primaria: es lo que se denomina una clave de aptitud. Parte de la unicidad del registro en la base de datos, determina la localidad de los datos o en qué nodo deben almacenarse.

- Clave primaria compuesta: una clave primaria compuesta se compone de una o varias columnas a las que se hace referencia en la clave primaria. Se forma así:

```
((Partition_Key_1,...Partition_Key_N), (Cluster_Key_1, ...Cluster_Key_N))
```

- Clave de partición: El propósito de una clave de partición es identificar la partición o el nodo en el clúster que almacena esa fila

- Clave de agrupación: el propósito de la clave de agrupación es almacenar los datos de las filas en un orden ordenado



<p align="center">
<img src="https://www.instaclustr.com/wp-content/uploads/2021/10/Cassandra-Partitions-Partition-and-Clustering-Key.png" width=700px>

</p>














