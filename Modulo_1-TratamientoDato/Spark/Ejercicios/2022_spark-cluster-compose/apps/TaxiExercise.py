# Start Spark Session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Import sql functions
from pyspark.sql.functions import *

# Load datasets to DFs
taxiDF = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/taxi_data.csv")
taxiZonesDF = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/taxi_zones.csv")

taxiDF.printSchema()
taxiZonesDF.printSchema()

"""
Question 1: Which zones have the most pickups/dropoffs overall? Note there are many PULocationIDs per Zone?
"""

"""
We can understand the question as getting the most popular zones for PU/DO, each one separately. 
Or understand it as getting the most popular zones for PU/DO together. In the first case we will have to make two separate .groupBy() + .agg(count()), 
in the second case, we will do just one. In this exercise we will do it with the first approach only.
"""

# First approach
# First, we'll do the groupBy per PU, and then, we'll count the totalTrips. We need the join to have the zones info. And we join by PULocationID == LocationID because
# these are the columns with "same" info in our DFs

pickupsByTaxiZonePUDF = taxiDF.groupBy("PULocationID") \
    .agg(count("*").alias("totalTrips")) \
    .join(taxiZonesDF, col("PULocationID") == col("LocationID")) \
    .drop("LocationID", "service_zone") \
    .orderBy(col("totalTrips").desc())

pickupsByTaxiZonePUDF.show(3)

ratesByTaxiZonePUDF = taxiDF.groupBy("PULocationID") \
    .agg(count("RatecodeID").alias("ratecodeTotal")) \

ratesByTaxiZonePUDF.show(3) 

# 1b - Now we can group by borough. That's because one Borough have several Zones, and Borough info is more relevant (we think)
pickupsByBoroughPUDF = pickupsByTaxiZonePUDF.groupBy(col("Borough")) \
    .agg(sum(col("totalTrips")).alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByBoroughPUDF.show(2)

# Now we have to do the same for DOLocationIDs:
pickupsByTaxiZoneDODF = taxiDF.groupBy("DOLocationID") \
    .agg(count("*").alias("totalTrips")) \
    .join(taxiZonesDF, col("DOLocationID") == col("LocationID")) \
    .drop("LocationID", "service_zone") \
    .orderBy(col("totalTrips").desc())

pickupsByTaxiZoneDODF.show(3)

# 1b - Now we can group by borough.
pickupsByBoroughDODF = pickupsByTaxiZoneDODF.groupBy(col("Borough")) \
    .agg(sum(col("totalTrips")).alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByBoroughDODF.show(2)

# Tips: drop and orderBy is just for make it more readable. The logic is groupBy -> agg -> join
# We make th count("*") because we want to know EVERY different trips with no nulls in all columns. Depending on what we want, the logic may change at this point.


"""
Question 2: What are the peak hours for taxi?
"""

"""
This is similar to the previous exercise. The only difference will be we have to group by hour this time. As we don't have the hour info directly in our DF, we have
to process the tpep_pickup_datetime column first. The rest of the logic will be the same.
"""

pickupsByHourDF = taxiDF \
    .withColumn("hour_of_day", hour(col("tpep_pickup_datetime"))) \
    .groupBy("hour_of_day") \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByHourDF.show(3)


"""
Question 3: How are the trips distributed by length? Show stats like mean, max, min, etc.
Then get the total trips for less/more than 30 km. Why are people taking the cab? For long or short trips?
You can also try the same with different distances. Which is the expected value for threshold is we want to obtain more or less the same trips in long/short counting?
"""

"""
In this case we want to obtain data about one of the attributes of the df, the distance (trip_distance). 
So we will make a select of that particular column and then apply the corresponding aggregations (count, average, etc).
"""

# Select stats for taxiDF
tripDistanceDF = taxiDF.select(col("trip_distance").alias("distance"))
tripDistanceStatsDF = tripDistanceDF.select(
    count("*").alias("count"),
    lit(30).alias("threshold"),
    mean("distance").alias("mean"),
    stddev("distance").alias("stddev"),
    min("distance").alias("min"),
    max("distance").alias("max"))
tripDistanceStatsDF.show(3)

"""
In the second part we want to group by long vs. short trips. But we don't have this data in the DF, so we will first add a flag, 
to determine if it is long/short. And then we can group by that flag.
"""
# We will add a isLong column (flag) with the true/false for long/short rides
tripsWithLengthDF = taxiDF.withColumn("isLong", col("trip_distance") >= 30)
tripsWithLengthDF.show(2)

# As we want to know how many long/short trip are we have to groupBy islong and count()
tripsByLengthDF = tripsWithLengthDF.groupBy("isLong").count()
tripsByLengthDF.show()


"""
Question 4: What are the peak hours for long/short trips?
"""

"""
In this exercise the logic is something like a mix of the two previous ones. On the one hand we want to group by long/short trips (the previous flag), 
and on the other hand by hours. So we will use the DF that we have created previously with the flag (e.g. 3), modify the time column as we have done in e.g. 2; 
and then we can group by (hours, long/short). Note that in this case the groupBy will be done by both columns.
"""

# We will use the DF created before with isLong flag. 
# Then, we'll groupBy either islong and hour columns and make a count.

pickupsByHourByLengthDF = tripsWithLengthDF \
    .withColumn("hour_of_day", hour(col("tpep_pickup_datetime"))) \
    .groupBy("hour_of_day", "isLong") \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

pickupsByHourByLengthDF.filter(col("isLong") == True).show()
pickupsByHourByLengthDF.filter(col("isLong") == False).show()


"""
Question 5: What are the top 3 pickup/dropoff zones for long/short trips?
"""

"""
Again, we are going to use the DF we created with the long/short flag. But in this case we also want to group by zones. 
Similar to what we have seen in exercise 1, we can see it as PU/Do zones separately, or at the same time.
"""

"""
Let's see the first approach (separately).
"""
# We will use again the DF with isLong info.
# If we understand the question as PU and DO popularity seprated, we will have two DFs, one per each.

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

# If we want just the three first Rows we can also do a .limit(3) instead of .show()

"""
For the second approach, we have to do the groupBy for the two columns and two joins, one for PU and one for DO.
"""

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


"""
Question 6: How are people paying for the ride, on long/short trips? Hint: the information about how good is the payment is in RatecodeID column.
"""

"""
We can first inspect the RatecodeID column to see what information it provides. And then we simply do a .groupBy() + .agg(count()) as usual.
"""

# The RatecodeID columns has the info about how good is the payment.
taxiDF.select("RatecodeID").distinct().show()

ratecodeDistributionDF = taxiDF \
    .groupBy(col("RatecodeID")).agg(count("*").alias("totalTrips")) \
    .orderBy(col("totalTrips").desc())

ratecodeDistributionDF.show()


"""
Question 7: How is the payment type (RatecodeId) evolving with time (in days)? Hint: use the column with pickup time info.
Get the same info but with avg of ratecode and total trips per day.
"""

"""
For the day we will use tpep_pickup_datetime column. We have to remove the time info from it in order to do the groupBy, 
so we will do a to_date.
"""

# We have to group by pickup time and ratecode this time.
ratecodeEvolution = taxiDF \
    .withColumn("pickup_day", to_date(col("tpep_pickup_datetime"))) \
    .groupBy(col("pickup_day"), col("RatecodeID")) \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("pickup_day"))

ratecodeEvolution.show()

# Now we can get the avg ratecode per day.
ratecodeEvolutionAvg = ratecodeEvolution.groupBy("pickup_day").agg(sum("totalTrips").alias("totalTrips"), avg("RatecodeID").alias("avgRate"))

ratecodeEvolutionAvg.show()


"""
We can do the same for hours (just fyi, not in question). First we'll do the same as in exercise 2. And then, we'll do the average.
"""
# And the same for hours
ratecodeEvolutionPerHour = taxiDF \
    .withColumn("hour_of_day", hour(col("tpep_pickup_datetime"))) \
    .groupBy(col("hour_of_day").alias("pickup_hour"), col("RatecodeID")) \
    .agg(count("*").alias("totalTrips")) \
    .orderBy(col("pickup_hour"))

ratecodeEvolutionPerHour.show()

# Now we agg in the same way to obtain avg rate and total trips.
ratecodeEvolutionPerHourAvg = ratecodeEvolutionPerHour.groupBy("pickup_hour") \
    .agg(sum("totalTrips").alias("totalTrips"), avg("RatecodeID").alias("avgRate")).orderBy("pickup_hour")

ratecodeEvolutionPerHourAvg.show()