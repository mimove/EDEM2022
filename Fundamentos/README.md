<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
# FUNDAMENTOS DEL DATO
=======
# FUNDAMENTOS GENERALES

(**Codesignal.com es otra web de retos de programación)

## _Clase 29/09/2022_

<br/>

### **Tipos de lenguajes de programación**

Lenguaje de programación: es aquello que nos permite comunicarnos con una máquina. Nos podemos comunicar a diferentes niveles. En binario sería el nivel más bajo, y con lenguajes como Python sería uno de los niveles más altos. Estos lenguaejs se clasifican en 3 grandes grupo: compilado, interpretado e intermedio.


En el lenguaje compilado, yo escribo en el lenguaje de programación correspondiente, en un segundo paso se traduce a lenguaje máquina (se compila el código) y por último se ejecuta.
Uno de sus mayores beneficios es que hacen un uso eficiente de la memoria

En el lenguaje interpretado, yo como usuario soy capaz de escribir directamente en un lenguaje que la máquina entiende (no requiere del paso de compilación). 

Un lenguaje intermedio es aquel en el que se requiere hacer una compilación del codigo fuente pero necesita una ayuda para ser ejecutado. Estos lenguajes necesitan una máquina virtual para funcionar. Esta máquina es un intérpete que traduce el código de alto nivel al lenguaje máquina.


**Los lenguajes que vamos a ver principalmente entro del máster son Python, Java y Scala. 

<br>

La caché de un ordenador es la memoria a corto plazo. Sirve para acceder a ciertos datos con mayor rapidez. Los datos que almacena pueden ser el resultado de un cálculo anterior o el duplicaod de datos amacenados en otro lugar. 


<br/>

### **Velocidad de Procesamiento**

Otro concepto importante dentro del mundo de los datos es la velocidad de procesamiento. Esta velocidad es más importante cuanto más grande es la cantidad de información que procesamos. De más lento a más rapido los modos de velocidad son: 

 - Modo batch. Va por lotes. Yo empiezo a procesar en cierto momento la información que quiero por un tiempo determinado. Un ejemplo podría ser la gestión de stock de un supermercado como Mercadona.
  
 - Modo batch en grandes volúmenes. Programa es apache spark. Es parecido al modo batch pero la ventana de tiempo es más pequeña. Spark soluciono el problema del modo batch normal haciendo procesado de datos en paralelo para acortar las ventanas de tiempo de procesado.
  
 - Microbatching: con spark streaming la ventana de tiempo es muy muy pequeña. Esto se puede considerar prácticamente como un procesamiento en tiempo real, pues las ventanas son solo de unos pocos minutos.
  
 - Streaming: con apache flink se permite el procesamiento por debajo de un segundo. Esto se utiliza por ejemplo para procesar las transacciones de un banco o la bolsa.



El coste de procesar la información se incrementa desde el modo batch al modo streaming. Por ello, al hablar con un cliente sobre un proyecto hay que tener claro los tiempos de procesamiento que serán óptimos en función del coste que se esté dispuesto a pagar. Es muy importante por tanto aprender a dimensionar las soluciones a los problemas que se nos presenten. Para ser un buen Data Engineer hay que saber evaluar esto muy bien.


<br>

### **Cores vs Threads**

Hay una diferencia entre los cores y los threads de un ordenador. Los cores son el numero de unidades de procesamiento que tiene mi ordenador. Mientras que los threads (o hilos en español) son las tareas que puede ejecutar cada core. Para trabajar en paralelo en el mundo del data se utiliza spark.


<br>

### **Log**

El log es el fichero de registro donde se guardan todos los acontecimientos que han ido afectando al sistema informatico.


<br>


### <b>Protocolos de comunicación: </b>

 - FTP: sirve para mover ficheros entre máquinas
  
 - SSH: sirve para ejecutar comandos en una máquina.
 - SMTP: es un protocolo simple para intercambio de emails.


Al conectarse a una máquina se hace a través de un puerto. Son la manera que tenemos de entrar a un servidor. Cada protocolo tiene unos puertos estándar por los cuales se puede acceder y, en general, no se puede acceder por otros. Por ejemplo, el SSH se conecta por el 22, el FTP por el 21 o HTTP por el puerto 80. Para hacer una conexión con un protocolo a través de un puerto que no es estándar, tanto el servidor como el cliente se tienen que poner de acuerdo. 

Nosotros usaremos puertos cada vez por ejemplo que levantemos un Docker.


<br>

### <b> Cliente-Servidor</b>

Es una arqutectura con un modelo de diseño software en el que las tareas se reparten entre los proveedores de recuros o servicios (servidores) y los demandantes (clientes). Se implementan a través de APIs que es la manera en la que, por ejemplo, conseguiremos los datos de un sitio (**get**), o subiremos datos (**post**), o modificaremos datos (<b>put</b>)

<https://cloud.google.com/vision/docs/drag-and-drop> tiene una API para devolver la info de las imágenes que procesa.


<https://reqin.com> Se utiliza para crear codigo en diferentes lenguajes para coger datos de una API


Las REST-APIs son aquellas en las que yo pregunto y obtengo respuestas.

<br>

### **CPU-GPU-TPU**

CPU es una unidad especializada en el procesamiento lineal.

GPU es la unidad que procesa en paralelo las tareas que le pedimos que ejecute. Tradicionalmente se ha utilizado para procesamiento gráfico. Pero en los ultimos años se están ampliando los usos de las GPUs. Los modelos de Deep Learning de imagenes se entran mediante GPUs

TPU está especializada en multiplicar matrices y hacer otras operaciones computacionales con ellas.


<br>

### **Tipos de Archivos**


Hay cuatro tipos de archivos que serán los más comunes en el Máster:

 - CSV
 - Excel
 - TXT
 - JSON

Cada tipo de fichero por buenas prácticas tiene que tener como contenido el formato esperado para su extensión. Por ejemplo, en un CSV no debo guardar contenido de texto plano, si no contenido separado por comas, ya que la extensión del fichero no determina su contenido, y cuando trabajamos con ficheros de datos es importante saber para lo que sirve cada extensión. Excel y CSV son formatos diferentes. Un fichero de Excel tiene contenido binario con formato propietario que hay que leer mediante una librería en Python que permite leerlo.


<br>


## ****CheatSheet**

Deberíamos tener las cheatsheet de GIT, Python y UNIX impresas.
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

