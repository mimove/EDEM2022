# EDEM - Master on Data Analytics - SQL

## Introduction

<img width="100" src="https://www.postgresql.org//media/img/about/press/elephant.png">


*(Following steps of [YouTube video](<https://www.youtube.com/watch?v=ZUORufqaN9M&list=LL&index=3&t=10s>) by Pedro Nieto )

In these section we will setup **[PostgreSQL](https://www.postgresql.org/)** and load a database [dvdrental](<https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/>) for learning SQL

## Initial Setup

We will be using the Docker Compose in this root folder, so start the Docker Compose components:

```shell
docker compose up -d
```

```shell
# List the running services
docker ps

# Stop a specific service
docker compose stop <SERVICE>
```


## Services

You will find the access to the pgAdmin in the following URL:

* [pgAdmin](http://localhost:5050/)
  * **Username**: pgadmin4@pgadmin.org
  * **Password**: admin


## Steps inside pgAdmin to create a server and load the Data Base of dvdrental

1. Right click on Servers->Create->Sever
    
    1.1 In tab General introduce name server1

    1.2  In tab Connection introduce Host name: postgres, Username: postgres and password: Welcome01. Click on Save Password 

    1.3 Click on Save

2. Click on the down arrow of server1 and right click on Databases(1)->Create->Database

    2.1 In tab General, write the name of the Database as dvdrental

    2.2 Click on Save

3. Right click on dvdrental->Restore

    3.1 Drag and drop the dvdrental.tar file that is inside dvdrental.zip

    3.2 Click on Show hidden files and folders?

    3.3 Select the Format as All Files

    3.4 Click on the x at the top right corner

    3.5 Click on dvdrental.tar

    3.6 Click on Select

    3.7 Select Role Name as postgres

    3.8 Click on Restore


4. Right click on dvdrental->Query tool







## Shut down and destroy

```shell
# Shut down the cluster
docker compose down
```