# NOTAS CLASE CERTIFICACIONES AZURE

## _Clase 04/02/2023_

<br>

Tiene 3 certificaciones básicas:

- Azure fundamentals (la más sencilla y cubre todas las herramientas)

- Azure data fundamentals (fácil y basada solo en Data)

- Azure AI fundamentals (fácil y basada en AI)



Los contenidos se dividen en:

- 25-30% sobre conceptos de cloud.

- 35-40% Actquitectura y servicios

- 30-35% Data governance y mantenimiento.

<br>

## Cloud computing

La computación en nube es la prestación de servicios informáticos a través de Internet, lo que permite una innovación más rápida, recursos flexibles y economías de escala.

Tiene que tener las siguientes características:

- Escalabilidad

- Elasticidad

- Agilidad

- Tolerancia a fallos
- Recuperación de fallos

- Alta disponibilidad

- Economías de escala


Hay 3 tipos de cloud: público, privado e híbrido.

<br>





## Conceptos básicos:

- Datacenter: infraestructura donce están ubicados los servidores del cloud.

- Regiones: área geográfica. Azure cuenta con +50 regiones. Tiene 1 o más datacenter conectados con baja latencia. Algunos servicios están sólo disponibles en una región.
- Zonas de disponibilidad: Característica de una region. Es un agroupamiento de instalaciones físicas que están separadas. Está diseñada para proteger a un data center de fallos. Hay 2 categorías de servicios (servicios zonalas y zona de servicios redundante). No está soportada en todas las regiones. Una zona está compuesta por uno o más datacenters.
- Regiones en parejas: cada región está emparejada con otra región construyendo una pareja entre ellas.

- Recursos: los objetos usados para manejar los servicios. Se guardan como JSON
- Grupo de recoursos: almacena recursos relacionados de forma lógica (tipo, tiempo de vida, departamento, etc.)
- Manager de recursos: capa de gestión de todos los recursos y grupos de recursos.



- Máquina virtual: emulación de software de máqinas físicas. Es un IaaS. Tienes total control sobre el sistema operativo. 

<br>

## Bases de Datos

- Azure SQL: está basada en las versiones más estables y recientes de servidores sql. Acepta operaciones masivas en paralelo. Se puede instalar el servidor de sql en una máquina virtual. 

- Azure cosmos DB: bases de datos no-sql con conectividad en múltiples regiones.

<br>

## Azure IoT Hub

Es un PaaS. Gestiona los servicios con comunicaciones bidireccionales. Es altamente seguro y escalable. Puedes usar imagenes SKD en un montón de lenguajes de programación. Acepta múltiples protocolos (HTTP, HTTPS, etc.).


<br>

## Azure IoT Central

Es un SaaS. Para usar plantillas específicas de una industria. No se necesita conocimiento teórico extenso.

<br>

## Azure Sphere

Una solución de software y hardware que ofrece funciones de comunicación y seguridad para dispositivos IoT.


<br>

## Azure Databricks

Es una plataforma analítica PaaS de Apache Spark. Espacio de trabajo unificado para bloc de notas, clúster, datos, gestión de acceso y colaboración. Se integra muy bien con servicioes muy utilizados de Azure data. La certificación con más valor en el mercado es de Azure Databricks the Spark con Scala.

<br>

## Azure Machine Learning

Plataforma basada en la nube para crear, gestionar y publicar modelos de aprendizaje automático.



<br>


## Azure DevOps solutions

DevOps es un conjunto de prácticas previas que combinan desarrollo y operación. El objetivo de DevOps es acortar el ciclo de vida del desarrollo proporcionando capacidades de integración y entrega continuas, al tiempo que se garantiza la alta calidad de los resultados. Dentro de Azure se ecnuentra Azure DevOps, que tiene varios servicios que ayudan al ciclo DevOps. 