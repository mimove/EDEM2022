# FUNDAMENTOS DOCKER

En este modulo vamos a ver tanto Docker como Docker compose. Docker compose es como Docker, pero tiene más funcionalidades. 

<br>
<br>

## Virtual Machines

<br>

Antes de las máquinas virtuales, una web tenía que estar en una sola máquina, lo que lo hacía muy costoso de mantener. Esto implicaba comprar físicamente nuevas máquinas para poder desarrollar nuevas aplicaciones. También había problemas de ciberseguridad, por ejemplo en empresas como Inditex donde un atacante podría acceder a todas sus páginas web entrando solo por una.

Otro aspecto importante, es que la mayoría del tiempo solo se estaba usando un 5% de la aplicación.


La virtualización es hacer creer a los sistemas operativos que tenemos muchas más máquinas de las que en verdad tenemos.

Esto se convirtió en una manera muy efectiva de reducir costes. Ya que de una sola máquina podía dividirlas en 2 y "hacer creer" al sistema operativo que tenía 2 en vez de 1.


Ante ataques de ciberseguridad, el atacante solo tendría acceso a los datos de una máquina virtual, pero no al resto de máquinas.



Al hacer una virtualización, los recursos de un PC (RAM, HD, CPU, etc) se dividen a través de un software de virtualización en varias máquinas más pequeñas.



Una máquina virtual consume muchos recursos, por ello, a veces al hacer el escalado es posible que se caigan las máquinas que ya tenía.




Existen varios tipos de virtualización:

 - Virtualización del servidor: varios sistemas operativos sobre el mismo servidor
  
 - Virtualización de red: varios equipos conectados en una red
 - Virtualización escritorio: mi ordenador local está vacío, y me meto a una máquina donde está todo el escritorio
 - Virtualización de almacenamiento: tengo un gran disco duro que divido en cachito y dejo usar a muchos usuarios.




Una máquina virtual se crea a partir de una imagen donde está el Sistema Operativo. Desde dicha imagen es como se levanta la máquina virtual.




<br>
<br>



## Hypervisor

Los hipervisores más comunes son VirtualBox, Hypes-V y VMWare. Se utilizan como entorno gráfico para visualizar las virtualizaciones de disco.


<br>
<br>



## Virtualization in Cloud


Existen diferentes Cloud Providers. Los principales son Google Cloud, AWS, Azure, Oracle e IBM. Lo que están intentando estos tres proveedores es que las empresas dejen de tener equipos locales en sus empresas y trabajen en el Cloud.

En un Cloud tú puedes tanto levantar un sistema operativo desde 0, como levantar una máquina que ya tenga varias aplicaciones instaladas.


Levantar una máquina en un país o en otro influye en la latencia que va a tener el usuario cuando acceda a la aplicación que tenga desarrollada en la máquina. Por ejemplo, un usuario de España tardaría más en acceder una aplicación en el Cloud del Data Center de Google en USA que alguien de México.

También es importante el tema del país con la privacidad de datos. Hay aplicaciones que tienen que levantarse con una máquina en el país de los usuarios ya que hay leyes que dictan que los datos de los usuarios no pueden salir de cierto país o países.



Las specs de las máquinas son personalizables. Puedo coger una máquina de 1 CPU y 1 Gb de RAM (barata) o una de 32CPUs y 32 Gb (mucho más cara).


Los proveedores de Cloud te permiten también importar máquinas virtuales que hayamos generados nosotros en nuestros ordenadores.

Los cambios que yo haga dentro de la máquina virtual no se guardan en la imagen de la máquina ya que es inmutable. Se crea un espacio en disco por serparado que guarda la información que nosotros hayamos modificado. Los Cloud Providers cobran por ese espacio en disco usado, aunque la máquna esté parada.



<br>
<br>


## CI/CD
<br>

### Desarrollo Continuo (CD)
<br>

Al hacer un programa en un lenguaje de programación, el desarrollo no termina cuando consigo que el programa funciones, si no que tiene que pasar por una serie de fases:

 - Entorno desarrollo local: desarrollo el programa en mi ordenador
  
 - Entorno desarrollo integración: integro mi desarrollo con el resto del código
 - Entorno desarrollo pre-producción: se hacen test dentro de la empresa para ver que se usable para los usuarios finales
 - Entorno desarrollo producción: el programa al que accede el usuario final



A esto se le llama ciclo de vida de desarrollo del software. 




Los ciclos de desarrollo de software a día de hoy son muy cortos. Por ello, se utilizan metodologías ágiles para ir haciendo entregas al cliente final cada 2-3 semana y recibir feedback que me ayuda para continuar con el desarrollo del código acorde con lo que quiere el cliente. Esto mejora mucho la metodología de waterfall que se usaba antiguamente.


En metodologías agiles, la automatización de los procesos cobra mucha importancia, ya que los tiempos para pasar por todos los pasos de las fases de desarrollo hay que ir muy rápido para poder hacer entregas cada 2-3 semanas al cliente. Existen también herramientas que analizan el código para ir detectando posibles errores que introduce el desarrollador.


<br>

### Integración Contiua (CI)

Se utiliza Git para poder compartir el código que he desarrollado con el resto de progaramadores para continuar las siguientes fases del entorno de desarrollo. Las ramas de Git son cada una de las fases de desarrollo que tiene un software. 


El objetivo de trabajar así es principalmente garantizar que las performance del código que estamos desarrollando es buena. 



<br>
<br>


## DevOps

<br>


Tradicionalmente siempre ha habido 2 enemigos: el desarrollador que quiere impelementar nuevas funcionalidades, y por otro lado, los ingenieros de infraestructuras cuyo objetivo es que todo funcione. Por ello, apareció una metodología que se llama DevOps para que tanto el desarrollador como el ingeniero de infraestructura sepan de la parte que tiene que llevar a cabo el otro. Esto hizo que entrase la infraestructura como código, que consiste en que cada cambio que haga el ingeniero, tiene que documentarlo en un script que se pueda ejecutar en todos los entornos de desarrollo.


<br>
<br>



## DOCKER Y CONTAINERS

<br>


### Intro
<br>
Un contenedor es un paquete estándar de software y dependencias.


Docker es una manera de empaquetar nuestro software. Esto nos permite empaquetar nuestro desarrollo en el contenedor y utilizarlo en muchos ordenadores y siempre va a funcionar. Esto es gracias a que los container comparten la mayoría del sistema operativo. Los contenedroes solo funcionan en el sistema operativo del que forman parte, esto los hace mucho más ligeros que una máquina virtual. Esta es la mayor diferencia con una máquina virtual, ya que la máquina virtual si que tiene su propio Sistema Operativo. Con Docker Desktop, el programa nos está levantando una máquina virtual que nos permiete trabajar con un contenedor del Sistema Operativo que queramos. También es importante saber que un contenedor no es el sustituto de una máquina virtual. 

<br>

<img src="https://www.netapp.com/media/Screen-Shot-2018-03-20-at-9.24.09-AM_tcm19-56643.png" alt="Container vs Virtual Machine"/>

<br>

<br>


### Docker

<br>

Docker sirve para desarrollar, empaquetar y correr aplicaciones que hemos introducido dentro de los contenedores.



- El Docker Engine solo está disponible en Lunux y es el programa que se encarga de levantar los contenedores en dicho Sistema Operativo

- El Docker Desktop es el equivalente a Docker Engine para Windows.



Una imagen de un contenedor es inmutable, lo que puedo cambiar es la información del container. Una imagen de Docker es como un CD de instalación. La imagen se puede cargar tanto por nombre como por ID. Se pueden tanto hacer pull de Docker Hub, como pushearlas a Docker Hub.



Un Docker Container es una instancia ejecutada de una imagen Docker. Te da el mismo aislamiento del sistema operativo del ordenador que una máquina virtual. El container también añade capas de escritura a las capas de la imagen y trabaja sobre ellas. Es importante saber también que los contianers pueden hablar entre si igual que los diferentes procesos de un sistema. Todas las imágenes tienen un hash que es como el resumen de la imagen.


Cada vez que ejecuto el commando `docker run` creo un nuevo contenedor con un nuevo ID.

Con el comando `docker start` estoy levantando una imagen que hay en un contenedor ya creado.



Para meternos dentro de un contenedor hay que hacer `docker run -it <nombre>`   

<br>

**Background Containers**

Son contenedores que se ejecutan en el background para escuchar y recibir o mandar comandos a un servidor u otro tipo de aplicación


Con la opción `docker start -i <nombre>` sirve para ver el modo interactivo del contenedor, con lo que volveríamos a entrar en la visión del modo escucha.


Para borrar una imagen `docker rmi <nombre imagen>`.


Para que no secuestre la terminal con el modo escucha el comando es `docker run -d <nombre>`


Cuando yo hago docker run, yo puedo utilizar comandos que se ejecuten dentro del container. Ejemplo `docker run <image> ls -l` muestra el contenido de ficheros de Ubuntu y crea un container más. No obstante, al pasarle un comando el contenedor simplemente ejecutará eso y no me dejará meterme en el.


Para copiar archivos a los contenedores se ejecuta el comando `docker cp <source> <target>`




El comando para ver los recursos que está consumiendo cada contenedor ejecutamos `docker stats <id>`


El comando para ver los procesos que hay dentro del contenedor `docker top <id>`



<br>

<br>

**Volúmenes y puntos de montaje**

Cuando un contenedor crashea o se borra, todos los datos desaparecen. Para evitar esto, Docker tiene 2 opciones:

 1. Volumenes: los gestiona docker y no el sistema operativo

 2. Bind mounts: es como crear una carpeta dentro del ordenador. Son gestionados por el sistema operativo

Ambos tienen las siguientes características:

 - Permiten que la información se guarde cuando se destruya el contenedor.

 - Permiten compartir información con el host machine
 - Permiten compartir información con otros contenedores


<br>
<br>




**Docker Image Layers**

Las imágenes docker están hechas de varias capas read-only (las capas son los dowload que aparecen cuando hago un pull de una nueva imagen). Esto hace que si entre varias imágenes se comparten capas se pueden usar entre todas.

<br>

**Docker File**

Las Docker Files son los archivos que se utilizan para construir una imagen utilizando el comando `docker build <path>`. Un ejemplo sería:



``` docker

FROM ubuntu:18:04

RUN apt-get update
RUN apt-get install -y nginx


COPY entrypoint.sh /
COPY index.html /var/www/html/index.html

EXPOSE 80


ENTRYPOINT ["/entrypoint.sh"]

```

















