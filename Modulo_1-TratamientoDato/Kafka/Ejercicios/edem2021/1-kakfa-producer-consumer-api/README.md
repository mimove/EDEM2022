# Kafka - Lab 1 

## Objectives

 1) Run Zookeeper + Kafka
 2) Produce messages from the command line
 3) Consume/Read messages from the command line
 4) Produce messages from a Java application.
 5) Consume/Read messages from a Java application.
 6) Modify the Java Producer and/or Consumer Java application.


### Requirements

 * Docker for Windows
 * Docker Compose 
 * Oracle JDK (para compilar Java) https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html
 * Maven (para compilar Java) https://ftp.cixug.es/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.zip (How-to install: https://maven.apache.org/install.html)

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

### Command Line Producer

Run the command line producer:

```sh
$ docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
>hi
>dlp
>

```

Read topic content:

```sh
$ docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
hi
dlp
```

### Java Example

The example is a Maven project. You can import the project as Maven project with your IDE. 

* Producer: The producer will generate 100 messages and send them to the `myTopic`. 
* Consumer: Consume and log messages from `myTopic`.  

### Run the Java application
Execute the Consumer: "com.gft.dlp.kafka.Consumer"
Execute the Producer:"com.gft.dlp.kafka.Producer"


#### Exercises 

* Modify the Java Producer Application and send different messages. Verify in the Consumer (command line or 
  Java Consumer application) that you can read/consume the new messages.
*  Use a messages more complex than a String. For example a JSON message like this one => {"name":"John", "age": 26} 
where you can increment the message JSON attribute "age" number in each sent message.

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```
