# Spark Cluster with Docker & docker-compose step-by-step

A simple spark standalone cluster for your testing environment purposses.

We will create the following containers:

container|
---|
spark-master|
spark-worker-1|
spark-worker-2|


## Create netwok

First we need to create a network. So open a new console in your machine and run:

```sh
docker network create -d bridge cluster
```

If it return that the network is already created is fine.

## Configure master node

Now we will configure the master node. So that, first we will run up a docker container with openjdk8. In your machine console run:

```sh
docker run -it --name spark-master -p 8080:8080 --network cluster adoptopenjdk/openjdk8
```

Now this console is inside the container, not in your machine! In this console run:

```sh
apt-get update && apt-get install -y curl vim wget software-properties-common ssh net-tools jq dbus-x11
apt-get install -y python3 python3-pip python3-numpy python3-matplotlib python3-scipy python3-pandas python3-simpy
```

We have to copy now the spark files, and additionally a spark sample app and data. Opne a new console **in your machine** and run:

```sh
docker cp spark-3.3.1-bin-hadoop2 spark-master:/spark
docker cp apps spark-master:/opt/spark-apps
docker cp data spark-master:/opt/spark-data
```

### Start spark-master

Now we will start the master. So, in the previous console, **inside the container** we will run:

```sh
bash /spark/sbin/start-master.sh -h 0.0.0.0
```

If your console has colsed somehow, you can open a new one by running in your machine:

```sh
docker exec -it <master_container_ID> bash
```

To get the maste_container_ID run:

```sh
docker ps
```


# Configure worker node

The process will be similar to the master. So, open a **new console** in your machine and run:

```sh
docker run -it --name spark-worker1 -p 8081:8081 --network cluster adoptopenjdk/openjdk8
```

Now this console is inside the container, not in your machine! In this console run:

```sh
apt-get update && apt-get install -y curl vim wget software-properties-common ssh net-tools jq dbus-x11
apt-get install -y python3 python3-pip python3-numpy python3-matplotlib python3-scipy python3-pandas python3-simpy
```

We have to copy now the spark files, and additionally a spark sample app and data. Opne a new console **in your machine** and run:

```sh
docker cp spark-3.3.1-bin-hadoop2 spark-worker1:/spark
docker cp apps spark-worker1:/opt/spark-apps
docker cp data spark-worker1:/opt/spark-data
```

Then we can start the worker. Run this command on the workers shell.

```sh
bash /spark/sbin/start-worker.sh -c 2 -m 4g spark://<IP_MASTER_NODE>:7077
```

To get the master IP Adress run docker inspect spark-master (or <master_container_id>) in your machine.

```sh
docker inspect <master_container_ID>
```

## Run Spark Job

Now we can run our first app. Go to the master`s shell and run:

```sh
bash /spark/bin/spark-submit --master spark://<IP_MASTER_NODE>:7077 /opt/spark-apps/app.py 
```

To set log level to WARN you can either chang the /spark/conf/log4j2.properties or run this command in your local machine.

```sh
docker cp env/log4j2.properties spark-master:/spark/conf/log4j2.properties
```


## Add second worker

The process will be the same as for the first worker, but with different names.
Here we describe the commands.

In a new shell on your machine:

```sh
docker run -it --name spark-worker2 adoptopenjdk/openjdk8
```

In the previous shell:

```sh
apt-get update && apt-get install -y curl vim wget software-properties-common ssh net-tools jq dbus-x11
apt-get install -y python3 python3-pip python3-numpy python3-matplotlib python3-scipy python3-pandas python3-simpy
```

In your machine:

```sh
docker cp spark-3.3.1-bin-hadoop2 spark-worker2:/spark
docker cp apps spark-worker2:/opt/spark-apps
docker cp data spark-worker2:/opt/spark-data
```

And finally in the worker shell:

```sh
bash /spark/sbin/start-worker.sh -c 2 -m 4g spark://<IP_MASTER_NODE>:7077
```


## Validate your cluster

Go to localhost:9090 to see the Spark Master UI.