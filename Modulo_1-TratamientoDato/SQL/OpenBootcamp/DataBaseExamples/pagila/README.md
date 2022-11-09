# LOADING PAGILA DATABASE

## Steps

1. Follow the steps of this [README.md](../../../../SQL/Entregables/docker_PostgreSQL/README.md) which shows how to start a docker image of a postgres sever.

```sh
docker compose up -d
```

2. Copy the ```pagila-schema.sql``` and ```pagila-schema.sql``` into the ```/data``` directory of the conainter

```sh
docker cp pagila-data.sql <postgres container id>:/data
docker cp pagila-schema.sql <postgres container id>:/data
```

3. Log into the container

```sh
docker exec -it <postgres container id> bash
```

4. Run the following commands to create the database pagila and fill it with its data

```sh
psql -U postgres
```

```
psql (12.1 (Debian 12.1-1.pgdg100+1))
Type "help" for help.

postgres=# CREATE DATABASE pagila;
postgres=# \q
```

```sh
psql -h localhost -p 5432 -U postgres -d pagila < pagila-schema.sql
```

```sh
psql -h localhost -p 5432 -U postgres -d pagila < pagila-data.sql
```