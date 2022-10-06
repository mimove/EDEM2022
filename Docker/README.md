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



## DOCKER

<br>

Un contenedor es un paquete estándar de software y dependencias.


Docker es una manera de empaquetar nuestro software. Esto nos permite empaquetar nuestro desarrollo en el contenedor y utilizarlo en muchos ordenadores y siempre va a funcionar. Esto es gracias a que los container comparten la mayoría del sistema operativo. Los contenedroes solo funcionan en el sistema operativo del que forman parte, esto los hace mucho más ligeros que una máquina virtual. Esta es la mayor diferencia con una máquina virtual, ya que la máquina virtual si que tiene su propio Sistema Operativo. Con Docker Desktop, el programa nos está levantando una máquina virtual que nos permiete trabajar con un contenedor del Sistema Operativo que queramos. También es importante saber que un contenedor no es el sustituto de una máquina virtual. 







