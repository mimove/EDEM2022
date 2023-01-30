import pandas as pd

prefix = "gs://example_od_1/"


df = pd.read_csv("dataset/train_labels.csv")
df[["xmin","xmax"]] = df[["xmin","xmax"]].div(df.width, axis=0)
df[["ymin","ymax"]] = df[["ymin","ymax"]].div(df.height, axis=0)
df["class"] = "obama"
df = df[["filename", "class", "xmin", "ymin", "xmax", "ymin", "xmax", "ymax", "xmin", "ymax"]]
df.filename = prefix + df.filename
df.to_csv("dataset/train_correct.csv", index=False, header=False)

df = pd.read_csv("dataset/test_labels.csv")
df[["xmin","xmax"]] = df[["xmin","xmax"]].div(df.width, axis=0)
df[["ymin","ymax"]] = df[["ymin","ymax"]].div(df.height, axis=0)
df["class"] = "obama"
df = df[["filename", "class", "xmin", "ymin", "xmax", "ymin", "xmax", "ymax", "xmin", "ymax"]]
df.filename = prefix + df.filename
df.to_csv("dataset/test_correct.csv", index=False, header=False)

