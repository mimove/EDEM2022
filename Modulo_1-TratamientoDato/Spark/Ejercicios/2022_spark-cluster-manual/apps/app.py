from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/taxi_data.csv")

print(df.count())
df.printSchema()