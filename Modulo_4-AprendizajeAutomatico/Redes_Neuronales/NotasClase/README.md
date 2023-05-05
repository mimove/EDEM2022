# Notas Clases Redes Neuronales

## _Clase 05/05/2023_

# Fundamentos

## Introducción

### RRNN

Objetivo: Entender el funcionamiento de las redes nueronales totalmente conectadas.

#### RRNN Biológicas

Las neuronas son células que se comunican entre sí a través de señales eléctricas y químicas. 

Las nuronas reciben señales a través de las dendritas y las envían a través de los axones, en caso de que se activen.

Las nuronas dan más importancia a unas señales de entrada que a otras para activarse.

#### RRNN Artificiales


Las neuronas artificiales imital las entradas y salidas con uan función que recibe una serie de entradas numéricas ponderadas y se activa si la suma de las mismas supera un cierto umbral.

Esta simplifiación del funcionamiento de las nueronas biológicas no tienen en cuenta la creación odestrucción de nuevas conexiones entre neuronas, pero ha demostrado ser muy útil en diversos ámbitos. 



Una neurona es una unidad de computación simple, cuya función es procesar información de entrada para reaccionar en consecuencia produciendo una salida. Entrada valor numérico 'x' y salida valor numérico 'y'.

<p align="center">
<img src="https://dcain.etsin.upm.es/~carlos/bookAA/_images/McCulloch-Pitts.png" width=500px>
</p>


La funcion de activacion determina como reacciona una neurona a una entrada determinada. La función de activación en las redes neuronales es definida por el desarrollador


<p align="center">
<img src="funciones.png">
</p>


Una red neuronal es un grafo de cálculo que combina diversas neuronas con múltiples variables de entrada.

Las variables de entrada y las neuronas se relacionan entre sí a través de conexiones, las cuales tienen asociados unos pesos.

Los pesos ponderan en que medida medida los extremos de las conexiones se relacionan entre si.

La capa de entrada está formada por las variables de entrada a la red neuronal. Puede ser cualquier tipo de valor numérico. Ejemplos:

- Píxeles de una imagen
- Caracerísticas de un producto
- Parámetros del funcionamiento de una línea de producción



Las capas oculatas de la red son aquellas que se encuentran entre la capa de entrada y la capa de salida. habitualmente están formadas por cientos o miles de neuronas.

Entrada: variables de entrada/Activaciones de otras capas oculatas, ponderadas por los pesos.

Salida: activaciones de las neuronas de la capa f(entrada)

Principales parámetros: Función de activación y número de neuronas.

<p align="center">
<img src="red_simple.png">
</p>

La capa de salida es la última capa de la red neurona. Funciona de la misma forma que las capas ocultas. Pero tiene 2 diferencias de diseño principales:

la función de activación que se elige

Número de neuronas, directamente ligado al problema al que se van a aplicar.




Funciones de activación más comunes en la capa de salida:

Problemas de regresión: 
- Función de salida Lineal. 
- Número neuronas en la capa de salida = Número de parámetros a estimar

Problemas de clasificación: 
- Función de salida:  Softmax
- Número de neuronas = número de clases

<br>

## Aprendizaje

Para que una red neuronal aprenda una determiada tarea se requiere de muestras etiquetadas.

El orden de muestras necesarias puede variar entre cientos y millones dependiendo de la complejidad del problema.



<p align="center">
<img src="imagenes_etiquetadas.png">
</p>



El aprendizaje de una red neuronal consiste en actualizar sus pesos de tal manera que se minimice el error que se produce al analizar los datos de entrenamiento para una tarea detemrinada.



Las funciones de périddas nos permiten evaluar el grado de efectividad de una red neuronal en una tarea concreta.

Cada tipo de tarea require de una función de périda distina.

El aprencizaje de las redes nueronales es un problema de otpimización. el objetivo es encontrar el conjunot de pesos W que minimice la función de pérdidas de la red neuronal para el conjunot de datos de entrenamiento.

Probelmas de Regresión:
Error cuadrático medio

$$MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y_i})^2$$


Problemas de Clasificación:
Entrópia cruzada

$$H_y'(y) := - \sum_{i} (y_i' \log(y_i) + (1-y')\log(1-y_i)$$


El descenso por gradiente es un método iterativo que permite encontrar el mímino de una función con respecto a sus variables utilizando derivadas parciales.

La intensidad de la actualización de los pesos está regulada por la Tasa de Aprendizaje ($\alpha$). Este parametro es fijado por el desarrollador.


<p align="center">
<img src="des_grad.png">
</p>


El algoritmo que permite entrenar las redes neuronales se denomina Retro-Propagación. El algoritmo comigna el Descenso por Gradiente con la regla de la cadena para calcular las derivadas parciales de la función de pérdidas con respecto a los pesos de la red neuronal.

<p align="center">
<img src="retro_prop.png">
</p>


El aprendizaje de una red neuronales es un proceso iterativo en el que se realizan las prediccioones sobre las muestras de entrenamiento y se ajustan los pesos en base a una fucnión de coste que pdepende de la veracidad de las predicciones.

Al proceso de predicción del conjunto de datos de entrenamiento y posterior actualización de los pesos se le denomina epoch.

El número de epochs de entrenamiento es un parámetro que debe ser fijado por el desarrollador.

Es recomendable el entrenamiento de RRNN en GPU en lugar de CPU. El número de muestras de entrenamiento que cuyo análisis se paraleliza simultáneamente se denomina tamaño de batch. El tamaño de batch es definido por el desarrollador en función del hardware del que dispone.



## Resumen clave

Parámetros que se tienen que elegir y ajustar durante el diseño de redes neuronales totalmente conectadas.

- Número de capas ocultas
- Número de neuronas por capa
- Función de activación
- Función de pérdidas
- Tasa de aprendizaje
- Número de epochs
- Tamaño de batch
