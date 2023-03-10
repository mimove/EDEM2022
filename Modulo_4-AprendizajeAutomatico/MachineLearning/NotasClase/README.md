# Introducción a Machine Learning

¿Qué es Machine Learning?

Machine Learning es un campo de la inteligencia artificial que le da a las computadoras la capacidad de aprender sin ser explícitamente programadas. 

Ejemplos:

- Netflix: recomendación de películas es un ejemplo de machine learning.

- Coche autónomo: el coche autónomo es un ejemplo de machine learning.


Hay tres ramas que  cubren machine learning:

- Computer Science: es la rama que se encarga de la teoría de machine learning.

- Business Knowledge: es la rama que se encarga de la aplicación de machine learning.

- Statistics and Maths: es la rama que se encarga de la estadística y la matemática de machine learning.

<br>

<br>



## Estructura proyecto ML

Paso previo - Plantear un problema o hipótesis a demostrar.

Paso 1 - Recopilar datos y limpiarlos. 

Paso 2 - Preparar los datos para el modelo.

Paso 3 - Entrenar el modelo.

Paso 4 - Evaluar el modelo.

Paso 5 - Optimizar el modelo.

Paso 6 - Presentar el modelo.

Paso 7 - Desplegar el modelo.

Paso 8 - Mantener el modelo.


<br>

<br>

## Ejemplo ML

Ejemplo de un problema de machine learning: 

### Train

Conjunto de imágenes de gatos y mujeres. A las imágenes de gatos se les etiqueta como 1 y a las imágenes de mujeres se les etiqueta como 0. 

### Test

Se prueba el modelo entrenado con nuevas imagenes en las que algunas son de gatos, otras de mujeres y otras de cosas que no son ni gatos ni mujeres, y se comprueba en cuales de las imágenes etiqueta correctamente y en cuales no. Si alguna de las imágenes se etiqueta como gato y no lo es se llama overfitting. 


<br>

<br>

## _Clase 10-03-2023_

<br>


## Cleaning vs preprocessing

Aunque compartan el mismo objetivo, cleaning y preprocessing son dos conceptos diferentes. 

### Cleaning

Cleaning es el proceso de limpiar los datos. 

### Preprocessing

Preprocessing es el proceso de preparar los datos para el modelo.

Diferencias:

- Cleaning: se hace antes de preprocessing.
  
- Preprocessing: se hace después de cleaning.

- Cleaning: se hace una vez.

- Preprocessing: se hace varias veces.

- Cleaning: se hace con el conjunto de datos completo.

- Preprocessing: se hace con el conjunto de datos de entrenamiento.


<br>

## Pasos del proceso de machine learning

<p align="center">
<img src="https://datos.gob.es/sites/default/files/u322/grafico.jpg" width=600px>
</p>



### Establecer el objetivo

El objetivo es la variable que queremos predecir. 

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, el objetivo es la variable diabetes.


### Selección de variables

Las variables son las características que se usan para predecir el objetivo. 

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, las variables son la edad, el sexo, el índice de masa corporal, la presión arterial, etc.


### Oversampling

Oversampling es el proceso de aumentar el número de muestras de la clase minoritaria.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, el oversampling consiste en aumentar el número de pacientes sin diabetes hasta tener 1000 pacientes sin diabetes.



### Undersampling

Undersampling es el proceso de reducir el número de muestras de la clase mayoritaria.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, el undersampling consiste en reducir el número de pacientes con diabetes hasta tener 100 pacientes con diabetes.


### Eliminar variables constantes

Eliminar variables constantes es el proceso de eliminar las variables que tienen el mismo valor para todas las muestras.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, y todas las muestras tienen el mismo valor para la variable sexo, se puede eliminar la variable sexo.


### Rellenar valores faltantes

Rellenar valores faltantes es el proceso de rellenar los valores faltantes de las variables.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, y algunas muestras tienen valores faltantes para la variable sexo, se puede rellenar esos valores faltantes con el valor más frecuente de la variable sexo.


### Agrupar categorías

Agrupar categorías es el proceso de agrupar las categorías de las variables categóricas.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, y la variable sexo tiene las categorías masculino y femenino, se puede agrupar las categorías en una sola categoría llamada sexo.

### Codificar variables categóricas

Codificar variables categóricas es el proceso de convertir las variables categóricas en variables numéricas.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, y la variable sexo tiene las categorías masculino y femenino, se puede codificar las categorías como 0 y 1.

### Escalar variables

Escalar variables es el proceso de transformar las variables numéricas para que todas ellas tengan el mismo rango de valores.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, y las variables edad y índice de masa corporal tienen rangos de valores muy diferentes, se puede escalar las variables para que todas ellas tengan el mismo rango de valores.

### Separar conjunto de datos en conjunto de entrenamiento y conjunto de prueba

Separar conjunto de datos en conjunto de entrenamiento y conjunto de prueba es el proceso de separar el conjunto de datos en dos conjuntos, uno para entrenar el modelo y otro para probarlo.

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, se puede separar el conjunto de datos en un conjunto de entrenamiento con 900 pacientes y un conjunto de prueba con 100 pacientes.



<br>

<br>

## Oversampling y undersampling

Un problema desbalanceado es aquel en el que las clases a predecir tienen ratios muy desiguales.  

Ejemplo:

- Si queremos predecir si un paciente tiene o no diabetes, y tenemos 1000 pacientes con diabetes y 100 pacientes sin diabetes, el problema es desbalanceado porque la clase con diabetes tiene 10 veces más muestras que la clase sin diabetes.


Los problemas desbalanceados suponen una problemática adicional para los modelos de ML porque los modelos tienden a predecir la clase mayoritaria.

Para disminuir el problema, muchas vece se recurre a una combinación de dos pasos:

- Undersampling: reducir el número de muestras de la clase mayoritaria. Puede ser aleatorio o estratificado.

- Oversampling: aumentar el número de muestras de la clase minoritaria. Puede ser aleatorio o estratificado. Puede ser SMOTE o ADASYN.




### SMOTE

SMOTE es una técnica de oversampling que consiste en generar muestras sintéticas de la clase minoritaria. Se emplea un algoritmo de clustering para generar muestras sintéticas de la clase minoritaria. Se usa cuando el dataset tiene datos estructurados

Algorigmo: 

- Seleccionar una muestra de la clase minoritaria.

- Elegir una de sus k vecinas más cercanas.

- Calcular los K vecinos más cercanos de la muestra elegida.

- Elegir aleatoriamente uno de los K vecinos.



## Eliminar variables No informadas

Eliminar variables No informadas es el proceso de eliminar las variables que tienen un porcentaje de valores faltantes superior a un umbral.

Los valores no informados pueden rellenarse de distintas formas. Sin embargo, si el porcentaje de missing values es muy alto, puede ser mejor opción eliminar la variable del dataset.

Es recomendable ser conservador, sobre todo en el caso de problemas desbalanceados. En estos casos, es mejor eliminar variables que rellenar valores faltantes.



## Rellenar missing values

Rellenar missing values es el proceso de rellenar los valores faltantes de las variables. La mayoría de los algoritmos de ML no pueden trabajar con valores faltantes, por lo que es necesario rellenarlos. La única excepción son los modelos de árboles de decisión, que pueden trabajar con valores faltantes.

Si después del data cleaning y de eliminar variables no informadas aún existen valores no informados, deben inferirse.

Existen distintas formas de rellenar los valores faltantes:

- Rellenar con el valor más frecuente de la variable.
- Rellenar con el valor medio de la variable.
- Rellenar con el valor mediano de la variable.
- Rellenar con el valor más cercano de la variable.
- Rellenar con el valor más cercano de la variable, pero solo si la distancia es menor a un umbral.


## One hot enconding

One hot enconding es el proceso de convertir las variables categóricas en variables numéricas. La mayoría de los algoritmos de ML no pueden trabajar con variables categóricas, por lo que es necesario convertirlas en variables numéricas.


