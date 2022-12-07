# Notas clase Kafka

## _Clase 24/11/2022_


## Introducción

Kafka intenta solucionar un problema de sistema de mensajería. En un sistema de mensajería se pueden dar 2 casos:

- Sistema de mensajes punto a punto: los mensajes se transmiten en cola. Uno o varios consumidores pueden consumir los mensajes de la cola, pero un mensaje concreto sólo puede ser consumido por un consumidor como máximo

- Sistema de mensajería de publicación-suscripción: los mensajes se mantienen en un tema. A diferencia del sistema punto a punto, los consumidores pueden suscribirse a uno o más temas y consumir todos los mensajes de ese tema. En el sistema de publicación-suscripción, los productores de mensajes se llaman editores y los consumidores de mensajes se llaman suscriptores.


Este tipo de sistemas, desacopla el emisor y el receptor, de manera que si uno de ellos no está conectado, los mensajes se siguen pudiendo almacenar y llegar al receptor. También el uso de tener un servidor entre medias hace que podamos desacoplar tecnologías. Kafka es una tecnología de publish-subscribe messaging donde puedo tener muchos senders y muchos receivers.



### Record retention

Los registros publicados se retienen durante un periodo que configuramos. Los registors están disponibles para consumirlos hasta que sean descartados por una de estas 3 causas:

- Tamaño

- Tiempo

- Compactación

<br>

## Productores

Un productor de Kafka es una aplicación que puede actuar como fuente de datos en un clúster de Kafka.

Un productor puede publicar mensajes en uno o más temas de Kafka 

Métodos de envío existentes:

- Fire-and-forget: No esperar al ACK - rendimiento muy alto - acks=0

- Asíncrono: Esperar el ACK del Líder - acks=1

- Sincrónico: Esperar al ACK del Líder + Réplicas - Seguro - acks=todos

Los productores de Kafka intentan reunir los mensajes enviados en lotes para mejorar el rendimiento.

Asignación de particiones

- Round-robin

- Función de partición basada en la clave


<br>

## Consumidores

Las particiones se asignan a los consumidores dentro del grupo de consumidores
Los consumidores recuerdan las particiones donde se - se comprometen con Kafka.
Mover la propiedad de la partición de un consumidor a otro se llama rebalanceo. Ventana corta de indisponibilidad de todo el grupo de consumidores.

<br>
<br>

## _Clase 26/11/2022_

## Kafka Streams

Definicion:

>Un flujo es la abstracción más importante proporcionada por Kafka Streams: representa un conjunto de datos ilimitado y en continua actualización.
Una partición de flujo es una secuencia ordenada, reproducible y tolerante a fallos de registros de datos inmutables, donde un registro de datos se define como un par clave-valor.


Una partición de flujo es una secuencia ordenada, reproducible y tolerante a fallos de registros de datos inmutables, donde un registro de datos se define como un par clave-valor.

- Procesamiento en tiempo de eventos con ventanas, uniones, agregaciones,... 

- Admite la semántica de procesamiento "exactamente una vez".

- Procesamiento con y sin estado


**DSL de Kafka Streams**

Una API de alto nivel que proporciona las operaciones de transformación de datos más comunes, como map, filter, join y aggregations, de forma inmediata

<br>

**API de procesadores**

Una API de bajo nivel que permite añadir y conectar procesadores, así como interactuar directamente con los almacenes de estado

<br>

## _Clase 01/12/2022_

## Schema Registry

Sirve para poder guardar los contratos AVRO de forma centralizada en un servidor Linux para que puedan ser utilizados por los diferentes departamentos de una empresa. Sus principales beneficios son:

- Los flujos de trabajos son resistentes.

- Es coste efectivo.

- Tenemos una evolución del schema segura.

- Las data pipelines son resilientes.

- Data discovery para que los departamentos puedan descubrir los datos que tenemos.

- Se obliga a tener una política de datos en la empresa.



## Kafka Connect

Es un framework para integrar fácilmente Kafka con otros sistemas.


