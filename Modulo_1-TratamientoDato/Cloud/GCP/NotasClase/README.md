# Notas Clase Google Cloud Serverless

## _Clase 27/01/2023_

* Formación https://thecloudgirl.dev


Serverless da la posibilidad a las empresas de probar y escalar soluciones tecnológicas de forma muy sencilla. 

Con serverless, no te importa donde se está ejecutando tu código. Sólo te importa tu código y eso ayuda a mejorarlo más rapidamente.

## Ventajas:

- Toda la arquitectura administrada por Google.
- Auto escalable y elástica (cuando hay pico de demanda aumentan los nodos y luego vuelven a disminuirse).

- Pagas por lo que usas

- Disminuye el tiempo de sacar una solución al mercado.


## Desventajas:

- Pierdes el control de todo lo que pasa por debajo

- Es muy difícil testear en local, tienes que deployearlo y esperar a que se ejecute.



## Casos comunes de uso:

- Integración continua (Cloud Build)

- CRON architecture

- Data processing y IoT


- Machine Learning

- Constuir RESTful APIs




## Dataflow

Cloud Datafusion es un servicio de procesamiento de datos sin servidor para ejecutar pipelines de haces de Apcache batch y streaming. 

Beam es un sistema para crear pipeline de procesamiento de datos (similar a Spark). Se puede ejcutar en Local, en Dataflow, con Spark y con Flink.


Fuentes y alamacenamiento de Dataflow:

- PubSub
- BigQuery
- Cloud Storage
- DataStream
- Firestore
- BigTable

Conectores de terceros:

- Apache Kafka
- Mongo DB

También puedes hacer conectores personalizados.


Dataflow se puede utilizar de tres maneras:

- Dataflow Templates
- Dataflow SQL
- Dataflow Notebooks.



