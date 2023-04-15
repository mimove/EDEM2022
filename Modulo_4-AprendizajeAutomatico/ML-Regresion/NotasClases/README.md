# Notas Clase ML-Regresion 

## _Clase 31-03-2023_

## ¿Qué es la regresión en el contexto de ML?

Técnica aprendizaje supervisado para predecir a partir de un histórico. Las aplicaciones incluyen: predicción de precios, predecir si un correo es spam.

Relación x->y para predecir valores futuros.


## Usos de la regresión lineal

* Predicción de valores
* Relación entre variables del modelo
* Importancia de las características del modelo



## Flujo de funcionamiento

1. Tenemos el training data
2. Extraemos las variables que nos interesan
3. Usamos el modelo para predecir
4. Retroalimentamos el modelo con los datos reales
5. Vemos si el modelo se ajusta a los datos reales


El valor real se conoce como $y$, y el valor predicho se conoce como $\hat{y}$

## Modelo simple de regresión lineal

### Terminología

* $x$ característica. Covariable, variable independiente o variable predictoria
* $y$ observación, respuesta o variable dependiente.
* $w_0$ parámetro. Constante o punto de corte eje $y$ y cuando $x=0$. Coeficiente de intercpetación.
* $w_1$ Parámetro. Pendiente

$$f(x) = w_0 + w_1x$$

### Suma de los cuadrados de los residuos

$$\mathrm{RSS} = \sum_{i=1}^{n}(y_i - \hat{y_i})^2$$

<p align="center">
<img src="https://cdn.wallstreetmojo.com/wp-content/uploads/2022/05/Residual-sum-of-squares.jpg" width=400px>
</p>


## Hallar máximos y mínimos analíticamente

Una función cóncava se curva hacia abajo, mientras que una fución convexa lo hace hacia arriba.



## Hallar Maximos y mínimos con gradientes vía "Hill Climbing"

### ¿Qué es el gradiente?

El gradiente es un vector que indica la dirección de mayor crecimiento de una función. En el caso de la regresión lineal, el gradiente indica la dirección de mayor crecimiento de la función de pérdida.

### ¿Qué es el gradiente descendente?

El gradiente descendente es un algoritmo que se utiliza para encontrar los mínimos de una función. En el caso de la regresión lineal, el gradiente descendente se utiliza para encontrar los mínimos de la función de pérdida.

### ¿Cómo funciona el gradiente descendente?

El gradiente descendente se basa en la idea de que si se comienza en un punto y se sigue la dirección del gradiente, se llegará a un mínimo local. El gradiente descendente se basa en la idea de que si se comienza en un punto y se sigue la dirección del gradiente, se llegará a un mínimo local.

### ¿Cómo se calcula el gradiente?

El gradiente se calcula como la derivada parcial de la función con respecto a cada uno de los parámetros. En el caso de la regresión lineal, el gradiente se calcula como la derivada parcial de la función de pérdida con respecto a cada uno de los parámetros.

$$\frac{\partial}{\partial w_0}RSS(w_0, w_1) = \sum_{i=1}^{n} -2(y_i - w_0 - w_1x_i)$$

### Step size

El step size es el tamaño del paso que se da en la dirección del gradiente. El step size es el tamaño del paso que se da en la dirección del gradiente.

### ¿Cómo se actualizan los parámetros?

Los parámetros se actualizan de la siguiente manera:

$$w_0 = w_0 - \alpha \frac{\partial}{\partial w_0}RSS(w_0, w_1)$$

$$w_1 = w_1 - \alpha \frac{\partial}{\partial w_1}RSS(w_0, w_1)$$

### ¿Cómo se elige el step size?

El step size se elige de forma manual. Para elegir el step size, se puede probar con diferentes valores y ver cuál funciona mejor. 

Se puede usar el método de la bisectriz para encontrar el step size óptimo.

### Método de la bisectriz

El método de la bisectriz es un método para encontrar el mínimo de una función. El método de la bisectriz es un método para encontrar el mínimo de una función.

### ¿Cómo funciona el método de la bisectriz?

El método de la bisectriz se basa en la idea de que si se comienza en un punto y se sigue la dirección del gradiente, se llegará a un mínimo local. El método de la bisectriz se basa en la idea de que si se comienza en un punto y se sigue la dirección del gradiente, se llegará a un mínimo local.


<br>

## Múltiples dimensiones: gradientes

$$\nabla g(w) = \begin{bmatrix} \frac{\partial g}{\partial w_1} \\ \frac{\partial g}{\partial w_2} \\ \vdots \\ \frac{\partial g}{\partial w_n} \end{bmatrix}$$

Este vector tiene $p + 1$ componentes, donde $p$ es el número de parámetros.



<br>

<br>

## _Clase 14-04-2021_


## Técnicas de Dimensionality Reduction

### La maldición de la dimensionalidad

- Dimensionalidad es el número de características de un modelo.

- High dimensional data: Cuando el número de características p es mayor que el número de observaciones N.

La maldición de la dimensionalidad se refiere a los problemas que surgen cuando se trabaja con datos de alta dimensionalidad.


Cómo intepreta el algoritmo esto. En ML tendemos a añadir el mayor número de caracterísicas. A medida que añadimos características, el modelo empeora en cierto punto. Se tiende por tanto al overfitting. A medida que crece el número de características/dimensiones, crece exponencialmente la cantidad de datos que necestiamos para genralizar con precisión.



### Problemas al aumentar la dimensión


Busca encontar el punto más cercano dado un putno objetivo. A medida que aumentan las dimensiones en el df, aumenta la complejidad. Baja dimensionalidad es fácil de resolver. Complejidad aumenta a medida que aumentamos las dimensiones. Problema común en datos de expresión génica. 


### Matrices dispersas

Las características dispersas se denominan así porque tienen muy pocos valores distintos de cero.

Características densas tienen muchos valores distintos de cero.

Puede tender a overfitting

### Complejidad computacional

Los algoritmos requiren tiempo y recursos computacionales en espacios de alta dimensionalidad. Las características densas tienen muchos valores distintos de cero.


### Sesgos de la muestra

Pasa cuando las muestras de datos no son representativas. La muestra puede estar sobrerrepresentada o infrarepresentada. Afecta a la inferencia estadística y la extracción de conclusiones

### Cuántas características tienen que tener un modelo

- Menor número de variables: Fácil de interpretar, menos probable el 'overfitting' menor precisión al predecir.
- Mayor número de variables: Más difícil de interpretar, mayor tendencia al overfitting, mayor precisión al predecir.



<br>

<br>


------------


## Métodos de filtro

Funcionan como parte del procesamiento de datos. La selección de variables es independiente de los modelos de ML. Clasifican las variables en función de la correlación que tienen con la variable de salida. Se utilizan criterios univariados.

<br>

### Chi cuadrado ($\chi^2$)

La prueba chi-cuadrado evalúa si dos variables categóricas están relacionadas de forma significativa. Utiliza tablas de contingencia. Copara la frecuencia osbervada con la frecuencia esperado. El resultado se compara con un valor cr´tico en una tabla de distribución de chi cuadrado.


Fórmula:

$$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$

Donde:

- $O_i$: Frecuencia observada
- $E_i$: Frecuencia esperada
  
- $k$: Número de categorías




### Ventajas y desventajas

- Ventajas:
  - Reducción del tiempo de procesamiento y almacenamiento.
  - Mejora de la interpretación de los datos.
  - Reducción del Overfitting

- Desventajas:
  - Analizan las variables de forma independiente.
  - No se tienen en cuenta las interacciones entre las variables.
  


<br>

<br>
------------



## t-SNE

Es una técnica para visualizar datos de alta dimensión con FE, mediante observaciones que son más diferentes en un espacio de altas dimensiones. Debido a esto, las ovservaciones que son similares estarán más cercanas entre sí y pueden agruparse. no funciona con variables categóricas. No es un método de filtro. Capatura relaciones no lineales entre variables.

1) Se mide la similaridad para cada par de puntos. La similaridad se define como la probabilidad que un punto $x_i$ elija a un punto $x_j$ como su vecino más cercano, dado que $x_i$ y $x_j$ son vecinos en el espacio de altas dimensiones.

2) Convierte esa distancia de similaridad en probabilidad, siguiendo una distribución Gaussiana centrada en $x_i$.

3) Se calcula la matriz de similaridad para todos los puntos del dataset.

4) t-SNE proyectan todos los puntos al azar en una dimensión inferior.
5) Hacemos los mismo cálculas para estos puntos en una dimensión menor calculando la similaridad, pero esta vez utilizando una distribución t-student centrada en $y_i$.
6) Calculamos la matriz de similaridad de los puntos.
7) t-SNE compara S1 y S2 e intenta que las diferencias entre estas se mucho más pequeña
8) Al final tendremos puntos de datos de menor dimensión que intentan capturar incluso relaciones complejas en las que el PCA falla.


<br>

<br>

--------------------


## Wrapping methods

En estos métodos se utilizan un subconjunto de varialbes para determinar la capacidad predictiva. Se añaden o eliminan características a este subconjunto. Son computacionalmente costosos. Se puede definir como un problema de búsqueda.


Se puede ver como un problema de búsqeuda en el espacio de estados (State Space Search). La selección puede ser representada como un array binario: 1 si la característica es seleccionada y 0 si no lo es. En total habrá un conjunto de $2^p$ posibles subconjutos donde p es el número de características.



### Forward Selection

Empieza con un conjunto vacío de características (Reduced set). La mejor variable de las restantes se añade a este Reduced Set. En cada iteración posterior, la mejor de las variables sobrantes se añade a este subconjutno hasta que la adición de una nueva variable no mejore el rendimiento del modelo.

### Backward Elimination

Comienza con todas las varaibes e, iterativamente, se elimina la menos importante, lo cual se define como la que menos contribuye al rendimiento del modelo. Se repite el proceso hasta que la eliminación de una variable no mejore el rendimiento del modelo.


### Bidirectional Elimination

Se combina Forward Selection y Backward Elimination. Se empieza con un conjunto vacío de características (Reduced set). La mejor variable de las restantes se añade a este Reduced Set. En cada iteración posterior, la mejor de las variables sobrantes se añade a este subconjutno hasta que la adición de una nueva variable no mejore el rendimiento del modelo. Se repite el proceso hasta que la eliminación de una variable no mejore el rendimiento del modelo.


### Random generation

Se generan aleatoriamente subconjuntos de características y se evalúa el rendimiento del modelo. Se repite el proceso un número determinado de veces y se selecciona el subconjunto que mejor rendimiento tenga.


### Score comparison

Es el método que más recursos consume. Selecciona una variable que ajuste bien al modelo. A partir de esta, construye todos los posibles modelos ($2^{n-1}$ combinaciones posibles donde n es el número de variables)  y selecciona el que mejor puntuación obtenga junto a la primera variable. Se repite el proceso hasta que no se mejore el rendimiento del modelo.


### Ventajas y desventajas

- Ventajas
  - Los resultados suelen ser mejores respecto alos Filter
  - Interacción entre los subconjuntos de variables
  - Mantienen las dependencias entre variables

- Desventajas
  - Computacionalmente costosos
  - Riesgo de overfitting
  - Dependientes del training set