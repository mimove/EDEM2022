from pyspark.sql import SparkSession
# Import sql functions
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()
taxiDF = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/taxi_data.csv")



taxiDF.printSchema()

taxiDF.show(2)

taxiZonesDF = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("/opt/spark-data/taxi_zones.csv")

taxiZonesDF.printSchema()

taxiZonesDF.show(3)


## QUESTION 1 

print('####### QUESTION 1 ##########')
pickupsByTaxiZoneDF = taxiDF.groupBy("PULocationID") \
    .agg(count("*").alias("totalTrips")) \
    .join(taxiZonesDF, col("PULocationID") == col("LocationID")) \
    .drop("LocationID", "service_zone") \
    .orderBy(col("totalTrips").desc())

pickupsByTaxiZoneDF.show(3)



# 1b - group by borough (city)
pickupsByBoroughDF = pickupsByTaxiZoneDF.groupBy(col("Borough")) \
    .agg(sum(col("totalTrips")).alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByBoroughDF.show(2)


print('###############\n\n\n\n')


## QUESTION 2

print('########## QUESTION 2 ##########')

pickupsByHourDF = taxiDF \
    .withColumn("hour_of_day", hour(col("tpep_pickup_datetime"))) \
    .groupBy("hour_of_day") \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByHourDF.show(3)

print('###############\n\n\n\n')


## QUESTION 3 

print('########### QUESTION 3 ###########')

print('Get stats for taxiDF')

tripDistanceDF = taxiDF.select(col("trip_distance").alias("distance"))
tripDistanceStatsDF = tripDistanceDF.select(
    count("*").alias("count"),
    lit(30).alias("threshold"),
    mean("distance").alias("mean"),
    stddev("distance").alias("stddev"),
    min("distance").alias("min"),
    max("distance").alias("max")
  )

tripDistanceStatsDF.show(3)


print('\nWe will add a isLong column with the true/false for long/short rides')

tripsWithLengthDF = taxiDF.withColumn("isLong", col("trip_distance") >= 30)

tripsWithLengthDF.show(2)


print('\nAs we want to know how many long/short trip are we have to groupBy islong and count()')
tripsByLengthDF = tripsWithLengthDF.groupBy("isLong").count()

tripsByLengthDF.show()

print('\n\n\n\n################')


## QUESTION 4

print('####### QUESTION 4 #############')

print("We will use the DF created before with isLong flag. Then, we'll groupBy either islong and hour columns and make a count.")

pickupsByHourByLengthDF = tripsWithLengthDF \
    .withColumn("hour_of_day", hour(col("tpep_pickup_datetime"))) \
    .groupBy("hour_of_day", "isLong") \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByHourByLengthDF.filter(col("isLong") == True).show()


pickupsByHourByLengthDF.filter(col("isLong") == False).show()


print('\n\n\n\n###############')


## QUESTION 5

print('We will use again the DF with isLong info.')

print('If we undertand the question as PU and DO popularity seprated, we will have two DFs, one per each.')


PUPopularDF = tripsWithLengthDF.groupBy("PULocationID").agg(count("*").alias("totalTrips")) \
    .join(taxiZonesDF, col("PULocationID") == col("LocationID")) \
    .withColumnRenamed("Zone", "Pickup_Zone") \
    .drop("LocationID", "Borough", "service_zone", "PULocationID") \
    .orderBy(col("totalTrips").desc())

PUPopularDF.show(10)



DOPopularDF = tripsWithLengthDF.groupBy("DOLocationID").agg(count("*").alias("totalTrips")) \
    .join(taxiZonesDF, col("DOLocationID") == col("LocationID")) \
    .withColumnRenamed("Zone", "Dropoff_Zone") \
    .drop("LocationID", "Borough", "service_zone") \
    .drop("DOLocationID") \
    .orderBy(col("totalTrips").desc())

DOPopularDF.show(10)


print('But if we undertand the question as the most popular zones per PU/DO at the same time (trips with the same PU/DO, not just one) we have to do the groupBy for the two columns and two joins, one for PU and one for DO.')

PUandDOPopularDF = tripsWithLengthDF.groupBy("PULocationID", "DOLocationID").agg(count("*").alias("totalTrips")) \
    .join(taxiZonesDF, col("PULocationID") == col("LocationID")) \
    .withColumnRenamed("Zone", "Pickup_Zone") \
    .drop("LocationID", "Borough", "service_zone") \
    .join(taxiZonesDF, col("DOLocationID") == col("LocationID")) \
    .withColumnRenamed("Zone", "Dropoff_Zone") \
    .drop("LocationID", "Borough", "service_zone") \
    .drop("PULocationID", "DOLocationID") \
    .orderBy(col("totalTrips").desc())

PUandDOPopularDF.show(10)



print('\n\n\n\n###############')


## QUESTION 6

print('######## QUESTION 6 ############')

print('The RatecodeID columns has the info about how good is the payment.')

taxiDF.select("RatecodeID").distinct().show()

ratecodeDistributionDF = taxiDF \
    .groupBy(col("RatecodeID")).agg(count("*").alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())


ratecodeDistributionDF.show()


print('\n\n\n\n###############')


## QUESTION 7 

print('####### QUESTION 7 ###########')

print('We have to group by pickup time and ratecode this time.')

ratecodeEvolution = taxiDF \
    .groupBy(to_date(col("tpep_pickup_datetime")).alias("pickup_day"), col("RatecodeID")) \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("pickup_day"))

ratecodeEvolution.show()




print('Now we can get the avg ratecode per day.')

ratecodeEvolutionAvg = ratecodeEvolution.groupBy("pickup_day").agg(sum("totalTrips").alias("totalTrips"), avg("RatecodeID").alias("avgRate"))

ratecodeEvolutionAvg.show()



print('And the same but this time grouping by hour')

ratecodeEvolutionPerHour = taxiDF \
    .withColumn("hour_of_day", hour(col("tpep_pickup_datetime"))) \
    .groupBy(col("hour_of_day").alias("pickup_hour"), col("RatecodeID")) \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("pickup_hour"))

ratecodeEvolutionPerHour.show()



print('\nNow we agg in the same way to obtain avg rate and total trips. ')

ratecodeEvolutionPerHourAvg = ratecodeEvolutionPerHour.groupBy("pickup_hour") \
    .agg(sum("totalTrips").alias("totalTrips"), avg("RatecodeID").alias("avgRate")).orderBy("pickup_hour")

ratecodeEvolutionPerHourAvg.show()
