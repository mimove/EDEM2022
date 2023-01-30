import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

"""## The Auto MPG dataset

The dataset is available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/).


"""

# Descargamos el dataset y lo procesamos con pandas

dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
dataset_path

column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']
dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)


BUCKET = 'gs://mibucket'

# Por facilitar el ejemplo, quitamos las filas con valores faltantes

dataset = dataset.dropna()

# La columna "Origin" es de tipo categorica, el procedimiento con estas variables suele hacer un One-Hot Encoding

dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})

dataset = pd.get_dummies(dataset, prefix='', prefix_sep='')
dataset.tail()

# Dividimos el dataset en entrenamiento y test

train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# Por comprobar que ambos sets tienen una naturaleza "comun" se suelen mirar las estadisticas

train_stats = train_dataset.describe()
train_stats.pop("MPG")
train_stats = train_stats.transpose()
train_stats

# Separamos los targets para ambos sets de entrenamiento
train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

# Normalizamos los dos sets con sus respectivas estadísticas, esto es importante pues si normalizamos el conjunto de entrenamiento teniendo en cuenta la estadística del conjunto de test tendríamos un caso de data leakeage.

def norm(x):
    return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

# Construimos el modelo

def build_model():
    model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
    return model

model = build_model()
model.summary()

# Entrenamos el modelo con un callback de EarlyStopping para dejar de entrenar en caso de que la métrica a observar deje de evolucionar positivamente durante unas epocas de paciencia.

model = build_model()

EPOCHS = 1000

# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

early_history = model.fit(normed_train_data, train_labels, 
                    epochs=EPOCHS, validation_split = 0.2, 
                    callbacks=[early_stop])


# Guardamos el modelo en un bucket, esto es opcional.
model.save(BUCKET + '/mimodelo/model')
