# Notas clase AirFlow

## _Clase 14/01/2023_

Es una plataforma para automatizar, programar y monitorizar workflows. 

- Scheduler: Analiza los DAG, comprueba los intervalos programados y transfiere las tareas a los trabajadores
- 
- Worker: Asume las tareas y realiza el trabajo.

- Webserver: proporciona la interfaz de usuario.

- Metadata DB: guarda la información sobre cada operador (start, end, stat, etc.)


<p align="center">
<img src="https://docs.datafabric.hpe.com/70/Airflow/images/Airflow_architecture.png" width = 500px>
</p>


## Tipos de ejecutores

- Ejecutor local: 2 tipos, ejecutor secuencial y ejecutor local. El local es el que más se usa ya que permite ejecutar tareas en paralelo.

- Ejecutores remotos: 2 tipos, ejecutor celery y ejecutor kubernetes. Celery utiliza una cola en la que va cargando y distribuyendo tareas en los workers. Kubernetes, hace lo mismo que celery pero sin cola. Es decir, kubernetes va creando pods con 1 o varios contenedores de docker que se crean, lanzan la tarea y se destruyen.

## DAG: Directed Acyclic Graph

Es dirigido porque las tareas se pueden organizar. Es acíclico porque tiene principio y fin. 

- Branches:

<p align="center">
<img src="https://airflow.apache.org/docs/apache-airflow/1.10.6/_images/branch_with_trigger.png" width = 500px>
</p>


  
## Tasks

Son la unidad básica de operación. Algunos tipos son

- Operadores: plantillas de tasks predefinidas (Ej: PythonOperator, BashOperator, EmptyOperator)

- Dependencias: Ejemplo << or >>

- Instancias: ejecuciones especificas de tasks. Los estados pueden ser: none, scheduled, queued, running, success, failed, etc.


- Trigger rules: all_sucess, all_failed, all_done, all_skipped, one_failed, one_done, none_failed, none_skipped, always


## Concurrency

Número de items (DAGs, tasks, etc) que se pueden ejecutar en parallelo

- Installation level: MAX_ACTIVE_TASKS_PER_DAT, MAX_ACTIVE_RUNS_PER_DAT, etc.

- DAG level: max_active_tasks, max_active_runs

- Task level: Pool, max_active_tis_per_dag



