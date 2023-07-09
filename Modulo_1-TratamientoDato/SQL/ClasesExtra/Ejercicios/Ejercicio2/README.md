# Pasos para ejecutar el proyecto

1. Levantar el docker-compose
```bash
docker-compose up -d
```

2. Instalar un cliente de mysql (ejemplo: mysql workbench) y conectarse a la base de datos
```bash
sudo apt-get install mysql-client
````

```bash
brew install mysql
```

3. Ejecutar el siguiente comando
```bash
mysql -h localhost --port 3306  -u user --password=password --protocol=tcp --database=edem_db
```

4. Ejecutar los siguientes comandos en orden
   
   - Crear la base de datos
   ```bash
   source tablas.sql
    ```
    - Llenar las tablas
    ```bash
    source alumnos.sql
    source master.sql
    source alumnos_master.sql
    ```
    - Ejecutar queries
    ```bash
    source queries.sql
    ```