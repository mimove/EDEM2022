# Notas Clase Introducción Cloud

## _Clase 19/01/2023_


En los años 60 se trabajaba ya con ordenadores mainframe dentro del sector de la banca. Estos ordenadores eran muy caros, y lo que hacían las empresas era compartirlos para reducir el coste. A finales de los 60, aparece ARPANET como precursor de lo que sería la red. En 1970 aparecen las máquinas virtuales, que son ordenadores con sistemas operativos que se pueden crear y destruir dentro de memoria y de forma rápida. El Cloud nace en 1997 y en 1999 empiezan a producirse empresas cuyo modelo de negocio es el SaaS. En 2003, aparece el concepto de Virtual Machine Monitor, en el que diferentes usuarios utilizan el mismo ordenador pero con OS diferentes y sin conexión entre las VM de un usuario y otro.

Entre 2002 y 2006 Amazon lanza AWS y hasta a día de hoy es el mayor proveedor de servicios Cloud y nace el concepto de Infraestructure as a Service (IaaS). 

<p align="center">
<img src="https://mma.prnewswire.com/media/1807513/CIS_Q122.jpg?w=500" width = 500px>
</p>

<br>

## Modelos comunes de deployement:

- Privado: me quedo en mis propios servidores

- Público: despliego mis aplicaciones en el Cloud

- Híbrido: hago una mezcla entre mis servidores y el Cloud


A día de hoy, el modelo Cloud es el más extendido. El privado se suele utilizar en el sector de la banca actualmente. El híbrido es lo que muchas empresas tienen a día de hoy, que están empezando a hacer migraciones de Private a Public.


<br>

## Cloud service providers

Son los servicios que consumimos en el Cloud. Por ejemplo, Netflix, Google Drive, Gmail, Dropbox, etc.

Cuando nosotros consumimos un servicio como Netflix, solo estamos viendo la punta del iceberg.


<p align="center">
<img src="https://www.securityindustry.org/wp-content/uploads/2017/04/Hebert-Iceberg-graphic-Scalability-min-1024x665.jpg" width=500px>
</p>


Cuando contratamos un servicio como Netflix, no solo estamos pagando por ver películas, estamos pagando por todo lo que hay por debajo (ej: el monitoreo del servicio, el despliegue de la infraestructura, los servidores, etc.)



**IaaS vs PaaS**

En el Platform as a Service (PaaS), yo estoy utilizando tanto la infraestructura como el Software de un proveedor de Cloud. Esto es menos flexible que un IaaS, donde yo tengo que instalar todo desde 0, pero tiene la ventaja de que es mucho más rápida la curva de aprendizaje y su escalabilidad.

<p align="center">
<img src="https://www.eginnovations.com/blog/wp-content/uploads/2021/11/Onsite-Iaas-Paas-Saas.jpg?no" width=500px>
</p>

Un Data Engineer debería estar en el PaaS y no en IaaS


<br>


## Cloud providers

- AWS: Da 2 tipos de servicios. El EC2 es el servicio de computación, y el S3 el de almacenamiento. AWS nació como IaaS y ahora también da servicios de PaaS


- GCP: Google es el último gran player en llegar, pero el que más rápido está cogiendo cuota de mercado en los últimos años.

- Azure: Tiene más cuota de mercado de momento que GCP, pero menos que AWS.


A día de hoy hay muchísimos más proveedores de Cloud. 


## Ventajas

- Rápida dotación de infraestructuras. Un cloud provider tarda entre 30s y 1min en darnos una máquina.

- Seguridad. Aunque en principio parezca que no, un cloud provider es mucho más seguro que tener las aplicaciones on premise.
- Mejora en la disponibilidad y fiabilidad. Al tener máquinas replicadas en todo el mundo, un cloud provider tiene mucha más fiabilidad que un servicio on premise

- Reduce la inversión a realizar y los costes proporcionales.

- Pagas por uso

- Muchos servicios SaaS. No hay un instalable que poner en tu ordenador, si no que directamente consumes una API

<br>

## Desventajas

- Problemas de vulnerabilidad.

- Reducción del control operacional.
- Portabilidad limitada entre Cloud Providers. Para solucionar esto ha surgido una línea de trabajo que se llama Infraestructura como código (eg. Terraform)
