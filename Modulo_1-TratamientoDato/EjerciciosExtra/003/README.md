# Description

En este ejemplo podéis ver como setear de manera completa un db de postgres con pgadmin. El siguiente paso es que creéis un fichero SQL que se llame fill data y rellenéis mediante inserts las tablas definidas en create_table.sql



## _Notas Miguel_

Se ha creado un archivo de Python que sirve para modificar los CSV generados con datos aleatorios en la web mockaroo. Además, a partir de estos CSV (que son cargados directamente con queries en la base de datos), se generan n entradas aleatorias tanto de ventas como de order_status. Se ha conectado el directorio ./db/ que tiene los archivos CSV con los datos de producto, ciudades, países, etc. a un directorio dentro del contenedor para poder acceder a los CSV una vez se dockeriza la aplicación.





