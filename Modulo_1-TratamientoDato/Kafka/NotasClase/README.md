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

- 