# Description

Hagamos un cambio y empecemos con Kafka, para ellos tenéis un entorno casi completo funcionando. Vuestro reto, es hacerlo funcionar y conseguir tener en esta URL los mensajes enviados por nuestro producer:

http://localhost:8080/ui/clusters/local/topics

La segunda parte del reto, es conseguir crear un contenedor que sea consumidor y recoja los mensajes de tópico y los meta en una base de datos con todo lo visto en los anteriores.

## _Notas Miguel_

Para este ejercicio se ha creado un productor que consume datos de la API de Mockaroo, en la cuál se han generado una serie de esquemas para generar datos aleatorios que sirvan para rellenar las tablas product, users, status_names, city, country y store_id. Una vez el productor consume los datos de la API, la info es enviada en mensajes con formato json a cada tópico en Kafka. También se ha creado un consumidor, que se subscribe a todos los tópicos creados por el productor, y ejecuta sentencias SQL para cargar los datos en la base de datos mySQL. Por último, a través de Grafana se pueden visualizar las ventas en tiempo real, como se muestra en el video que hay en la carpeta [video](./video/)


