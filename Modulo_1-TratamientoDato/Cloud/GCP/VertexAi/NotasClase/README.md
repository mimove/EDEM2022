# Notas Clase VertexAI

## _Clase 21/01/2023_

<br>

Es una plataforma que reúne dos productos de GCP: AutoML y AI Platform. Además, nos proporciona herramientas que cubren todo el flujo de trabajo:

- Notebooks

- Datasets: Datos tabulados, imagenes/video, texto

- Models: mediante AutoML o AI Platform
- Deploy

<br>

## Auto ML

Es la capacidad de entrenar un amplio rango de modelos sin preocuparnos por los detalles. Para ello, tomará un dataset previamente creado en vertex AI y realizará múltiples entrenamientos (caja negra) y nos presetnará con un modelo ganador.

Este entrenamiento puede ser limitado a un número de horas (Budget, Maximum node hours) para limitar el costo económico. 

No necestica casi configuración. Solo hay que seleccionar el dataset, el objetivo, el peso y compute y el early stopping.

<br>

## Platform AI

Es la capacidad de entrenar un modelo de AI empleando nuestro propio código. Aquí podemos emplear cualquier herramienta que creamos conveniente para resolver la tarea.

Permite acceder a todo el resto de ventajas que proporciona Vertex AI.

Es bastante más complicado de emplear


<br>

## Notebooks

Plataforma de creación de notebooks (Jupyter Notebooks) dentro de Vertex AI. Esto permite ejecutar código Python con todas las librerías relacionadas con Vertex AI ya configuradas sin necesidad de realizar la configuracíon por nuestra parte.

Es muy similar a Google Colab.


<br>

## Datasets de datos tabulados

La primera línea del CSV ha de ser la cabecera, estos son los nombres de las columnas. 

Las columnas pueencontener caracteres alfanuméricos y la barra baja "_". 

Cada CSV no puede pasar de 10GB, si pesa más lo puedes repartir en varios CSV hasta un máximo de 100GB. 

El delimitador tiene que ser la coma ",".

Al menos hay que tener 1000 filas para Tabular Data, 100 imágenes por clase para Vision AI.

El CSV se sube con la varaible a predecir incluida.

No hace falta delimitar el schema del CSV, Vertex AI lo hace por ti. Se puede repartir los datos entre entrenamiento, validación y test de forma automática o manual.

<br>

## Model Metrics

- True Positive (TP)
- True Negative (TN)

- False Positive (FP)
- False Negative (FN)



$$\mathrm{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\mathrm{Precision} = \frac{TP}{TP + FP}$$

$$\mathrm{Recall} = \frac{TP}{TP + FN}$$

<br>

**F1 Score**

Es la media armónica de la precisión y el recall

$$F_1=\frac{2}{recall^{-1}+precision^{-1}}=2\frac{precision\cdot recall}{precision + recall}=\frac{2tp}{2tp + fp + fn}$$



<br>

**ROC AUC Curve**

El AUC es invariable respecto a la escala. Mide como de bien se clasifican las predicciones, en lugar de sus valores absolutos.

El AUC es invariable con respecto al umbral de clasificación. Mide la calidad de las predciiones del modelo, independientemente del umbral de clasifcación elegido.

$$TPR=\frac{TP}{P}=\frac{TP}{TP+FN}=1-FNR$$


Si la integral de la curva TPR (AUC) es 1, el clasificador es perfecto. Si es 0.5, el clasificador es aleatorio.


<br>

**Matriz de confusión**

Se trata de una tabla donde se indica la cantidad de prediccione de una clase frente a la clase verdadera.


<br>

**Intersection Over Union**

Esta es una métrica exclusivamente de visión por computador. Se trata de una métrica de similitud, por lo tanto, cuanto mayores es la cifra mayor similitud. Su valor esta acotado entre 0 y 1.

$$IOU = \frac{\mathrm{area\ of\ overlap}}{\mathrm{area\ of\ union}}$$

