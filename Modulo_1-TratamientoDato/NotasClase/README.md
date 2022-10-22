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











[uml]:<http://www.uml.org/>