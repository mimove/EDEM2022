# TRATAMIENTO DEL DATO

(*leer el paper de Shatoshi sobre BitCoin y el paper de 2003 de hadoop de Google sobre procesamiento distribuido)

(*para el mundo de los datos utilizar Apache para buscar conceptos)

(*tutoriales sql, kafka y spark)

<br>


## _Clase 13/10/2022_

<br>

## Intro Módulo

El mundo de los datos empezó hablando solo de hacer páginas web con bases de datos, que poco a poco fueron haciéndose más grandes. En esa época (años 2000 a 2010) los datos se usaban solo para consultar información y hacer algún análisis muy simple. 

En 2011 IBM consiguió crear un algoritmo que ganaba el Jeopardy. En 2012 empieza a haber grandes proyectos de data en las empresas. 

No obstante, en 2014 se descubrió que Hadoop no era algo escalable y se publicó Spark. 

En 2016, aparece TensorFlow y entra la IA en el mundo de los datos. Es el momento en el que el mundo de la IA se "democratiza". La IA no nace en 2016, pero TensorFlow hace que los programadores puedan hacer uso de ella. No obstante, a día de hoy todavía no hay una IA genérica que pueda hacer múltiples funciones. 

En 2018 se adopta la tecnología Cloud para el desarrollo de los proyectos, y la mayoría de las empresas empiezan a trabajar para migrar su infraestructura a la nube.


A día de hoy un proyecto siempre está basada en Cloud, con Data Scientist construyendo modelos y Data Engineers encargados de montar la infraestructura y la ingestión de Datos. Un equipo de 5 personas a día de hoy sería:

 - 3 Data Engineers

 - 1 Data Scientist
 - 1 Cloud Engineer

En el Máster tenemos que conseguir estar en una posición intermedia entre el CEO y el "techi" junior para poder transmitir la información de los datos entre los diferentes estamentos de la empresa.

Cada vez va mejorando más la IA y la vamos teniendo más presente en nuestras vidas. Va pasito a paso y nosotros la vamos absorviendo, y ya hay muchas cosas que hacemos día a día que hacen uso de ella (Ej: Google Maps). 



A día de hoy estamos en el mejor momento de los datos, ya que tenemos la fuente que recoge los datos, la computación en la nube y la analítica con IA.



Las empresas están en la mayoría en el punto de trabajar con pequeños sets de datos. El siguiente paso sería sacar algo de información visual con gráficas. Después va el paso de intentar predecir lo que va a pasar en el futuro con lo que ha pasado en el pasado (conocimiento), el útimo paso sería ser capaz de vender ese conocimiento a otros.

Los skills más buscados de las compañías a día de hoy son:

- Cloud

- Analitica
- Artificial Intelligence
- Algo de Blockchain pero cada vez menos


Las partes de la arquitectura de datos son:

1. Data Ingestion services: Herramientas para poder canalizar los datos a un sistema de almacenamiento.

2. Capa de Data Repository:

    2.1 Raw Layer

    2.2 Enterprise Layer

    2.3 Application Layer




<br>
<br>

## _Clase 20/10/2022_

<br>


## Origen del Problema


Durante los últimos años, el volumen de datos generados por las personas ha crecido exponencialmente, y es necesario para las empresas procesar la mayor cantidad de información posible.

Las 5 V's del Big Data:

1. Volumen: el tamaño de los datos

2. Velocidad: La velocidad a la que se generan los datos

3. Variedad: Los diferentes tipos de datos

4. Veracidad : La confianza que tenemos en los datos en términos de que precisos son

5. Valor: Que valor me aportan los datos que tengo

<br>

<p align="center">
<img src=https://www.edureka.co/blog/wp-content/uploads/2018/06/Five-Vs-of-Big-Data-What-is-Big-Data-Edureka.png width=800px>
</p>

<br>

El Big Data cada vez va a ir a más, porque tanto el volumen como la velocidad de procesamiento de datos va a seguir creciendo de forma continua. El gran volumen de datos que se genera a día de hoy crea un problema de almacenamiento que se tiene que resolver. La explosión del Cloud ha hecho que el coste de almacenamiento por 1Gb de datos haya decrecido mucho en los últimos años. 


De los 5 puntos del Big Data, el más importante para saber si tengo un entorno Big Data es la variedad, que nos dice si estamos procesando información de manera distinta. Esta variedad se consigue ingestando datos de muchas fuentes, y dichas fuentes están también creciendo considerablemente en los últimos años. Es importante poder controlar dichas fuentes para recibir los datos de forma adecuada. Dentro de los datos que recibo, el tipo va a ser diferente. No es lo mismo recibir un precio como €2.0 que 2.00 que 2€. La variedad es lo que nos convierte un sistema clásico en un sistema Big Data. 


La veracidad es algo que damos por hecho cuando recibimos los datos. Hay 3 variables que hacen que la vercidad de la información no sea tan fácil de gestionar:

- **Cultural**: la competitividad entre departamentos puede hacer que los datos no se compartan entre ellos

- **Estructural**: En grandes compañias, los datos se almacenan de manera gerárquica y por diferentes capas que son manejadas por personal muy especializado.

- **Tecnológica**: Las aplicaciones puede que no se usen o diseñen para hacer referencia cruzada de datos entre ellas. 



La función que tienen los datos en una empresa al final es para que aporten un valor. Si simplemente los almaceno, no voy a conseguir obtener nada de ellos. El valor de los datos se puede usar para diferentes cosas: optimizar tareas y procesos, reforzar el conocimiento y las relaciones del cliente, venderlos, facilitar y acelerar la toma de decisiones, mejorar los servicios, crear nuevos servicios y productos. Lo que hay que tener claro, es que los datos que estamos recolectando tienen un valor, y si vemos que no lo tienen, nos tenemos que plantear hacerlos desaparecer para mejorar la eficiencia del volumen, almacenamiento y velocidad de procesamiento de los mismos. 

Uno de los problemas que lleva el crecimiento de los datos es la gestión de los mismos. Hay datos relativos a la privacidad de las personas que están regulados por leyes como la GDPR y hay que tener cuidado a la hora de almacenarlos y pedirlos al usuario. 


Cada vez que nos planteemos un proyecto de Big Data me tengo que plantear las 5 V's, y por ejemplo, si no cumple la de variedad, no tengo un problema de Big Data y puedo aplicar soluciones tradicionales para resolverlos. 

Para almacenar los datos tengo varias soluciones:

- **Data Warehouse**: Los datos se almacenan de manera vertical si se pueden independizar, por ejemplo datos de ventas y compras cada uno por separado. Los Data Warehouse son más lentos a la hora de escribir datos, pero a la hora de leerlos son muy rápidos porque los datos están organizados. Cuando hay mucha variedad de datos, un Data Warehouse presenta inconvenientes porque los contenedores de datos están predefinidos. Las Bases de Datos tipo Oracle (SQL) son las que almacenan los Data Warehouse

- **Data Lake**: Los datos se almacenan todos en espacios intercambiables, de manera que datos que hacen referencia a diferentes variables se almacenan juntos. En un Data Lake al no estar organizados los datos, se tarda más en leer los datos. No obstante, en cuanto a variedad de datos es mucho más eficiente el uso de un Data Lake. Tecnlogías como Spark para bases de datos distribuidas, etc. son las que se usan en Data Lakes.

<br>


<p align="center">
<img src=https://www.qubole.com/wp-content/uploads/2020/12/Dl-vs-DW-infograph-1000x563.png width=800px>
</p>

<br>


Si no se cumplen las condiciones para que el problema que tenemos que resolver sea de Big Data, es mucho más conveniente utilizar un Data Warehouse que un Data Lake. Dicho de otra manera, a no ser que haya un problema que lo justifique, siempre usaremos Data Warehouse. 


<br>

## _Clase 21/10/2022_

En lenguaje cotidiando, un Data Lake sería necesario cuando queramos almacenar tanto audio, como video, fotos, json, etc. Sería como una carpeta de Windows. Mientras que un Data Warehouse sería necesario solo si tenemos un tipo de datos como por ejemplo archivos csv. En este caso un Data Warehouse sería similar a Excel.

En cualquier momento se puede pasar de un tipo de infraestructura a otra. Lo normal, es empezar teniendo un Data Warehouse y, con el tiempo y el incremento de volumen de datos, pasarnos a un Data Lake. Si se toma esa decisión, se dejaría el DW para la visión analítica de un Data Analyst y el DL para el análisis de un Data Scientist.


<br>

### **Escalado**

Un DW tiene un escalado vertical, eso quiere decir que para mejorarlo tengo que mejorar la capacidad de programación, RAM y almacenamiento.

Un DL tiene escalado horizontal, lo que quiere decir es que tienes más recursos informáticos en paralelo, pero de menores prestaciones. Spark es el framework que nos permite trabajar en paralelo en el mundo del data. 


<br>


## Definición del Dato

Un dato es una medición objetiva. Cuando hablamos de datos estamos hablando de hechos. Por otro lado, la información es lo que nosotros generamos de manea subjetiva a partir de unos datos. Cuando cogemos una base de datos lo que queremos es construir información a partir de esos datos. La información tiene un problema, y es que al ser subjetiva no es intercambiable, ya que cada persona puede generar una información distinta a partir de los mismos datos. De este modo, los sistemas utilizan datos, y las personas información. Por ello, si no conseguimos transformar los datos en información no somos capaces de transmitir valor a las personas. 

El conocimiento se cataloga de la siguiente forma de la parte más baja a la parte más alta:

 1. Datos: Tomar las decisiones a este nivel significa mucho riesgo

 2. Información

 3. Conocimiento

 4. Sabiduría: Las decisiones a este nivel suponen el menor riesgo para la empresa, pero no siempre va a ser posible estar en este nivel.




Las empresas toman las decisiones a diferentes niveles, y nosotros tenemos que ayudarlas a tomar decisiones cuanto más arriba del nivel de conocimiento posible. 


<br>
<br>

## Ciclo de vida de los datos

El ciclo de vida de los datos se divide en:

1. Crear. En este primer paso los datos (estructurados o no estrucutrados) se crean

2. Guardados. Una vez que son creados se guardan en algún sitio. Hay que asegurar la protección de los mismos.

3. Uso. En este paso., los datos son visualizados, procesados, modificados y guardados. Se aplican controles de seguridad.

4. Compratidos. Los datos se mueven en diferentes localizaciones publicas o privadas y son usados por diferentes data owners desde diferentes dispositivos y plataformas.

5. Archivados. En algun momento los datos dejan de ser usados y se archivan.

6. Destruidos. Cuando el volumen de datos archivados alcanza cierto nivel, los datos tienen que ser destruidos para evitar el exceso de acumulación.

<br>

<p align="center">
<img src="https://www.clicdata.com/wp-content/uploads/2022/06/data-lifecycle-management-process.jpg" width=300>
</p>


<br>
<br>

## Arquitectura orientada a datos

Uno de los problemas que se suelen tener en el mundo de los datos es como diseñamos nuestra arquitectura. Para construir estas arquitecturas se suele utilizar [UML][uml].


<br>
<br>


## _Clase 05/11/2022_

## Gobierno del Dato


Estamos en la 4ª revolución industrial. La principal diferencia es que no hay una nueva tecnlogía, simpoelmente la revolución está basada en los datos y su análisis. Se espera que el PIB mundial se multiplique x4. Los 3 líders mundiales están basados en el dato (Amazon, Apple y Google). 


<p align="center">
<img src="https://cdn.statcdn.com/Infographic/images/teaser/17539.jpeg" width=400px>
</p>



Los datos son la materia prima que genera petróleo. Sin capacidad para darles sentido, no valen nada. 


### **Ciclo de vida del dato**

1.  Captura

2. Almacenamiento

3. Uso

4. Gestión

5. Protección 

6. Borrado


<p align="center">
<img src="https://www.juanbarrios.com/wp-content/uploads/2020/04/FasesCicloVidaDato-scaled.jpg" width=500px>
</p>


Definición gobierno dato:

>Es la coordinación formal de personas, procesos y tecnología que permite a una organización utilizar los datos como un activo al que sacarle valor.

Gobierno del dato facilita que todos los departamentos de las empresas tengan acceso fácil y rápido a los datos. Tipos de modelos:


- Descentralizado

- Federal descentralizado

- Federal centralizado

- Centralizado

No existe un modelo ideal, ni que sirva para todas las empresas. El modelo epnderá de la madurez de la organización, las capacidades, la cultura, las iniciativas y el proceso de toma de decisiones. Si tenemos un empresa muy poco madura, utilizamos un modelo centralizado, cuya despentaja principal es que da poco lugar a la creatividad.


Objetivos gobierno de dato:


- Reducir riestos y costes

- General la suficiente calidad en los datos

- Cumplir con las regulaciones y apoyar en la seguridad

- Habilitar un lenguaje común en la organización

- Democratizar el dato

- Cimentar la capacidad analítica


El 91% de las empresas invierten en Big Data e IA, pero solo el 31% consigue una solución válida. ¿Por qué pasa esto?

1. La iniciativa es liderada por IT con un punto de vista sólo técnico

2. El Gobierno del Dato es entendido como un proyecto, en lugar de una iniciativa estratégica continua a largo plazo

3. La estrategia de datos y el gobieno no están alineados con la estrategia corporativa de la organización.

4. No se tiene conocimiento previo del panorama de datos dentro de la Organización

5. Se trata de aobrdar todo a la vez, en vez de hacerlo de manera incremental

6. No involucrar a todos los stakeholders, desde los usuario de negocio hasta los técnicos


Para evitar esto, hay que realizar estrategias de Analítica sin tener definida e implantada una estrategia de gobierno del dato es como fabricar un submarino descapotable. 

Estrategia gobierno del dato

**Paso 1.** Endender la situación

**Paso 2.** Marcar unos objetivos

**Paso 3.** Definir un camino

**Paso 4.** Involucra a las personas y gestiona el cambio

<br>

**11 pilares de gobierno del dato**

<p align="center">
<img src="https://datos.gob.es/sites/default/files/u322/gobierno_del_dato.jpg" width=400px>
</p>


Pilar Estructura de gobierno: se define la estrategia de datos a seguir en la compaía, el tipo de gobierno que quermos tener, las políticas a cumplir, creamos las métricas a utilizar y definios los roles y responsabilidades. 


Los 3 principales roles de gestión de datos son:

- Data Owner: persona responsablde del dato dentro de su dominio

- Data Steward: quien se encarga de la parte más técnica y negocio

- Data Custodian: la parte IT que solventa los problemas


Pilar arquitectura del dato: los objetivos principales son traducir las necesidades de negocio en tecnlogia, ver como va a evolucionar a futuro y definir los modelos que se van a utilizar



Los **datos maestros** son el conjunto de identificadores que proporcionan contexto sobre los datos comerciales, como la ubicación, el cliente, el producto, el activo, etc. Son los datos centrales que son absolutamente esenciales para ejecutar operaciones dentro de una empresa o unidad comercial.



## Metadatos

Definición

>Son datos que describen otros datos. Literalmenet significa "más alla de los datos". Son altamente estrucutrados y describen características como el contenido, información, calidad y seguridad. 


Ejemplo metadato:

<p align="center">
<img src="https://media-exp1.licdn.com/dms/image/C4D22AQGtjgZqq0qLlA/feedshare-shrink_2048_1536/0/1654617734356?e=2147483647&v=beta&t=RAj0L-4YCc-xEm0pVhfSD9yRSudHfqsa6ZUlvd7oQDM" width=400px>
</p>



<br>

<br>



## Calidad del dato

La calidad del dato es un activo y siempre hay que producirla. Es también un pilar fundamental del gobierno del dato.


Objetivo de la calidad del dato

>Es garantizar el nivel válido de aeptaciónsegún unas dimensiones, requerido para cada dato, en funcion de su uso.


Beneficios:

- Seguridad

- Confianza

- Ahorro

- Valor


**Dimensiones de la calidad del dato**


<p align="center">
<img src="https://bigdatamagazine.es/wp-content/uploads/2022/07/Infografia-1-1024x683.png" width=500px style="background-color:white;">
</p>


Principales errores de calidad:

- Las manualidades: introducir datos manualmente cause muchos errores

- Adquisición e integración de datos externos que ya estaban mal

- Procesos ETL (Extract Transform Load)

- Migraciones de Datos

- Fusiones de BBDD

- Falta de gobernanza en los sistemas



Principales procesos de Calidad del dato

- Perfilado del dato

- Limpieza del dato

- Validación del dato

- Homogeneización

- Enriquecimiento



**Herramienta para trabajar calidad del dato**

<https://www.trifacta.com/start-wrangling>



<br>
<br>

## _Clase 12/11/2022_


## Visualización de datos

>"Si no sabes cómo hacer la pregunta correcta, no descubrirás nada" (Edward Deming)



### **Tableau**

Definión:

>Herramienta que te permite crear flujos de extracción, transformación y carga de tus datos.


Tableau prep es una herramienta ETL de Tableau. Fue diseñada por la compañía para ayudar a los data analyst a hacer operaciones ETL y no usar solo Tableau para visualizar datos. No obstante, en grandes compañias no se usa puesto que no es la más potente para operaciones ETL. En grandes empresas se suele utilizar Tunnel y Integration services (Microsoft).

 


Para trabajar en equipo, primero se desarrolla en Tableau Desktop y después se publica en Tableau Online o Server para que todo el mundo pueda utilizar el Dashboard. 


Resumen:

1. Preparar el dato --> Tableau Prep


2. Desarrollar dashboard --> Tableau Dekstop

3. Publicar y visualizar datos --> Tableau Online o Server





Recursos Online para Tableau:

- [Tableau Help](https://www.tableau.com/support/help): página de artículos técnicos y prácticos sobre como desarrollar en Tableau 


- [Tableau Commnunity](https://community.tableau.com/s/): Sito oficial de Tableau donde la comunidad responde preguntas


- [Tableau Public](https://public.tableau.com/app/discover): tiene las mismas características que Tableau desktop, excepto que te puedes conectar a otro tipo de bases de datos, y que se guardan datos en un servidor público


- [Knowledge Base](https://www.tableau.com/support/knowledgebase): similar a Tableau help pero con más info y con cursos para aprender Tableau




En Tableau se trabaja por hojas para montar los gráficos, luego se juntas las hojas en un Dashboard, y por último hay un apartado de historias donde puedes combinar varias hojas y/o varios Dashboard.


Una vez que abrimos una hoja, las variables se dividen automáticamente en aquellas con las que puedo hacer una operación aritmética (precio, descuento, cantidad, etc), y entidades en las que no puedo hacer estas operaciones.


Por defecto, la conexión con nuestros datos es en tiempo real y, conforme se vayan actualizando, se actualizarán en Tableau.


En los campos calculados, es muy importante conocer las funciones de agregación, para por ejemplo conseguir que el % de beneficio de cada producto aparezca correctamente.

[uml]:<http://www.uml.org/>
