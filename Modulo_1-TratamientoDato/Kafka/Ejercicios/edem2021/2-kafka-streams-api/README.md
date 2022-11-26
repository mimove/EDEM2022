# Kafka Streams Lab

## Objectives

 1) Run Zookeeper + Kafka
 2) Produce messages
 3) Process messages with Kafka Streams DSL
 4) Output results
 
## Run
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
$ docker-compose up -d
```

Status: 

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab1_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab1_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```
 
### Example Description

The example is a Kafka Java application build with Maven. You can import the project as Maven project with your IDE. 

* **Shakespeare Quotes Producer (Java file com.gft.dlp.kafka.ProducerStep1.java)**: The producer will generate 1000 Shakespeare random quotes messages, 
by using the [Faker API](https://github.com/DiUS/java-faker), and send them to the Kafka topic `quotes-input`.
  * Quote Examples: 
    * `True is it that we have seen better days.`
    * `Can one desire too much of a good thing?.`

* **Word Count Kafka Streaming Processor (Java file com.gft.dlp.kafka.Step2WordCountProcessor.java)**: The WordCount,
using the high-level Kafka library [KStream DSL](https://docs.confluent.io/current/streams/developer-guide/dsl-api.html),
will read in near-realtime the Shakespeare random quotes messages previously saved in the Kafka topic `quotes-input`, 
and compute a simple word occurrence histogram from each Shakespeare quote line. 
The histogram output is written to the Kafka topic "streams-wordcount-output", where each record is an updated count of a single word

* **Results Consumer ((Java file com.gft.dlp.kafka.Step3Consumer.java)**: The Consumer will read and print the messages
stored in the Kafka topic "streams-wordcount-output" in previous step by com.gft.dlp.kafka.Step2WordCountProcessor.java

Example of the outpout printed by the final Consumer Step3Consumer.java: 

```sh
     | think | 625
     | he | 625
     | is | 1852
     | wise | 1249
```

### Running

Execute the com.gft.dlp.kafka.Step1Producer

Run com.gft.dlp.kafka.Step2WordcountConsumer

Run com.gft.dlp.kafka.Step3Consumer
 

#### Extra Exercises

* Filter words - Example: Count only words with length > 3

* Filter results - Example: Count > 10000

* Hint: Modify code at com.gft.dlp.kafka.Step2WordCountProcessor.java after "wordCounts.toStream()."

 

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```


