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

## _Clase 01-04-2021_




