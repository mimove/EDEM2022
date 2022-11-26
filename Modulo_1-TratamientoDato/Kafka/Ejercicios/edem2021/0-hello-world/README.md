# Kafka - Lab 0 

## Objectives

 1) Run Zookeeper + Kafka
 2) Check status
 3) Create a topic

### Requirements

 * Docker for Windows
 * Docker Compose 

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
lab0_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab0_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```

### Zookeeper 

Check the ZooKeeper logs to verify that ZooKeeper is healthy.

```sh
$ docker-compose logs zookeeper | Select-String binding
```

Sample output: 

```sh
zookeeper    | [2020-02-18 15:49:28,229] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
```

### Broker 

Check the Kafka logs to verify that broker is healthy.

```sh
$ docker-compose logs kafka | Select-String started
```

Sample output: 

```sh
kafka_1      | [2020-02-18 16:05:21,153] INFO [SocketServer brokerId=1] Started 2 acceptor threads for data-plane (kafka.network.SocketServer)
kafka_1      | [2020-02-18 16:05:21,646] DEBUG [ReplicaStateMachine controllerId=1] Started replica state machine with initial state -> Map() (kafka.controller.ZkReplicaStateMachine)
kafka_1      | [2020-02-18 16:05:21,663] DEBUG [PartitionStateMachine controllerId=1] Started partition state machine with initial state -> Map() (kafka.controller.ZkPartitionStateMachine)
kafka_1      | [2020-02-18 16:05:21,715] INFO [SocketServer brokerId=1] Started data-plane processors for 2 acceptors (kafka.network.SocketServer)
kafka_1      | [2020-02-18 16:05:21,727] INFO [KafkaServer id=1] started (kafka.server.KafkaServer)
```

### Create Topic

Create a topic named `myTopic`, one partition and one replica.

```sh
$ docker-compose exec kafka kafka-topics --create --topic myTopic --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server host.docker.internal:9092
```

Output: 

```sh
Created topic myTopic.
```

Topic information:

```sh
$ docker-compose exec kafka kafka-topics --describe --topic myTopic --bootstrap-server host.docker.internal:9092
```

Output: 

```sh
Topic: myTopic  PartitionCount: 1       ReplicationFactor: 1    Configs:
        Topic: myTopic  Partition: 0    Leader: 1       Replicas: 1     Isr: 1
```

### Clean up_

Shut down Docker Compose

```sh
$ docker-compose down
```
