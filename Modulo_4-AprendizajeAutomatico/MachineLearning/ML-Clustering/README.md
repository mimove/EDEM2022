# Notas clase Clustering

## _Clase 22_04_2023_

## K-Means

K-means es un algoritmo de clustering que se utiliza para agrupar un conjunto de datos numéricos/continuos en k grupos (clusters) distintos. 


Objetivo: Encontrar la mejor asignación de los datos a los diferentes grupos, donde los datos en cada grupo son similares entre sí, y los datos en diferentes grupos son diferentes.

Pasos K-means:

- El usuario especifica el número de grupos k que desea crear.
- El algoritmo selecciona aleatoriamente k puntos del conjunto de datos como centros iniciales de los grupos.
- Para cada punto de datos, se calcula la distancia euclidiana a cada uno de los centros del grupo. El punto de datos se asigna al grupo cuyo centro está más cerca de él.
- Se recalculan los centros de cada grupo tomando la media de todos los puntos de datos asignados a ese grupo.
- Se repiten los pasos 3 y 4 hasta que se alcance un criterio de parada, como un número máximo de iteraciones o una convergencia satisfactoria.
- El resultado final del algoritmo es un conjunto de k grupos, cada uno representado por su centroide (el punto promedio de todos los puntos de datos asignados a ese grupo). Los grupos resultantes son disjuntos y cada punto de datos pertenece a uno y solo uno de los grupos.


### Elbow method

Encontrar el número óptimo de clusters

El valor "codo" se obtiene en la gráfica de la suma de los cuadrados de las distancias intra-cluster (WCSS) en función del número de clusters.
El "codo" en la gráfica del Elbow Method es el punto en el que la disminución en WCSS se aplana significativamente. Agregar más clusters no resultará en una mejora significativa en la calidad del clustering.


N.B.: El valor óptimo de clusters puede variar dependiendo de los datos y de la aplicación en cuestión, por lo que es importante realizar pruebas y explorar diferentes valores para encontrar la mejor solución.

### Silhouette method

A diferencia del Elbow Method, que mide la calidad de los clusters en función de la distancia intra-cluster (WCSS), el silhouette method mide la calidad de los clusters en función de la similitud entre los puntos y los clusters vecinos más cercanos.

Se asigna a cada punto un valor de silueta, que es una medida de cuán bien se ajusta el punto a su cluster en comparación con los clusters vecinos más cercanos. 


Se usa para para datasets con gran dimensionalidad.

El coeficiente de silueta mide la proximidad entre un punto de un conglomerado y los puntos de los conglomerados vecinos, y oscila entre -1 y 1.


Puntuación:

<0: El punto está mal asignado a su cluster.
0: El punto está en la frontera entre dos clusters.
1: El punto está bien asignado a su cluster.




<br>

<br>


## K-Modes

Algoritmo de clustering para agrupar datos categóricos en grupos homogéneos. A diferencia de K-means, que es un algoritmo diseñado para datos numéricos continuos, K-modes se utiliza para datos categóricos o discretos.


### ¿Por qué categóricos?

A diferencia de los datos numéricos continuos, los datos categóricos no tienen una medida natural de distancia euclidiana. Por lo tanto, se requiere una medida de disimilitud que sea adecuada para datos categóricos.

En K-modes, la medida de disimilitud utilizada se basa en la frecuencia de coincidencia de las categorías entre diferentes instancias. La idea es que dos instancias son más similares si comparten más categorías. 

Ej: Si dos personas compran un mismo producto en una fecha determinada, y otro producto igual en otra fecha determinada, podemos decir que ambos tienen similitudes.

K-modes utiliza un enfoque de asignación basado en modas (modes), que es diferente al enfoque de asignación basado en centroides utilizado por K-means. En lugar de utilizar la media de los valores de las características, K-modes utiliza la moda de las categorías para cada grupo, lo que lo hace adecuado para trabajar con datos categóricos.

La distancia euclidiana no es adecuada para medir la similitud entre dos instancias que contienen datos categóricos, ya que no se puede establecer una distancia como tal. En su lugar, K-modes utiliza una medida de distancia específica para datos categóricos llamada distancia de Hamming, que se define como el número de características en las que dos instancias difieren.

Pasos K-mode:

- Inicialización: Se seleccionan k centroides al azar entre las muestras categóricas de entrada.

- Asignación: Cada muestra se asigna al centroide más cercano (en términos de la distancia de Hamming, que mide la diferencia entre las características categóricas). Esto crea k grupos iniciales.

- Actualización: Se actualizan los centroides de cada grupo para que coincidan con la moda (el valor más común) de cada característica dentro del grupo.

- Repetición: Se repiten los pasos 2 y 3 hasta que no haya cambios en la asignación de las muestras a los centroides.

- Resultado: El resultado final es un conjunto de k grupos, cada uno representado por su centroide (es decir, la moda de cada característica dentro del grupo).

### Métodos de inicialización


- Iniciación aleatoria: El utilizado en k-means y el que se utilizaba en k-modes.
  
- Método Huang: Selección de centroides basada en la frecuencia. Es más rápido
  
- Método Cao: Selección de centroides basada en la densidad y busca seleccionar centroides que estén lo más alejados posible entre sí. Es más estable y coherente que el método Huang.


### Elbow method

En K-modes también se utilizan el Elbow y Silhouette Method.
Lo único que cambia es que se utiliza una función de coste en vez de WCSS/SSE.




<br>

<br>



## K-Prototypes

K-prototypes combina la distancia euclidiana para las variables numéricas y la distancia de coincidencia o Hamming para las variables categóricas. Utiliza el mismo proceso que KMEANS y KMODES. 

K-prototypes es ampliamente utilizado en aplicaciones comerciales, como el análisis de datos de clientes, el análisis de segmentación de mercado y la detección de fraude en las transacciones financieras.


- Datos numéricos y categóricos
- Sigue el mismo proceso que k-means
- Utiliza ambasa la media (numéricos) y la moda (categóricos)
- La distancia se mide con la matriz gamma (i.e. combinación)
- Elbow method (función de coste)
- Silhouette method
- Computacionalmente intensivo


<br>

<br>


## DBSCAN

El Density-Based Spatial Cluestring of Applications with Noise (DBSCAN) es un algoritmo basado en densidad, lo que significa que agrupa puntos de datos en función de su proximidad y densidad.


Es capaz de manejar datos en forma de vectores de características, donde cada característica puede ser numérica o categórica. Por lo tanto, se puede aplicar a una variedad de tipos de datos, como datos de imágenes, datos de texto y datos de series temporales.

Además, el algoritmo DBSCAN es particularmente útil para datos con estructuras de alta dimensionalidad y datos no lineales, ya que puede detectar agrupaciones en formas complejas en lugar de simplemente encontrar agrupaciones convexas.


A diferencia de la familia "k", no requiere especificar el número de clusters. 

Los clusters se definen a través de 2 parámetros principales: 
- Epsilon (eps): 
    La distancia máxima permitida entre dos puntos para que se consideren vecinos y se incluyan en el mismo cluster. Controla el tamaño del vecindario alrededor de cada punto. 

    Grande → Inclusión de puntos que no pertenecen al mismo cluster.
    Pequeño → Clusters separados en subgrupos más pequeños.


- Puntos mínimos (min_samples):
    Número mínimo de puntos que deben estar dentro de la distancia Eps para que se forme un cluster. Este parámetro controla la densidad requerida para que un grupo de puntos se considere un cluster. 

    Grande → Puede hacer que algunos clusters no se identifiquen.
    Pequeño → Puede resultar en la identificación de clusters con ruido.



DBSCAN tiene varias ventajas sobre otros algoritmos de clustering, como su capacidad para manejar clusters de formas y tamaños variables, y su capacidad para identificar outliers. También es relativamente simple de implementar y eficiente computacionalmente.

Pasos:

- Definición de parámetros: eps (epsilon) y min_samples (puntos mínimos). 

- Clasificación de puntos: Cada se clasifica como 'núcleo', 'borde' o 'ruido'.

- Expansión de clusters: El algoritmo comienza seleccionando un punto 'núcleo' aleatorio. A continuación, encuentra todos los puntos 'núcleo' densamente conectados y los asigna al mismo cluster. Este proceso se repite hasta que todos los puntos 'núcleo' han sido asignados a un cluster.

- Asignación de puntos 'borde': Los puntos 'borde' se asignan a los clusters correspondientes en función de su vecindad a los puntos 'núcleo'. Los puntos 'ruido' se dejan sin asignar.

DBSCAN es robusto frente a ruido y puede identificar clusters de diferentes densidades y formas arbitrarias. Sin embargo, es sensible a la elección de los parámetros eps y min_samples.

### FINE-TUNING & DISTANCIAS 

A la hora de medir las distancias, cada método es apropiado para según qué datos.

Datos numéricos:

- Distancia euclidiana
- Distancia de Manhattan
- Distancia coseno


Datos categóricos:

- Distancia de Hamming
- Distancia de Jaccard


**DISTANCIAS NUMÉRICAS**

euclidiana: Es la medida de distancia máss común y predeterminada en la mayoría de los algoritmos de clustering. Tiene en cuenta la geometría del espacio de características.

Manhattan (o L1): Especialmente en espacios de alta dimensionalidad. La distancia de Manhattan es útil cuando se quiere dar más importancia a diferencias más grandes en una sola dimensión en lugar de diferencias acumuladas en múltiples dimensiones.

Coseno: Es una medida de distancia popular en análisis de texto y espacios de alta dimensionalidad. La distancia de coseno se basa en el ángulo entre dos vectores en lugar de su magnitud, lo que permite comparar la dirección de los vectores en lugar de su longitud.


**DISTANCIAS CATEGÓRICAS**

hamming: La distancia de Hamming es una medida que compara dos puntos en función de la cantidad de coordenadas que difieren. Es adecuada para datos categóricos o binarios y es especialmente útil cuando se trabaja con datos codificados, como secuencias de ADN.

Jaccard: La distancia de Jaccard compara dos puntos en función de la cantidad de características que comparten en relación con la cantidad total de características que tienen en conjunto. Es adecuada para datos categóricos, especialmente cuando se trabaja con conjuntos de datos dispersos o datos binarios de alta dimensionalidad, como datos de presencia/ausencia o datos de transacciones.



### Nearest Neighbours

Se encarga de encontrar los k vecinos más cercanos de cada punto en un conjunto de datos.

- Primero, aprende de la estructura de datos. Se puede ajustar el algoritmo utilizado en el parámetro “algorithm=”:
    - “brute”: Por fuerza bruta, muy intensivo, no recomendable.
    - “kd-tree”: Eficiente para baja/moderada dimensionalidad.
    - “ball-tree”: Eficiente para alta dimensionalidad y para categóricos.
    - “auto”: Detecta el algoritmo más apropiado → el default


NOPE → No es necesario que n_neighbors = min_samples → n_neighbors >= min_samples

El parámetro min_samples en DBSCAN especifica el número mínimo de puntos requeridos en la vecindad de un punto para que se considere un punto central. Este valor influye directamente en cómo se forman los clusters en DBSCAN y ayuda a controlar el ruido en el resultado del clustering.

Representa el valor de k (número de vecinos más cercanos a considerar) para calcular las distancias promedio. 

Generalmente, se elige un valor de n_neighbors que sea lo suficientemente grande como para capturar la estructura de densidad local de los datos, pero no demasiado grande como para incluir puntos de otros clusters.


<br>

<br>

## Gaussian Mixture Models

### Tipos de modelos

**Centroid based models**

En estos modelos, si un punto pertenece a un cluster depende de la distancia con el centroide, no con otro punto individual.

Se selecciona un número de clusters k y se inicializan k centroides de manera aleatoria. Luego, se asigna cada punto de datos al centroide más cercano y se recalculan los centroides en función de los puntos asignados a cada cluster. 

→ K-MEANS


**Density based models**

Un punto pertenece a un cluster si entra en el área de densidad de ese cluster.

Los clusters se forman a partir de regiones densas de puntos de datos separadas por regiones de baja densidad. Los puntos de datos que se encuentran en regiones de alta densidad se consideran parte del mismo cluster, mientras que aquellos que se encuentran en regiones de baja densidad se consideran outliers.

→ DBSCAN


**Distribution based models**

Se asume que los datos se distribuyen según alguna distribución probabilística, como la distribución gaussiana. 

→ Gaussian Mixture

<br>

Un modelo de mezcla gaussiana es una combinación de varios modelos gaussianos simples, donde cada modelo gaussiano representa uno de los clusters en los datos. El modelo se entrena para ajustar las distribuciones gaussianas a los datos y determinar la cantidad y los parámetros de cada modelo gaussiano que mejor se ajusten a los datos.

GMM puede identificar clusters de diferentes formas y tamaños en función de los parámetros de distribución aprendidos del conjunto de datos. Por eso, GMM se utiliza a menudo para problemas de clustering donde la distribución de los datos es desconocida.

GMM también se utiliza a menudo en problemas de modelado generativo, donde el objetivo es aprender una distribución de probabilidad sobre los datos de entrada para poder generar nuevos datos que se parezcan a los originales.


Pasos:

- Inicialización: Seleccionamos el número de clusters 'K' y se asignan aleatoriamente parámetros iniciales a cada uno, incluyendo la media, la varianza y los pesos (proporciones) de las distribuciones gaussianas.

- Expectation-Maximization (EM): El algoritmo EM es un proceso iterativo que consiste en dos pasos: el paso de Expectation (E) y el paso de Maximization (M).

    - a) Paso de Expectation (E): Calcular la probabilidad de que cada punto de datos pertenezca a cada uno de los 'K' clusters. Estas probabilidades se conocen como "responsabilidades".
    - b) Paso de Maximization (M): Actualizar los parámetros de las distribuciones gaussianas (media, varianza y pesos) utilizando las responsabilidades calculadas en el paso E. La idea es maximizar la probabilidad de que los datos observados hayan sido generados por la mezcla de distribuciones gaussianas.

- Convergencia: Repetir los pasos E y M hasta que los parámetros de las distribuciones gaussianas converjan.


### Performance

En GMM no se utiliza el Elbow Method. Se utilizan BIC (Criterio de Información Bayesiana) y AIC (Criterio de Información de Akaike).

Goodness: Cuán bien un modelo describe los datos.

Model Complexity: Número de parámetros o variables que utiliza el modelo. 

→ Un modelo más complejo podría ajustarse mejor a los datos, pero también podría ser más propenso al sobreajuste y tener un rendimiento deficiente en datos nuevos.
→ BIC penaliza modelos más complejos de manera más estricta que AIC.





