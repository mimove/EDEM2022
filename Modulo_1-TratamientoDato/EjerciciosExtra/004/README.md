# Description

¿Qué pasa si quisieramos usar MySQL en lugar de postgres? Siguiendo el ejercicio 3 completa de manera correcta el docker compose para conseguir lo mismo.


## _Notas Miguel_

Se ha modificado el archivo de Python del ejercicio 003 que sirve para modificar los CSV generados con datos aleatorios en la web mockaroo. Además, a partir de estos CSV (que son cargados directamente con queries en la base de datos), se generan n entradas aleatorias tanto de ventas como de order_status. Se ha conectado el directorio ./db/ que tiene los archivos CSV con los datos de producto, ciudades, países, etc. a un directorio específico (/var/lib/my-sql-files/) dentro del contenedor para poder acceder a los CSV una vez se dockeriza la aplicación. Hay que utilizar este directorio del contendor, ya que si no salta un error con la siguiente info: "The MySQL server is running with the --secure-file-priv option so it cannot execute this statement", lo que hace referencia a que, por defecto, el contenedor de MySQL tiene activada la función de ```secure-file-priv``` y solo permite leer archivos desde ese directorio.
`