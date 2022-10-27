# NOTAS CLASE MODULO APLICACIÓN A NEGOCIO

## _Clase 27/10/2022_


## Analítica aplicada al negocio

La manera en la que hacemos negocios ha cambiado por completo. Hasta hace 10 años, la manera de ahcer engocio era muy enfocado a mi información propia. Es decir, yo conocía mis clientes, productos, etc. Pero no conocía especificamente el comportamiento de mis clientes y por qué me compraban a mi y no a la competencia. Esto ha hecho crear la sensación de que el dato es el "nuevo petróleo". No obstante, el dato per se no vale, hay que cultivarlo para poder sacar información valiosa. Es como el pan, tú necesitas cereal (dato en crudo) para hacer el pan, pero al final te comes el pan (dato cultivado). 

<br>

### **Framework de madurez analítica**

<p align="center">
<img src="https://imply.io/wp-content/uploads/blogs/1619638099-screen-shot-2021-04-28-at-3-27-54-pm.png">
</p>


La mayoría de empresas piensan que están mucho más arriba en el nivel de madurez de lo que realmente están. En la mayoría de los casos, las empresas usan una anlítica básica (nivel 1).


Al movernos más hacia la analítica avanzada, lo que queremos es poder anticiparnos a lo que va a ocurrir (flujo de caja, rotura de stock, etc.). Antes de empezar a trabajar con la analítica avanzada, hay que pensar donde está la compañía. Hay que contarle a los clientes un viaje, desde donde estamos a donde vamos, comunicarle lo importante de cultivar la analítica. Siempre hay que gestionar las expectativas de nuestros clientes previamente a meternos en cualquier proyecto. Las empresas más tradicionales tienen una cultura que hace más difícil implementar el cambio en el modelo de gestión de sus datos. Les cuesta más entender el valor que les aportan los datos.


La información más básica de la compañía, se suele cargar 1 vez al día, a la semana o al mes. Pero la información de IoT tengo que estar enviándola en tiempo real. Esto hace plantearse preguntas como si debemos almacenar la información en el mismo Data Lake o distintos. El problema viene porque hay diferentes áreas de una compañia que se tienen que regir por diferentes reglas o metodologías. Estos Data Lakes están empezando a migrar de on premise a las nubes más conocidas (AWS, Google, etc.), las cuales funcionan con programación distribuida (servidores que replican la información y están repartidos por todo el mundo). La ventaja del almacenamiento en la nube es que el escalado es muy barato y la capacidad de ir incrementándolo es muy sencilla. No obstante, a muy gran escala el almacenamiento 100% cloud sigue siendo muy caro, por lo que las compañías hacen un híbrido entre cloud y on premises. 

Siempre hay que tener en cuenta los KPIs que quieren conocer los directivos de la empresa para la que trabajemos, y centrarnos sólo en entregar los datos relacionados con dichos KPIs. 


Tableu y PowerBI son los 2 programas principales que se utilizan para la visualización de la analítica de datos en la actualidad. Tableu es una herramienta que hace gráficos muy buenos, pero tiene una curva de aprendizaje muy lenta. Por el contrario, PowerBI se ha apalancado en la funcionalidad y la extensión que tiene el Excel. No es una herramienta tan buena como Tableu, pero es muy sencilla de utilizar. 

<br>

### **Proveedores de programas de Analítica de Datos**

<p align="center">
<img src="https://www.cxtoday.com/wp-content/uploads/2022/03/gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms-2022.png" width=400px>
</p>



Al hacer análisis estadístico, es importante hacer un estudio previo de las variables que necesitamos introducir en el algoritmo. Dichas variables, se pueden obtener de programas que analizan la importancia de cada variables en el algoritmo (llamados PCA Principal Component Algorithms), y te identifica las que son más importantes. Hay que tener mucho cuidado con la información.


<br>

## Casos de uso:


### **GeoMarketing**

Existen 2 clases de variables para la analítica de datos:

- **Exógenas (externas)**: incluye los puntos de venta de los competidores, datos económicos y urbanos, datos socio-demográficos, haitos de consumo, puntos de interes (si hay carreteras, parques, cines, etc.). 

- **Endógenas (internas)**: incluyen puntos de venta, definicion de público objetivo, información de venta, datos del cliente y redes de influencia.

Tenemos que conseguir luego atractores de geolocalización para conseguir atraer clientes. Para ello se utilizan modelos graviatacionales que ayudan a realizar el trabajo anaítcilo uniendo tanto las variables internas como externas. Por último, en GeoMarketing se utiliza la geolocalización para ayudar a identificar nuevas áreas para la ubicación de nuestro negocio.


Algunos ejemplos de fuentes de datos externas en GeoMarketing son el INE (datos un poco antiguos), AEMET (influye mucho para un montón de negocios), datos del gobierno o de la oficina del catastro.


<br>

### **Optimización de portfolio**

Empresa que está monopolizando el mercado a través de la adquisición de competidores. Debido a ello (querer abarcar todo el mercado) tienen un problema de eficiencia en el almacenamiento de stock (muy pocas unidades por referencia). Esto hace que sus costes de producción y almacenamiento sean muy altos. El problema a resolver, por tanto, es como optimizar el stock. 

Para empezar a resolver este problema hay que hacer muchas preguntas diferentes para poder sacar información y llegar a conclusiones (¿por qué no subes el precio?, ¿por qué no aumentas tus zonas de venta?, etc.). Una vez que se tiene información y se detecta el problema (en este caso que había muchas referencias con pocas unidades) hay que estudiar las posibles soluciones. En este caso concreto, ahora hay que estudiar que referencias de nuestro stock nos podemos quitar en base a datos financieros de la empresa. Dichos datos dieron información de los productos de los que se obtenía mayor beneficio y se pudo estudiar cuáles se podrían retirar.
