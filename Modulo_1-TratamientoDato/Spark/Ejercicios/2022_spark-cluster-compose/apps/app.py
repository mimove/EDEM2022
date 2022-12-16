from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


# Import sql functions
from pyspark.sql.functions import *


taxiDF = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/taxi_data.csv")
taxiZonesDF = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/taxi_zones.csv")

taxiDF.printSchema()