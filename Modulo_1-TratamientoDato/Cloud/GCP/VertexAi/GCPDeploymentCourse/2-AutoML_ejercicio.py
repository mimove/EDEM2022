from sklearn.datasets import fetch_covtype
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score

df = fetch_covtype(return_X_y=False, as_frame=True)['frame']
df = df[df.Cover_Type.isin([5, 3])].sample(2000).reset_index(drop=True)
train = df.head(1500)
test = df.tail(500)


df.to_csv("2ejercicio.csv", index=False)