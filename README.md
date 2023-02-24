# MASTER DATA  [![N|Solid](https://edem.eu/wp-content/plugins/edem-shortcodes/public/img/logo-Edem.png)](https://edem.eu)   2022

En el Máster de [EDEM][edem] sobre Data Analytics, el aprendizaje se estructura en diferentes módulos, cuyo contenido en este repositorio se ha clasificado en las siguientes carpetas:

<br>

| CARPETA | CONTENIDO |
| ------ | ------ |
| [Modulo_0-Fundamentos](Modulo_0-Fundamentos/) | Contiene la parte introductoria del curso. En este primer módulo se aprende sobre lenguajes como Python o Unix, así como el manejo de herramientas como Docker  |
| [Modulo_1-TratamientoDato](Modulo_1-TratamientoDato/) | En este módulo aprendemos los conceptos y programas empleados para el tratamiento de los datos, desde la ingestión de datos hasta su aplicación al negocio |
| [Modulo_2-AplicacionNegocio](Modulo_2-AplicacionNegocio/) | En este módulo aprendemos diferentes ideas sobre como utilizar los datos para potenciar el crecimiento de una empresa |
| [Modulo_3-TransformacionDigital](Modulo_3-TransformacionDigital/) | En este módulo nos enseñan las formas en la que los datos están transformando nuestra sociedad y como cambiará el mundo en las próximas décadas  |
| [Modulo_4-AprendizajeAutomatico](Modulo_4-AprendizajeAutomatico) | En este módulo aprendemos algoritmos de Machine Learning y Deep Learning que se utilizan para sacar el mayor provecho de los datos a través de la IA  |


<br>

Dentro de cada una de las carpetas la organización es la siguiente:

<br>

| ARCHIVO/DIR | CONTENIDO |
| ------ | ------ |
| README.md | Explica la estructura que tiene dicho módulo y como se dividen las diferentes carpetas  |
| NotasClase | Incluye los apuntes tomados sobre teoría general de dicho módulo |
| <lenguaje/software> | Cada carpeta con el nombre de un lenguaje de programación o software que se utiliza durante el Máster |


--------------------------------------------------------------------------------

<br>

A lo largo del Máster también hemos realizado 4 data projects (cada uno en un repositorio individual al que se puede acceder pinchando en el enlace del título) que tratan sobre lo siguiente:

<br>

## [DATA PROJECT 1](https://github.com/mimove/DATAPROJECT1)

<br>

<p align="center">
<img src=".images/idealista.jpg" width=250px>
</p>

### Descripción

El portal lider de compra de vivienda en españa quiere sacar un piloto de calidad de vida aplicado a la vivienda y ha elegido Valencia como sede para su piloto. La idea de este piloto es ofrecer un mapa de calidad de la vivienda en funcion de indicadores de datos abiertos. La calidad de la vivienda se medirá por ruido, hospitales, contaminación… teniendo que dar una nota a una zona en concreto en base a dichos parámetros.

<br>

### Equipo

- [Fan Wu](https://www.linkedin.com/in/fan-wu-98697b13b/): Licenciado en ADE. Encargado de la parte de Business Inteligence y mejora de la aplicación para la incorporación de viviendas a la base de datos a través de Python y POSTRESQL

- [Dario Fernández](https://www.linkedin.com/in/dar%C3%ADo-fern%C3%A1ndez-fern%C3%A1ndez/): Economista. Encargado de la parte de Data Analytics diseñando la encuesta a realizar a los clientes y desarrollando el código para conexión a la API de Google a través de Python

- [Francisco Rosillo](https://www.linkedin.com/in/francisco-rosillo-d%C3%ADez/): Ingeniero de Telecomunicaciones. Parte del equipo de Data Engineering del proyecto. Desarrollo de código Python para carga de base de datos y creación de tablas en POSTGRESQL. También encargado de la parte de Calidad del Dato del proyecto.

- [Miguel Moratilla](https://github.com/mimove): Doctor en Ing. Aeroespacial. Encargado Senior del proyecto. Responsable de la extracción y transformación de los datos desde la web de [open data](https://valencia.opendatasoft.com/pages/home/). Diseño de la arquitectura, y dirección del proyecto distribuyendo tareas entre los componentes del equipo.

<br>

### Diseño de la arquitectura

El proyecto consta de 3 contenedores docker que se encargan de las 3 partes de Data Engineering (ETL) y un cuarto contenedor para realizar un estudio de calidad del dato:

1. Contenedor NiFi (Extracción): el contenedor NiFi se utiliza para la recolección de datos de la web de open data. NiFi se configura a través de un volumen bind mounted en el que se encuentra el flujo que tiene que ser ejecutado automáticamente cuando se levanta el contenedor. Este volumen se está alojado en ./nifi/conf_local. En total se descargan 9 archivos geojson con diferentes datos relativos a la calidad de vida de Valencia. Los archivos son compartidos con el contenedor Python a través de un volumen que se llama nifi_python. Los datos descargados son:

    - Zonas Verdes

    - Distribución de Hospitales

    - Distribución de colegios

    - Nivel de ruido

    - Limpieza

    - Puntos de recarga de coches eléctricos

    - Transporte público



2. Contenedor Python (Transformación): el contenedor Python se encarga de leer los archivos geojson que descarga NiFi, calcular la intersección del geoDataFrame de barrios con todos los geoDataFrame del resto de características, conectarse a la API de Google y calcular los barrios recomendados para los clientes en función de sus respuestas a la encuesta. Una vez hechas todas las transformaciones a los datos, el programa de Python se encarga también de cargar los datos en las tablas de la base de datos SQL. Las funciones creadas se han metido dentro de modulos para tener una estructura más organizada del código. El contenedor tiene 2 volumenes conectados: 

    - nifi_python: Volumen del que recoge los datos descargados por NiFi

    - db_barrios: Volumen en el que escribe el archivo final geojson con las características interpoladas a todos los barrios


3. Contenedor Postgres (Carga): el contenedor Postgres se utiliza como data warehouse para almacenar la base de datos del proyecto. Las tablas se crean desde un archivo .sql en tiempo de construcción del contenedor y son posteriormente alimentadas por Python.


4. Contenedor Jupyter (Calidad del dato): el contenedor docker se conecta a través del volumen db_barrios a python para poder acceder al archivo geojson y realizar un estudio de calidad del dato.

El diagrama con la arquitectura es el siguiente:

<p align="center">
<img src="./.images/docker-compose_test.png" width=500px>
</p>

<br>


Por otro lado, el modelo de datos consta de 6 tablas: Casas, Barrios, Recomendación, Cliente, Barrio_Características y Características, siendo la tabla principal la de Recomendación, ya que es la que unifica la información de los clientes con los barrios que le corresponden para cada característica según el estilo de vida que han respondido en el cuestionario.

<p align="center">
<img src="./.images/DB_image.png" width=500px>
</p>

<br>

### Ejecución del proyecto

Para ejecutar el proyecto simplemente hay que clonar el repositorio y ejecutar*:

```sh
docker compose up
```

Esto levanta todos los contenedores y asigna los volumenes y los puertos a cada uno de ellos. Para ver como funciona el código completo se puede consultar el siguiente video de YouTube:

<https://www.youtube.com/watch?v=w-ZNPGcKnTY&ab_channel=FanWu>



El contenedor NiFi se puede comprobar desde la siguiente dirección:

<http://localhost:8443/nifi>

El contenedor Jupyter se puede comprobar desde la siguiente dirección:

<http://localhost:10000>


Para cargar el archivo en Tableu hay que conectarse a la base de datos con los siguientes campos y abrir el archivo de la carpeta [tableau](./tableau):

| Campo | Texto a completar |
|----------|---------|
| <b>Server Address*</b> | localhost  |
| <b>Port*</b> | 5432  |
| <b>Database*</b> | idealista  |
| <b>Username*</b> | postgres  |
| <b>Password</b> | Welcome01  |



<br>

*El código funciona utilizando la distribución WSL:Ubuntu. Desde Windows existe un problema con el script start.sh de NiFi a la hora de copiarlo al contenedor


<br>



<br>

## DATA PROJECT 2 (On Premise) [^1]


<p align="center">
<img src=".images/logo_company.png" width=300px>
</p>


<br>

### DESCRIPCIÓN

La empresa de placas solares **SolarMinds Technologies [^2]** ha decidido montar una infraestructura de gestión de los datos que cada placa individual genera para poder estimar la producción total de energía, así como monitorizar el estado de cada placa solar para facilitar las tareas de mantenimiento. En principio, dicha empresa tiene en su sede central montados y funcionados una serie de servidores que le gustaría utilizar para este proyecto. Nuestro objetivo como consultores es, primero facilitarles una herramienta E2E on premise que puedan usar para sacar la mayor cantidad de información valiosa posible pero, por otro lado, queremos enseñarles también las ventajas que supondría tener este software en el Cloud. 



<br>

### Equipo

- [Elyca Jardín](https://www.linkedin.com/in/elycajardin/): Máster en Ingeniería Marítima. Encargada de la parte de Business Inteligence y Data Analytics utlizando Grafana Cloud y Looker Data Studio

- [Pablo Martínez](https://github.com/Pablomartiver): Economista. Encargado de la parte de Data Engineering relativa a la cola de mensajes en Pub/Sub y Kafka (On premise)

- [Jorge Martínez](https://github.com/joorgemartinez): Licenciado en International Business. Parte del equipo de Data Engineering del proyecto. Desarrollo de código Python para Dataflow y Cloud Functions así como de Spark (On premise)

- [Miguel Moratilla](https://github.com/mimove): Doctor en Ing. Aeroespacial. Encargado Senior del proyecto. Responsable de la generación de los datos y la parte DevOps del proyecto. Diseño de la arquitectura, y dirección del proyecto distribuyendo tareas entre los componentes del equipo.

<br>

En este repositorio, se encuentra la solución On premise que hemos diseñado. Consta de las siguientes partes:

1. Generador de datos con envío a Kafka

2. Spark streaming para transformación de los mensajes

3. MySQL como almacenamiento

4. Grafana para visualización

5. Flask para generar una API de consulta de datos a la BD

Todo ello se encuentra dentro de un Docker compose. Para ejecutar el docker compose up hay que tener en cuenta 2 cosas:

1. Dentro del archivo de variables de entorno .env se puede configurar lo siguiente:

    ```s
    CONTAINERS=4 #Numero de paneles solares máximo a crear
    PROBABILIDAD=10 #Probabilidad de que un panel se apague
    TIME=5 #Delay entre datos de los paneles
    IMAGE=solar_gen_premise #Nombre de la imagen de docker de cada panel
    TOPIC=panelInfo #Nombre del topico en Kafka
    ```

2. Una vez configurado el archivo de variables de entorno, se puede ejecutar ```docker-compose up -d``` para activar la aplicación.


<br>


### Diseño de Arquitectura

En la siguiente imagen se puede ver el diseño de arquitectura seguido:

<p align="center">
<img src=".images/arq_premise.png" width=500px>
</p>

<br>

### Generador de datos (KAFKA)

Para simular el comportamiento de un placa solar, se ha optado por utilizar una ecuación basada en la secante hiperbólica, cuya distribución es muy similar a una distribución normal. La ecuación utilizada es:

$$\mathrm{P}=\frac{\mathrm{P_{max}}}{\cosh((t-t_{ini})*C-t_{ini})^{C}}$$


Donde $\mathrm{P_{max}}$ es la potencia máxima del panel, $t_{ini}$ la hora a la que empieza a generar energía, y $C$ es una constante que se utiliza para modificar el ancho de la curva.

La siguiente figura muestra como se vería la curva para una placa solar que produjera durante una hora, con un máximo de potencia de 400W:

<p align="center">
<img src=".images/sech.png" width=400px>
</p>


Con esta ecuación, el generador de datos lo que simula es una serie de contenedores Docker, siendo cada contenedor una placa solar individual, que tiene una probabilidad dada cada n segundos de estar produciendo energía o no.

Estos contenedores, envían información a un tópico de los brokers de Kafka. En total, está configuración cuenta con 2 Brokers para estar diseñada con tolerancia a fallos. Si uno de los 2 brokers se apaga, el otro sigue funcionando y la aplicación no daría ningún fallo.

<br>

### SPARK

Dentro de la carpeta de pyspark, se encuentra el código Python escrito utilizando la librería Spark Streaming para consumir los datos generados por los paneles solares mediante una subscripción al tópico de Kafka. En Spark se realizan los siguientes pasos:

1. Primero se leen los mensajes escritos en formato JSON que se encuentran en el tópico, creando un Dataframe con el contenido de los mensajes.

2. Los datos recibidos se guardan en una tabla de MySQL  que tiene el siguiente schema:

    ```sql
    CREATE TABLE IF NOT EXISTS panelData (
    Panel_id varchar(250) NOT NULL,
    power_panel DECIMAL(20,3) NOT NULL,
    current_status INT NOT NULL,
    time_data TIMESTAMP
    );
    ```


3. Se calcula una ventana para sacar en franjas de 30 segundos la potencia media generada por los paneles, y se escribe el resultado de la transformación en otra tabla de MySQL.

Una diferencia importante con respecto a la arquitectura de Cloud, es que Spark streaming no es 100% en streaming, si no que funciona mediante la creación de microbatches que luegos son volcados con la clase ```writeStream``` a la base de datos


Para ejecutar este código se puede hacer de 2 formas:

1. Ejecutando el siguiente comando desde la terminal:

    ```sh
    docker exec dataproject2_onpremise-spark-master-1 \
                /spark/bin/spark-submit \
                --master spark://spark-master:7077 \
                --jars /opt/spark-apps/mysql-connector-java-8.0.13.jar \
                --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.2 \
                --driver-memory 1G \
                --executor-memory 1G \
                --conf "spark.worker.instances=2" \
                /opt/spark-apps/main.py
    ```

2. Ejecutando el script ./run.sh que se encuentra dentro de la carpeta


<br>

### API EN FLASK

Se ha construido una API en Flask que, mediante una consulta con un ID concreto de una placa, devuelve todos los registros de esa placa en concreto para poder trabajar con ellos desde otra aplicación. En la siguiente imagen se ve un ejemplo de la llamada a la API:


<p align="center">
<img src=".images/api.png" width=800px>
</p>


<br>

### GRAFANA CLOUD

En la parte de visualización, se ha creado un dashboard que se muestra en la siguiente imagen para un ejemplo con 30 placas solares:


<p align="center">
<img src=".images/grafana.png" width=800px>
</p>


<br>
[^1]: El proyecto también se ha desarrollado en Cloud y se puede ver en el siguiente [link](https://github.com/mimove/DATAPROJECT2)
[^2]: Logo y nombre creados con la inteligencia artificial [Dall·E 2](https://openai.com/dall-e-2/) y ChatGPT respectivamente.


<br>



<br>

## DATA PROJECT 3


<br>


<br>

## DATA PROJECT 4


<br>







[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[edem]: <https://edem.eu>

