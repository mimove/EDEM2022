# Spark Cluster with Docker & docker-compose

# General

A simple spark standalone cluster for your testing environment purposses. A *docker-compose up* away from you solution for your spark development environment.

The Docker compose will create the following containers:

container|
---|
spark-master|
spark-worker-1|
spark-worker-2|
...|
spark-worker-n|


# Installation

The following steps will make you run your spark cluster's containers.

## Pre requisites

* Docker installed

* Docker compose  installed


## Build the images

The first step to deploy the cluster will be the build of the custom images, these builds can be performed with the *build-images.sh/build-images.bat* script. 

The executions is as simple as the following steps:

```sh
./build-images.sh
```
*If you don't have exec permission run first.

```sh
chmod +x build-images.sh
```

This will create the following docker images:

* spark-base:2.3.1: A base image based on java:alpine-jdk-8 wich ships scala, python3 and spark 2.3.1

* spark-master:2.3.1: A image based on the previously created spark image, used to create a spark master containers.

* spark-worker:2.3.1: A image based on the previously created spark image, used to create spark worker containers.


## Run the docker-compose

The final step to create your test cluster will be to run the compose file:

```sh
docker-compose up --scale spark-worker=2
```
To create *n* containers execute with spark-worker=n

## Validate your cluster

Go to localhost:9090 to see the Spark Master UI.


# Resource Allocation 

This cluster is shipped with three workers and one spark master, each of these has a particular set of resource allocation(basically RAM & cpu cores allocation).

* The default CPU cores allocation for each spark worker is 1 core.

* The default RAM for each spark-worker is 1024 MB.

* The default RAM allocation for spark executors is 256mb.

* The default RAM allocation for spark driver is 128mb


# Binded Volumes

To make app running easier we have two volume mounts described in the following chart:

Host Mount|Container Mount|Purposse
---|---|---
/mnt/spark-apps|/opt/spark-apps|Used to make available your app on all workers & master
/mnt/spark-data|/opt/spark-data| Used to make available your app's data on all workers & master


# Run a sample application

Now let`s run our apps.

Create a PySpark app and copy the .py file to apps folder on your host (it will be loaded in our nodes as well on /opt/spark-apps).

Then run on your master:

```sh
bash /spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark-apps/app.py
```

If you want to avoid all the INFO logs when running our app, you can copy a custom log4j2.properties file to the node by running:

```sh
ocker cp env/log4j2.properties <master_container_ID>:/spark/conf/log4j2.properties
```

You can  find <master_container_ID> by running on **YOUR HOST CONSOLE** (not into containers):

```sh
docker ps
```

# Summary:

* We compiled the necessary docker images to run spark master and worker containers.

* We created a spark standalone cluster using 2 worker nodes and 1 master node using docker && docker-compose.

* Copied the resources necessary to run a sample application.

* We ran a distributed application at home(just need enough cpu cores and RAM to do so).

# Why a standalone cluster?

* This is intended to be used for test purposses, basically a way of running distributed spark apps on your laptop or desktop.

* This will be useful to use CI/CD pipelines for your spark apps(A really difficult and hot topic)
