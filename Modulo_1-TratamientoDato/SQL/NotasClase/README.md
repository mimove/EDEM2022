# Notas clase sobre SQL

## _Clase 22/10/2022_

SQL (Structured Query Language) es un lenguaje de dominio para manipular, seleccionar, añadir, borrar, etc. en bases de datos. Hay 2 tipos de bases de datos:

- Relacional: Tienes tablas ordenadas con filas, columnas, y cabezera en la que hay una relación (1-1, 1-n o n-1) entre ellas. Ej:

<br>

MASTERS     
| ID | Nombre | Coste |
| ------ | ------------ | -------- |
| DTA  | DATA | 10000 |
| MKT | MARKETING | 8000 |
|  . | . |
| . | . |
    
<br>

ALUMNOS                              
| ID | Nombre | Edad | País | Ciudad |                    
| ------ | ---- | ------ | ------ |  ------ |         
| 1 | Miguel | 31 | USA | Nueva York |           
| 2 | Julio | 29 | UK |   Southampton |                     
| . | . |  .    |                       
| . | . |  .   |                          
| . | . | . |


<br>

ALU_MASTER                              
| ID | ID_ALUMNO | ID_MASTER |                      
| ------ | ---- | ------ |              
| 1 | 1 | MKT |              
| 2 | 2 | DTA |                         
| . | . |                               
| . | . |                               
| . | . |

<br>


- No relacional: Todo los demás tipos de estrucutras de datos que nos pueden llegar: imagenes, videos, audios, texto plano, etc.



[Bigquery][bigquery] es el almacen de datos corporativos de Google y lo que utilizaremos para hacer consultas. Bigquery tiene datos cifrados, durables y altamente disponibles. Este servicio es escalable, simple, compartible, seguro y barato. 

<br>

### Tipos operaciones SQL

 - DDL (Data Definition Language): Permite crear y modificar la estructura de una base de datos. 

 - DML (Data Manipulation Language): Permite recuperar, almacenar, modificar, eliminar, insertar y actualizar datos de una base de datos. Este es el bloque que más se va a tratar en el Máster.

 - DCL (Data Control Language): Permite crear roles, permisos e integridad referencial, así como el control al acceso a la basee de datos.

 - TCL (Transactional Control Language): Permite administrar diferentes transacciones que ocurren dentr de uan base de datos.

 <p align="center">
 <img src="https://static.javatpoint.com/sqlpages/images/types-of-sql-commands.png" width=500px>
 </p>

<br>

<br>

## DATA MANIPULATION LANGUAGE

Comandos más típicos:

- SELECT: Para consultar registros 

- INSERT: Para cargar registros

- UPDATE: Para actualizar registros

- DELETE: Para eliminar registros


<br>

**Sintaxis de SELECT**

```sql
ORDER BY:
 - ASC: De menor a mayor
 - DESC: De mayor a menor


SELECT DISTINCT Y SELECT DISTINCT ON(GROUP BY)


WHERE:
- AND y OR
- = y <>
- IN y NOT IN


LIKE y NOT LIKE:
- Operadores: % y _

BETWEEN
```


Ejemplo SQL con tablas del inicio:

```sql
SELECT * --El asterísco se usa para seleccionar todas las columnas
FROM Alumnos
WHERE Edad < 30 AND Pais <> 'España'
WHERE Ciudad LIKE (%S)
ORDER BY Edad, DESC, Nombre;
```


Ejemplos diapositivas:

```sql
SELECT NOM,PAIS FROM EDEM.ALUMNOS; --Devuelve 2 columnas Nombre y País de EDEM.ALUMNOS 

SELECT NOM FROM EDEM.ALUMNOS WHERE ID BETWEEN 1 AND 10; --Devuelve Nombre de EDEM.ALUMNOS cuyo ID esté entre 1 y 10

SELECT NOM FROM EDEM.ALUMNOS WHERE NOM LIKE '%O%'; --Devuelve Nombre de EDEM.ALUMNOS cuyo nombre contenga una O (el % al inicio no afecta al primer caracter)

SELECT NOM FROM EDEM.ALUMNOS WHERE ID IN (1,2,3); --Devuelve Nombre de EDEM.ALUMNOS que tengan ID 1, 2 y 3
``` 

El ```;``` se utiliza para separar queries. En el ejemplo anterior, habría 4 queries.


<br>

**Sintaxis de INSERT**

```sql
INSERT INTO table_name --Todas las columnas por orden
VALUES(data1, data2, etc) ;

INSERT INTO table_name(field1, field2) --Columnas específicas
VALUES(data1,data2,...) ;
```




Ejemplo SQL con tablas del inicio:

```sql
INSERT INTO Alumnos
VALUES(1, 'Marina', 23, 'ESPAÑA', 'Valencia');

INSERT INTO Alumnos(Nombre, Edad)
VALUES('Marina', 23)
```


<br>

**Sintaxis de UPDATE**

*Hay que poner cuidado y poner ```WHERE``` para modificar solo los registros que queremos.

```sql
UPDATE table_name 
SET column_name = new_value --Una columna
WHERE some_condition; 

UPDATE table_name 
SET column_name = new_value, column_name = new_value  --Múltiples columnas
WHERE some_condition;

UPDATE table_name 
SET column_name = column_name + 1; --Valor personalizado
```

Ejemplo SQL con tablas del inicio:

```sql
UPDATE ALUMNOS 
SET Edad = 27 
WHERE Nombre = 'Miguel';

UPDATE ALUMNOS
SET Edad = 27, Nombre = 'David'
WHERE Nombre = 'Miguel';

UPDATE MASTERS
SET Coste = Coste + 5000;
```

*Hay que poner cuidado y poner ```WHERE``` para modificar solo los registros que queremos. Para asegurarme de que estoy modificando lo que quiero, puedo hacer primero un ```SELECT``` para ver que la selección es correcta.


```sql
SELECT *
FROM ALUMNOS
WHERE Nombre = 'Miguel';

UPDATE ALUMNOS 
SET Edad = 27 
WHERE Nombre = 'Miguel';
```



<br>

**Sintaxis de DELETE**

```sql
DELETE FROM table_name; --Borra todos los registros

DELETE FROM table_name 
WHERE column_id > 1; -- Borra el registro con ID 1
```

Ejemplo SQL con tablas del inicio:

```sql
DELETE FROM ALUMNOS;

DELETE FROM ALUMNOS 
WHERE Nombre = 'Miguel';
```

Al igual que en el update, es recomendable hacer primero una búsqueda con el ```WHERE``` para asegurarnos de que vamos a borrar los registros que queremos.



## DATA DEFINITION LANGUAGE

Comandos más tipicos:

- CREATE: Para crear una nueva base de datos, table, indice o procedimiento.

- DROP: para borar de forma sencilla distintos objetos como base de datos, tablas o índices

- ALTER: se usa para agregar, borrar o modificar columnas de una tabla existente


<br>

**Sintaxis de CREATE**

```sql
CREATE DATABASE db_name -- creamos base de datos

CREATE TABLE table_name -- creamos tabla
```












## Constraints


**Primary Key**

Una clave primaria es una columna o grupo de columnas que se usa para identificar de forma única un registro en una tabla.


<br>

**Foreign Key**

La clave de relación es un campo o grupo de campos de una tabla que identifica de manera única una fila en otra tabla. En otras palabras, una clave foránea es definida en una tabla que referencia la clave primaria de otra tabla.


<br>

**UNIQUE**

A veces, se quiere que los valores almacenados en una columna o grupo de columnas sean unicos en toda la tabla. Para ello se usa UNIQUE para asegurar que el dato introducido no se repite

<br>

**NOT NULL**

En una tabla, el valor NULL es no conocido o información perdida. El valor NULL es diferente de una cadena vacía o un número cero. Por ejemplo, puede pedir a una persona una dirección de correo electrónico, si no la conoce, utiliza el valor NULL para insertarla en la columna de correo electrónico. Esto indica que la información en el momento de la inserción es desconocida. En caso de que la persona no tenga ninguna dirección de correo electrónico, puede actualizarla a una cadena vacía.

El valor NULL es muy especial. Por ejemplo, NULL no es igual a nada ni siquiera a NULL. Para comprobar si un valor es NULL o no, se utiliza el operador booleano IS NULL o IS NOT NULL. La expresión NULL = NULL devuelve NULL.


<br>
<br>

## _Clase 28/10/2022_



### **SQL JOINS**

<br>

<p align="center">
<img src="https://ingenieriadesoftware.es/wp-content/uploads/2018/07/sqljoin.jpeg" width=500px>
</p>

<br>


Los SQL JOINS se utilizan para cruzar diferentes tablas y conseguir valores que cumplan alguna de las condiciones booleanas de la tabla de arriba. 




Ejemplo SQL de INNER JOIN con tablas del inicio: Conseguir el alumno que estudia máster de MKT

- Usando ```WHERE```

```sql
SELECT A.Nombre M.Nombre FROM ALUMNOS A, ALU_MASTER AM, MASTER M
WHERE A.ID = AM.ID_ALUMNO
AND AM.ID_MASTER = M.ID
AND M.Nombre = 'MKT'
```


- Usando ```JOIN```

```sql
SELECT A.Nombre M.Nombre 
FROM ALUMNOS A
JOIN ALU_MASTER AL 
ON A.ID = AM.ID_ALUMNO
JOIN MASTERS M
ON AM.ID_MASTER = M.ID
WHERE M.Nombre = 'MKT'
```



Páginas web para recordar los diferentes tipos de joins:

<https://joins.spathon.com/> 

<https://sql-joins.leopard.in.ua/> Mejor esta


<br>

### **FUNCIONES ESPECIALES SQL**


```sql
COUNT(*) --Cuenta filas

SUM(<column>) -- Suma la columna

AVG(<column>) -- Media de la columna

MIN(<column>) -- Mínimo de la columna

MAX(<column>) -- Máximo de la columna

LIMIT <num> -- Devuelve <num> filas
```





** Web con servidor SQL **

<http://35.198.74.120:9999/browser>



[bigquery]: <https://cloud.google.com/bigquery>


