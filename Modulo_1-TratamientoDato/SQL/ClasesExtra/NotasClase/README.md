# BASES DE DATOS

## 1. Introducción

SQL es un lenguaje de consulta,un lenguaje en el que el usuario solicita información de la base de datos, suelnen ser de un nivel superior a los lenguajes de programación.

Además de cosnultas, con SQL, es posible definir la estructura de los datos, modificar los datos de la base de datos y especificar restricciones de seguridad. 

SQL se base en le Teoría Mat´matica del Álgebra Relacional. El lenguaje SQL consta de varios elementos.

- Lenguaje de definición de datos (DDL): proporcional órdenes para definir, modificar o eliminar los distintos objetos de la base de datos (tablas, vistas, índices, etc.).

- Lenguaje de Manipulación de Datos: proporcional órdenes para insertar, modificar, eliminar y consultar datos de la base de datos.

- Lenguaje de Control de Datos: proporcional órdenes para controlar el acceso a los datos de la base de datos. 


Las distintas implementacions de SQL pueden diferenciarse en detalles, o pueden admitir sólo un subcojunto del lenguaje completo.

El restultado de ejecutar una consulta SQL es un conjunto de filas y columnas, denominado conjunto de resultados.



### Ejercicio 1

```sh
docker run -d -p 3306:3306 --name my-mysql-container -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=edem_db -e MYSQL_USER=edem_user -e MYSQL_PASSWORD=edem_password mysql:latest

brew install mysql
mysql -h localhost --port 3306  -u edem_user --password=edem_password --protocol=tcp
```


### Algunas consideraciones

Las relaciones de cada base de datos deben especificarse en el sistema en términos de un lenguaje de definición de datos (DDL). 

El lenguaje de definición de datos (DDL) es un lenguaje de alto nivel que permite especificar la estructura de la base de datos.

El lenguaje de manipulación de datos (DML) es un lenguaje de bajo nivel que permite especificar las operaciones de consulta y modificación de la base de datos.

El lenguaje de control de datos (DCL) es un lenguaje de bajo nivel que permite especificar las restricciones de seguridad de la base de datos.



## Definición básica de esquemas SQL

Para crear una tabla utilizamos el comando create table:

```sql
CREATE TABLE <nombre_tabla> (
    <nombre_columna> <tipo_dato> <restricciones>,
    <nombre_columna> <tipo_dato> <restricciones>,
    ...
    <nombre_columna> <tipo_dato> <restricciones>
);
```

Ejemplo:

```sql
CREATE TABLE IF NOT EXISTS alumnos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    email VARCHAR(50) UNIQUE,
    telefono VARCHAR(15)
);
```


## Restricciones de integridad

Las restricciones de integridad son condiciones que deben cumplir los datos almacenados en la base de datos. 

Tipos:

- Oblicatoriedad: NOT NULL
- Clave primaria: PRIMARY KEY (los atributos han de ser no nulos y únicos)
- Clave foránea: FOREIGN KEY
- Verificación: CHECK AUTO_INCREMENT
- Valores por defecto: DEFAULT

Ejemplo query con todos los tipos:
    
```sql
CREATE TABLE IF NOT EXISTS alumnos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE DEFAULT '1900-01-01',
    email VARCHAR(50) UNIQUE,
    telefono VARCHAR(15),
    CONSTRAINT fk_alumnos FOREIGN KEY (id) REFERENCES alumnos (id),
);
 ```


**INTEGRIDAD REFERENCIAL**

Asegura qued un valor que aparece en una relación para un conunto de atributos determinado aparezca también en otra relación para un cierto conjunto de atributos.

Las calves primarias, candidatas y las claves externas o ajenas se pueden especificar como parte de la instrucción create table de SQL:

- La claúsula primara key incluye una lista de los atributos que comprende la clave primaria.
- La cláusula unique key incluye una lista de los atributso que comprende una clave candidata.
- La claúsula foreign key incluye una lista de los atributos que comprende la clave externa y el nombre de la relación a la que hce referencia mediante la clave externa. Por defecto, una clave externa hace referencia a los atributos de la clave primaria de la tabla referenciada.


