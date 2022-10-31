# Entregable SQL

## Descripción del caso

En este entregable tenemos que realizar una serie de consultas sobre una base de datos que obtenemos de la web de [este enlace](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/). 

El Entity-Relationship model de esta base de datos es el de la siguiente imagen:

<p align="center">
<img src="https://www.postgresqltutorial.com/wp-content/uploads/2018/03/dvd-rental-sample-database-diagram.png" width=500px>


<br>
<br>

## Uso de PostgreSQL con Docker y Visual Studio Code para hacer consultas  a la base de datos

<br>

<p align="center">
<img src="https://github.com/mimove/mimove/blob/main/.images/postgre_docker_vscode.png?raw=true">
</p>

<br>

Para hacer las consultas a esta base de datos, lo que se ha hecho es utilizar una imagen de postreSQL dentro de un contenedor Docker que, una vez levantada, se puede conectar a Visual Studio Code a través de la extensión desarrollada por **Matheus Teixeria** que se puede descargar en [este enlace](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-pg). Los pasos a seguir son:


1. Entrar en el directorio [docker_PostreSQL](docker_PostgreSQL/) y seguir los pasos escritos en el README.md para levantar el servidor PostreSQL dentro del contenedor y cargar la base de datos **dvdrental** en el servidor.

2. Abrimos Visual Studio Code y hacemos click en el icono de la izquierda que dice SQLTools. 

3. Nos conectamos a la base de datos introduciendo los siguientes campos:

    | Campo | Texto a completar |
    |----------|---------|
    | <b>Connection name*</b> | \<nombre que queramos>  |
    | <b>Server Address*</b> | localhost  |
    | <b>Port*</b> | 5432  |
    | <b>Database*</b> | dvdrental  |
    | <b>Username*</b> | postgres  |
    | <b>Password</b> | Welcome01  |


4. Una vez conectados, se abre automáticamente un archivo con el nombre \<nombre que queramos>.session.sql donde podemos hacer consultas SQL. 

<br>

## Queries a completar

Las consultas SQL de las que hay que proporcionar una respuesta son las siguientes:

1. Proporciona una SQL que muestre los siguientes datos:
   - Nombre Actor
   - Apellido Actor

2. Proporciona una SQL que muestre los siguientes datos:
   - Nombre y apellido Actor,
   - Titulo de la Película

3. Proporciona una SQL que muestre los siguientes datos:
   - Nombre y apellido Actor
   - Número de películas 

4. Ordenar de mayor a menor
   - Proporciona una SQL que muestre los siguientes datos:
   - Película
   - Numero de veces alquilada(orden de mayor a menor)


5. Proporciona una SQL que muestre los siguientes datos:
   - Película
   - Dinero recaudado por película(ordenado)

6. Proporciona una SQL que muestre los siguientes datos:
   - Nombre y apellido del mejor cliente (mayor gasto)

7. Proporciona una SQL que muestre los siguientes datos:
   - Nombre y apellido del mejor cliente (mayor num alquileres)


Las respuestas se encuentran en el directorio [Ejercicios](Ejercicios/). El README.md contiene las consultas y parte del resultado, mientras que el archivo Postgres.session.sql contiene las consultas en formato .sql.