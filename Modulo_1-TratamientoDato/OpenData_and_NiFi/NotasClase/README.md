# Notas Clase OPEN DATA + NIFI

## _Clase 29/10/2022_

<br>

## **Introducción**



**Definición**:

>Open Data se trata de datos que son abiertos y se pueden usar para diferentes temas. Son datos que se pueden usar sin ningún tipo de restricción.



Antiguamente era casi imposible conseguir datos de organismos gubernamentales, pero hoy en día la situación ha mejorado, aunque todavía esta lejos de ser una situación ideal. 


<br>

### **Tipos de Open Data**


- Gubernamentaltes: se proveen por diferentes organismos gubernamentales (locales, regionales, nacionales, etc). Son puramente Open Data. Ej: Ayuntamiento Valencia, European Data Portal

- Estadísticos: pueden ser considerados un sub tipo de datos gubernamentales. Proveen información económica y estadística. Ejemplos: INE

- Datasets públicos: Son usados normalmente para testeo o para entrenar modelos de Inteligencia Artificial. No pueden ser considerados como fuente de datos, si no como una data set individual. Ejemplos: Google Dataset Search


- Comerciales: son datos que se proporcionan con fines comerciales. Se paga para usarlos aunque normalmente se proveen ciertos datos de forma gratuita. Ejemplos: Redes sociales, Datos financieros (IEX, Morning star, ...).




<br>


### **Formatos de datos**

CSV (Comma Separated Values): No es el mejor sistema para estructurar dato

<p align="center">
<img src="https://wiki.teltonika-networks.com/wikibase/images/3/33/RMS-CSV-file-example-notepad.png">

</p>


JSON (JaaScript Objet Notation): Uno de los mejores formatos para guardar datos

<p align="center">
<img src="https://miro.medium.com/max/1016/1*q98TVdovx6JBLA72R1xtuA.png" width =300px>

</p>


XML (Extensible Markup Language): Muy usado hace años. Con menos uso a día de hoy.

<p align="center">
<img src="https://cdn.educba.com/academy/wp-content/uploads/2020/11/XML-File-1.6.png" width =500px>

</p>


Formatos de información geográfica:

- WMS (Web Map Service): estándar internacional por OGC. Servicios de georeferencia en mapas de imágenes.

- GML (Geography Markup Language): Desarrollado por OpenGIS. Basado en XML

- KML (Keyhole Markup Language): Utilizado por Google Earth. Es similar a GML y puede ser comprimido a KMZ.


News feeds (Atom & RSS)

- Escrito en XML

- Se entrega vía HTTP

- Muchos lectores disponibles


RDF (Resource Description Framework)

- Definido por el W3C, usado para modelado de recursos web.

- Similar a diagramas de claes.

- Utiliza SPARQL como lenguaje de queries.

- Puede ser serializado a diferentes formatos (Turtle, JSON, XML, ...)

<br>

### **Mecanismos de entrega**

**Descarga directa:** Es la forma más facil de descargarse los datos. Pero, no es la forma ideal para descargarse datos.

**REST API:** llamamos a una URL que nos descarga los datos normalmente en formato JSON. La desventaje es que tengo que ir a pedirlos a la URL y hay veces que necesito que los datos me lleguen todo el tiempo sin tener que solicitarlos.

**Real-Time:** los datos se entregan en tiempo real. Lo más normal para conectarse a este tipo de servicios es vía websocket. La principal diferencia de un websocket con una API es que primero me tengo que conectar, y luego subscribirme a algunos datos en concreto. De esta manera, cada vez que se generen datos nuevos, el websocket me devuelve esta información a la que estoy subscrito.

**Feeds:**


<br>

### **Frecuencia**

Dependiendo de la naturaleza del dato y la frecuencia a la que se actualiza, puede ser entregado de diferentes maneras. 

```
Real-Time              Daily         Monthly        Yearly
------------------------------------------------------------------------------>
         Near-real-time       Weekly       Quarterly      Ad-hoc (on-request)
```




<br>

<br>

## Fuentes de datos


### **Gubernamentales**


Ejemplos:

<u>**Ayuntamiento de Valencia**</u>

<https://www.valencia.es/dadesobertes/va>

<br>

<u>**Gobierno de España**</u>

<https://datos.gob.es>


<br>

<u>**Unión Europea**</u>

<https://data.europa.eu/es>

<br>
<br>

### **Estadísticas**

Ejemplos:

<u>**INE**</u>

<https://www.ine.es>


<br>


<u>**Eurostat**</u>

<https://ec.europa.eu/eurostat>

<br>

<u>**Banco Mundial**</u>

<https://data.worldbank.org/>

<br>

<u>**Gapminder**</u>: Para analizar datos

<https://www.gapminder.org/tools>

<br>



<br>
<br>

### **Datasets públicos**


Ejemplos:

<u>**Google Search**</u>

<https://toolbox.google.com/datasetsearch>

<br>

<u>**Curated lists**</u>


<br>
<br>

### **Comerciales**

Hay muchas compañías que proveen datos con diferentes modelos de monetización (DaaS, pay per use, dowloadable content) y se adquieren a través de proveedores de datos.

Los más habituales son: Redes Sociales, Económicos y financieros, Datos simuladots, Cloud datasets y muchos otros (Crypto exchanges, Google Analytics, etc.)




<br>

<br>

<br>


## INGESTIÓN PURA Y NIFI


### **Introducción**

**Definición:**
>La ingestion de datos es el proceso de adquirir datos desde sistemas de fuentes, y enviarlos (y/o almacenarlos) en un sistema. Un ejemplo típico de Data Ingestion is el envío de datos dentro de un Data Lake.


La adecuada ingestión de datos es clave para obtener un mejor procesamienot de los datos. Existen 2 formas de ingestión de datos:

- <u>**ETL**</u>: extraemos los datos de la fuente de datos, los transformamos y los guardamos. Es la forma tradicional de recoger los datos. Ejemplo: Business Inteligence, Data Warehousing, etc. Este modelo es más lento en la ingestión de datos y procesamiento.

- <u>**ELT**</u>: hoy en día como se gestionan los datos es extrayéndolos, los guardo sin transformar y luego ya los transformo.


<p align="center">
<img src="https://cdn.buttercms.com/qZu81OW0TwGL9mPvDHYs" width=600px>
</p>



<br>

### **Mejores prácticas**


1. **Alertas**: añadir alertas para detectar errores en la ingestión.

2. **Definir expectativas**: como la ingestion de datos no es sencilla, es necesario comunicar a los jefes y project managers unas tiempos de entrega realistas.

3. **Reutilización**: hacer plantillas para reutilizar frameworks de desarrollo ya que muchas pipelines de ingestión son repetititvas.

4. **Guardar una copia**: mantener una copia de todos los datos en crudo antes de aplicar transformaciones. Esto sire de backup en caso de fallo.

5. **Automatizar**: automatizar pipelines, definir SLAs y usar orchestration. Esto permite el monitoreo de equipos para avisarles en caso de que las pipelines fallen o tarden más de lo esperado

6. **Idempotencia**: las pipelines tienen que ser idempotentes, de manera que si ejecutas una operación muchas veces, el resultado siempre va a ser el mismo.

7. **Documentar**: documentar las pipelines: input, output y logica dentro del pipeline.

<br>

Estas prácticas son necesarias ya que la ingesta de datos es complicada. Los principales problemas son:

- La diferentes fuentes de datos te aportan los datos en diferentes formatos.

- La forma de entrega de cada proveedor es muy variada. Puedes estar leyendo de una base de datos, pueden venir los datos de un fichero en un SFTP, etc.

- Los proveedores de datos envían la información a frequencies diferentes desde real-time a en batch.


- La ingestión de datos no es algo estático, ya que las diferentes fuentes de datos van cambiando tanto el formato, como la forma de entrega como la frecuencia de entrega.


Para ayudar con esta resolución de problemas surgen las herramientas de ingestión de datos. Sus principales características ideales son:

- Es fácil conectarse a las fuentes de datos y añadir nuevas fuentes

- Son fáciles de usar (graphical interface)

- Tienen un buen catálogo de componentes

- Son escalables

- Se pueden monitorear

- Tiene trazabilidad para ver de donde viene el dato y porque procesos ha pasado


Las herramientas más comunes son: **NiFi**, **StreamSets**, **Airbyte**, Flume (para Big Data), Elastic, Splunk (muy especializado en gestión de logs), Fluentd, Informatica, Sqoop (para transferir datos de una base de datos a un Data Lake). Las 3 primeras son de ingestión pura.


<br>
<br>

### **Apache NiFi**


> Apache NiFi (Niagara Files) es un proyecto open-source de la funcación de software de Apache diseñado para automatizar el flujo de datos entre sistemas de software. Fue creada por la NSA en el 2006 y en el 2014 se convirtió en Open-Source.


Sus principales características son:

- Tiene una interfaz web

- Es altamente configurable

- Tiene trazabilidad de datos

- Diseñada para extender sus capacidades

- Es segura (SSL, SSH, HTTPS, contenido encriptado, etc)


Conceptos básicos:

- **FlowFile:** es el dato que está fluyendo desde la fuente hasta su lugar de almacenamiento. Ej: si de la API de Twitter cojemos tweets, cada tweet es un FlowFile

- **FlowFile Processor:** cada paso desde que lo coges de la fuente, lo modificas y lo dejas en el lugar de almacenamiento.

- **Connection:** las conexiones entre los diferentes FlowFile Processors.

- Process Group: forma de agrupar procesos.

- Controller


**FlowFile Anatomy**

Los FlowFile tienen una serie de atributos que sirven por ejemplo para enrutarlos. Po ejemplo el resultado de la petición a una API, la URL de la que viene, el tamaño del archivo, etc. Además de los atributos, el FlowFile tiene el contenido que queremos guardar.


