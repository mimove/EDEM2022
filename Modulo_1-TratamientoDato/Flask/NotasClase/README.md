# NOTAS CLASE FLASK

## _Clase 16/12/2022_

Hace unos años todas las aplicaciones estaban programadas usando muy pocos lenguajes de programación. Las principales desvantajes de esto son:

- Qué pasa si las tecnologías cambian?

- Que pasa si queremos escalar?

- Que pasa si queremos dividir el trabajo en equipos?

- Como de reutilizable es tu código?

- Qué pasa si un 3rd party quiere ver parte de tu código?


Esto se cambió a hacer arquitecturas de microservicios en la que diferentes tecnologías se encargan de cada una de las partes de la aplicación (front-end, logica, database, etc). El problema es como conecto ahora todos los microservicios entre sí. Para ello, se desarrollan las APIs que permiten interconectar servicios.

<br>

## Swagger

> Swagger permite describir estrucutras de tus APIs de forma que las máquinas puedan leerlas. 

Características:

- Puede construir automaticamente documentación interactiva de la API con la estrucutra de lectura.

- Puede generar la client lib de la API en numerosos idiomas


Estructura básica:

<p align="center">
<img src="https://developer.ibm.com/developer/default/articles/wa-use-swagger-to-document-and-define-restful-apis/images/image001.png" width=500px>
</p>


