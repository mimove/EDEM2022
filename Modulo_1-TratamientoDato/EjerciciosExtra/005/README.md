# Description

Con la solución del 4 funcionando, si ahora queremos instertar con un contenedor en python qué necesitamos incluir?


## _Notas Miguel_

Se ha modificado el archivo de Python del ejercicio 004 para incluir el uso de la librería ```mysql-connector-python``` (importante utilizar esta librería, ya que la librería mysql-connector tiene fallos al estar obsoleta) para poder realizar queries desde el archivo Python. Se ha dockerizado el archivo python dentro del directorio con el mismo nombre, y se ha creado un volumen ```dbdata``` que se utiliza para intercambiar los archivos .csv que modifica el script de python con el directorio de MySQL ```/var/lib/mysql-files/```.


